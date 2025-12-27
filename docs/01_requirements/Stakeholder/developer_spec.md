# Stakeholder Requirement – Developer Spec

Developer Spec - MIS Multi Timeframe Renko RSI MACD
Purpose - 
This document describes a production-ready intraday MIS trading bot that executes on Renko bricks (TF4). It uses intrabar Heikin-Ashi on TF1/TF2/TF3 and subscribes to a live tick feed. All trading decisions occur only on completed Renko brick events. Renko brick size is computed once weekly and stays constant for the week.
All datetimes are tz-aware Asia/Kolkata. Use Decimal for all price and money arithmetic. Use quantize with ROUND_HALF_UP for rounding to renko_round_decimals.


1. Quick config (UI-exposed)
Provide these as UI-configurable fields (defaults in parentheses):
equity : Decimal
risk_per_trade_pct : float (e.g., 1.0)
risk_buffer_pct : float (e.g., 0.10)
risk_per_trade_min_pct : float (optional)
risk_per_trade_max_pct : float (optional)
margin_cap_pct : float (5.0)
margin_requirement : float (fraction or per symbol fallback)
leverage : int
entry_window_start : string (e.g., "09:30 IST")
entry_window_end : string (e.g., "11:00 IST")
force_close_time : string (e.g., "15:15 IST")
max_spread_pct : float (0.1)
Renko-specific
renko_method : string — highest_atr_div4 | percentile_midpoint_div4 (default highest_atr_div4)
renko_divisor : float (default 4.0)
renko_atr_sample_candles : int (default 375)
renko_percentile_low : float (default 5.0) — for percentile method (configurable)
renko_percentile_high : float (default 95.0) — for percentile method (configurable)
renko_round_decimals : int (default 3)
renko_rebuild_time : string (default "Fri 16:00 IST")
renko_min_floor : Decimal (default 0.001)
Volatility & concurrency
volatility_threshold_pct : float (default 1.05)
volatility_second_threshold : float (default 1.02)
allow_multiple_positions_per_symbol : bool (default false)
use_intrabar_HA : bool (default true)
partial_fill_policy : string ("accept_immediate")
logging_level : string
persistence_path : string or DB connection

2. Broker / Data Adapter contract (summary)
Adapter must provide tz-aware Asia/Kolkata timestamps and the following functions (same as Version 1 but clarified):
get_historical_candles(symbol, timeframe, limit) → list [OHLCV] (OHLCV includes start_ts, end_ts)
subscribe_ticks(symbols, callback) → tick feed entries with bid, ask, last, ts, symbol
get_bid_ask(symbol) → (bid, ask)
place_market_order(symbol, side, quantity, client_order_id=None) → (order_id, executed_qty, executed_avg_price)
get_open_positions() → list
close_position(position_id) → result
get_server_time() → tz-aware datetime Asia/Kolkata
get_margin_requirement(symbol) → fraction (fallback to global if missing)
Instrument metadata required: lot_size, min_qty, qty_step, price_tick, price_decimals, currency, exchange, trading_hours, product_type.
Price source for Renko formation: use bid/ask midpoint from tick feed (continuous). This replaces Version 1 ambiguity.

3. Indicators (explicit)
Use Decimal arithmetic, quantize outputs where needed. Standard definitions with explicit parameters:
Heikin-Ashi (intrabar) — compute per tick using last closed 5-min candle for bar open/high/low then use last_price from tick for HA_close formula.
HA_close = (bar_open + bar_high + bar_low + last_price) / 4
HA_open = (prev_HA_open + prev_HA_close) / 2
HA_high = max(bar_high, HA_open, HA_close)
HA_low = min(bar_low, HA_open, HA_close)
RSI: period = 14
MACD: short=12, long=26, signal=9 → use MACD histogram (macd - signal)
EMA: EMA20 and EMA9_of_EMA20 (EMA(9) applied to the EMA20 series)
ATR: standard ATR with TR = max(high-low, abs(high-prev_close), abs(low-prev_close)), ATR period = 14 for ATR uses.
Supertrend: ATR period = 10, Multiplier = 3. Bands computed using (High+Low)/2 ± Multiplier × ATR, standard flip logic.

4. Renko brick size (final) — weekly job
Summary: brick size is computed once per week (at renko_rebuild_time) and persists for the week. Do not change during trading week. Use ATR(14) computed on 5-min Heikin-Ashi candles. After computing raw value apply raw = max(raw, renko_min_floor) and then round using Decimal quantize to renko_round_decimals with ROUND_HALF_UP.
Common inputs
n = renko_atr_sample_candles (default 375)
divisor = renko_divisor (default 4.0)
round_decimals = renko_round_decimals (default 3)
Method 1 — highest_atr_div4 (user preference)
Compute ATR(14) for each of the last n 5-min Heikin-Ashi candles → atr_vals.
max_atr = max(atr_vals).
raw_brick = max_atr / renko_divisor.
raw_brick = max(raw_brick, renko_min_floor).
renko_brick_size = Decimal(raw_brick).quantize(Decimal(10) ** -renko_round_decimals, rounding=ROUND_HALF_UP).
Persist renko_brick_size for the week.
Method 2 — percentile_midpoint_div4 (user preference)
Compute ATR(14) for each of the last n 5-min Heikin-Ashi candles → atr_vals.
Sort ascending. Let p_low = renko_percentile_low / 100 and p_high = renko_percentile_high / 100 (defaults: 5% and 95%).
Compute nearest-rank percentile values using index = round(p × (n + 1)) clamped to [1, n].
v_low = value at p_low percentile index.
v_high = value at p_high percentile index.
midpoint = (v_low + v_high) / 2.
raw_brick = midpoint / renko_divisor.
raw_brick = max(raw_brick, renko_min_floor).
renko_brick_size = Decimal(raw_brick).quantize(Decimal(10) ** -renko_round_decimals, rounding=ROUND_HALF_UP).
Persist renko_brick_size for the week.
Notes
The percentile endpoints (renko_percentile_low and _high) are configurable but default to 5% and 95%.
Use Decimal throughout and ensure persisted value is exact to renko_round_decimals.
Weekly job: run at renko_rebuild_time. If scheduled time falls while market closed, run at next pre-market/open time before trading starts.

5. Renko formation (tick-by-tick — exact rules)
box = renko_brick_size.
last_close = close price of last saved Renko brick.
P = (bid + ask) / 2 from current tick (bid/ask midpoint).
diff = P - last_close.
If diff >= box: k = floor(diff / box) → append k up-bricks sequentially.
If diff <= -box: k = floor(abs(diff) / box) → append k down-bricks sequentially.
For each appended brick set brick_open = previous_close, brick_close = previous_close ± box, direction, and timestamp = tick time when brick was formed.
After appending k >= 1 bricks evaluate strategy once using the last appended brick. Log all appended bricks and timestamps.
Notes on reversal: natural reversal requires traversing previous bricks; multi-brick append logic handles this automatically.

6. Persisted state (per-symbol, atomic)
Persist an atomic record per symbol (DB transaction or write-temp + atomic rename). Fields:
renko_brick_size (Decimal)
renko_series or last_index
last_renko_bar_time (tz-aware)
Flags: emaAlignedBuy, emaAlignedSell, supertrendReadyBuy, supertrendReadySell
prev_supertrend_direction, last_supertrend_flip_timestamp
refClose (Decimal) — renko-derived reference price
open_trade_state: { trade_open: bool, entryPrice: Decimal, entryQuantity: int, entry_side: "BUY"|"SELL" }
last_persist_ts
Persist after every renko append, flag change, or trade state change.

7. Flagging rules (EMA alignment & Supertrend readiness)
EMA alignment (TF4 Renko)
emaAlignedBuy = true if EMA20 >= EMA9_of_EMA20 OR EMA20 crossed from ≤ to > EMA9_of_EMA20 within current Renko bar.
emaAlignedSell = true if EMA20 <= EMA9_of_EMA20 OR EMA20 crossed from ≥ to < within current Renko bar.
Supertrend readiness (TF4)
supertrendReadyBuy: Supertrend flips down→up AND the immediately preceding downtrend had at least one macd_hist < 0. When set, record refClose = min(close of bearish Renko bricks) in that downtrend.
supertrendReadySell: Supertrend flips up→down AND the immediately preceding uptrend had at least one macd_hist > 0. Record refClose = max(close of bullish Renko bricks).
Flags persist until used or until Supertrend flips back (reset).

8. TF rules (intrabar applied)
Use Heikin-Ashi aggregated from 5-min candles + intrabar HA computed from ticks.
TF1 (Daily HA): BUY bias when HA_close > HA_open AND RSI > 60 AND RSI_current > RSI_previous. SELL bias is the inverse.
TF2 (1H HA): trend/momentum confirmation similar to TF1 plus EMA check on Renko (EMA alignment flag).
TF3 (15m HA): Volatility filter passes if ATR rising 2 bars OR ATR_t / ATR_EMA >= volatility_threshold_pct AND ATR_t / ATR_{t-1} >= volatility_second_threshold. Momentum via MACD_hist rising.
Momentum rule (clarified): At least one of TF2 or TF3 momentum must be aligned with the trade side for an entry to be valid.

9. Entry conditions (evaluated on new Renko brick)
Place an entry only when all of the following are true:
TF1 bias matches trade side.
emaAlignedSide AND supertrendReadySide are true.
TF2 and/or TF3 momentum check passes (at least one aligned with trade side).
TF3 volatility check passes.
Current time within entry_window_start and entry_window_end.
Spread ≤ max_spread_pct.
Computed quantity >= 1.
If all true place market order (see order execution rules). Quantity computation uses Renko-derived refClose and priceThreshold (do not use raw tick price for priceThreshold).

10. Position sizing (explicit formulas)
All money/price arithmetic uses Decimal. Rounding rules: quantities rounded down to instrument qty_step and respect lot_size.
Effective risk percent
base = risk_per_trade_pct
effective_risk_pct = max(0.0001, base - risk_buffer_pct)
risk_amount = equity * (effective_risk_pct / 100)
Per-share risk (Renko priceThreshold)
BUY: priceThreshold = refClose - renko_brick_size (Renko price)
per_share_risk = entryPrice - priceThreshold
SELL: priceThreshold = refClose + renko_brick_size
per_share_risk = priceThreshold - entryPrice
If per_share_risk <= 0 abort entry and log.
Qty by risk
qty_risk = floor(risk_amount / per_share_risk)
Qty by margin
max_trade_value = equity * (margin_cap_pct / 100)
qty_margin = floor(max_trade_value / (entryPrice * margin_requirement))
Final quantity
quantity = max(1, min(qty_risk, qty_margin))
Apply instrument lot_size and qty_step (round down to nearest permitted lot). If resulting quantity < min_qty abort and log.

11. Order execution & partial fills
Acquire per-symbol mutex lock.
Place market order for computed quantity.
On broker response:
Fully filled: record entryPrice, entryQuantity.
Partially filled: accept executed quantity immediately; do not retry remainder. Persist executed avg price/qty. Cancel remainder per broker behavior. Log details.
Release lock then immediately re-evaluate the latest snapshot (see concurrency below).

12. Exit rules (evaluated on each Renko brick)
Priority order:
Price-based stop (highest priority)
BUY: exit if currentRenkoClose <= refClose - renko_brick_size.
SELL: exit if currentRenkoClose >= refClose + renko_brick_size.
Supertrend flip (profit-only exit)
BUY: on flip up→down exit only if currentRenkoClose > entryPrice.
SELL: on flip down→up exit only if currentRenkoClose < entryPrice.
Force-close at force_close_time — market order to close any open positions.
After exit reset trade_open state and relevant flags. No hard stop orders are placed by default.

13. Multi-brick creation & concurrency (real-time, latest-snapshot-only)
Multi-brick append: compute k = floor(abs(diff) / box) and append sequentially. Evaluate only on last appended brick.
Per-symbol lock: acquire mutex prior to submitting orders. While lock held continue renko building and indicator computation but suppress order submissions.
Latest-snapshot-only policy: while lock held store only the most recent snapshot (renko_index, renko_close, flags, indicators, server_time`) — overwrite older snapshots.
On lock release: re-evaluate latest snapshot. If conditions still valid and allow_multiple_positions_per_symbol permits, act immediately. Otherwise drop snapshot and log.
Partial fills accepted. On lock release re-evaluate to decide scale-in only if allow_multiple_positions_per_symbol = true.
Rationale: keep decisions fast and act on freshest market state.

14. Persistence & restart behavior
Persist full per-symbol record atomically after renko append, flag change, or trade state change.
On restart reconcile persisted open trades with broker positions.
Keep replay buffer (developer choice) for at least last 10k renko events or 30

