# Stakeholder Requirement â€“ Strategy Spec

Strategy Summary
Multi-timeframe trend-following Renko system using Heikin Ashi directional bias, momentum filters (MACD, RSI), and Supertrend-based entry and exit validation. Risk-based Quantity ensures consistent exposure. All logic is evaluated only on the creation of a new Renko bar.
This strategy will be used to trade MIS stocks available for trading via broker Dhan (5x times leverage).
UI interface will be required for control and analysis.
Trading logic is based on inputs from multiple charts.
â€¢ Chart 1 (TF1): Heikin Ashi Daily (adjustable)
â€¢ Chart 2 (TF2): Heikin Ashi 1 Hour (adjustable)
â€¢ Chart 3 (TF3): Heikin Ashi 15 min (adjustable)
â€¢ Execution Chart (TF4): Renko chart (calculated by bot, refer notes section)

### Directional Bias â€“ Chart 1 (TF1 - HA Daily)
1. If HA Close > HA Open, RSI > 60, Current RSI > Previous RSI   â†’ Bias is BUY
2. If HA Close < HA Open, RSI < 40, Current RSI < Previous RSI   â†’ Bias is SELL
3. If HA Close = HA Open â†’ treat as no bias / skip entries.

### Chart 2 (TF2 - HA 1H) Indicators
1. 20-Period EMA
2. 9-Period EMA of the 20 EMA (source = 20 EMA)
3. RSI (14) with levels 60 and 40
4. MACD Histogram

### Chart 3 (TF3 - HA 15 mins) Indicator
MACD Histogram
ATR (14) and 9 EMA of ATR (14)

### Chart 4 (TF4 - Renko Execution Chart) Indicators
1. 20 EMA
2. 9 EMA of the 20 EMA (source = 20 EMA)
3. MACD Histogram
4. Supertrend (Period = 10, Multiplier = 3)

### BUY Entry Condition - Evaluated only when a new Renko bar is created.
Proceed only if TF1 bias is BUY. All of the following must be true:

TF4 (Renko Execution) - Entry Conditions
Proceed only if TF1 bias is BUY. All of the following must be true before triggering:

1. EMA condition: either
a. 20 EMA crosses above its 9 EMA (9-period EMA of the 20 EMA), or
b. 20 EMA is already above its 9 EMA.
- Track this as a boolean flag `emaAlignedBuy` which becomes true once EMA20 > EMA9 or upon 20 EMA crossing up its 9 EMA.


2. Supertrend flip with historical MACD check:
- When Supertrend flips from downtrend to uptrend, identify the immediately preceding downtrend phase.
- During that downtrend phase, MACD histogram must have been negative at least once.
- If this check passes, set a flag `supertrendReadyBuy = true`.
- After the flip, MACD state no longer matters.




3. Order-independence:
- The trade should trigger only once both `emaAlignedBuy` and `supertrendReadyBuy` are true.
- If `emaAlignedBuy` becomes true first, wait for `supertrendReadyBuy` on the next valid flip.
- If `supertrendReadyBuy` becomes true first, wait for `emaAlignedBuy` (cross or existing) before entry.
4. Reset:
- After triggering a BUY, reset both flags.
- If Supertrend returns to downtrend, reset `supertrendReadyBuy` until the next flip with MACD check.

5. Only after both flags are true, and TF2/TF3 momentum filters hold, trigger BUY on the next Renko bar.
#### TF3 and TF2 - Momentum Filter
- The current MACD Histogram value must be greater than the previous value on either of TF2 or TF3.
#### TF3 - Volatility filter
Pass volatility filter if either:
a) ATR rising for 2 consecutive bars (ATR_t > ATR_t-1 and ATR_t-1 > ATR_t-2), OR
b) ATR_t / ATR_EMA >= 1.05 (i.e. 5%) and ATR_t / ATR_t-1 >= 1.02 (i.e. 2%). (Percent adjustable)
ATR EMA is 9 period EMA of current ATR which is 14 period

#### TF2 (HA 1H) - Trend + Momentum Confirmation
1. 20 EMA > 9 EMA (or crosses from â‰¤ to >)
2. HA Close > HA Open
3. RSI > 60
4. Current RSI > Previous RSI





1. Trade Setup: BUY (At Entry)
When a BUY trade is executed:
entryPrice = Renko close price at BUY entry
refClose = Close price of the lowest bearish Renko brick (Close < Open) during the Supertrend downtrend phase immediately before the Supertrend flipped to uptrend
renkoBrickSize = size (price range) of a single Renko brick
priceThreshold = refClose - renkoBrickSize (used for price-based exit)

Position sizing
ï‚· Risk Control
Risk â‰¤ 1% of total equity per trade (adjustable).
ï‚· Margin Cap
Margin used per trade â‰¤ 5% of equity (adjustable).
ï‚· Max Trade Value
Max Trade Value = min ((Equity X Margin Cap/Margin requirement), x% of Equity)

BUY Trade Exit Logic (Renko + Supertrend)
Price-Based Exit (Each Renko Bar)
â€¢	On every new Renko brick:
If currentRenkoClose <= (refClose - renkoBrickSize) â†’ Exit BUY trade immediately
This indicates price moved at least one Renko brick below the last bearish reference close - signalling loss beyond tolerance.

Supertrend Flip Exit (Conditional)
â€¢	Continuously monitor the Supertrend direction.
When Supertrend flips from uptrend to downtrend:
If currentRenkoClose > entryPrice (i.e., the BUY trade is in profit) â†’ Exit the trade
Else (if currentRenkoClose <= entryPrice) â†’ Do not exit
Continue holding the BUY trade.
Wait for the Supertrend to flip back to uptrend, then evaluate the next down-flip for potential exit only if the trade is in profit at that time.
â€¢	Repeat this flip-evaluate cycle until either:
The price-based exit is hit, or
A Supertrend flip occurs while in profit
3. Order of Evaluation (Per Renko Bar)
Price Check:
If renkoClose <= (refClose - renkoBrickSize) â†’ exit BUY
Supertrend Flip Check:
If Supertrend flips from up to down and renkoClose > entryPrice â†’ exit BUY


Else: continue holding
Pseudocode snippet:
if renkoClose <= (refClose - renkoBrickSize):
exitTrade("BUY")
elif prevSupertrend == 'up' and currentSupertrend == 'down':
if renkoClose > entryPrice:
exitTrade("BUY")
# else: hold trade

4. Reset After Exit
After closing the BUY trade:
Reset:
entryPrice
refClose
Quantity
Supertrend state trackers (e.g. prevSupertrendState)






### SELL Entry Condition - Evaluated only when a new Renko bar is created
Proceed only if TF1 bias is SELL. All of the following must be true:

TF4 (Renko Execution) - Entry Conditions
Proceed only if TF1 bias is SELL. All of the following must be true before triggering:

1. EMA condition: either
a. 20 EMA crosses below its 9 EMA (9-period EMA of the 20 EMA), or
b. 20 EMA is already below its 9 EMA.
- Track this as a boolean flag `emaAlignedSell` which becomes true once EMA20 < EMA9 or upon 20 EMA crossing down its 9 EMA.

2. Supertrend flip with historical MACD check:
- When Supertrend flips from uptrend to downtrend, identify the immediately preceding uptrend phase.
- During that uptrend phase, MACD histogram must have been positive at least once.
- If this check passes, set a flag `supertrendReadySell= true`.
- After the flip, MACD state no longer matters.

3. Order-independence:
- The trade should trigger only once both `emaAlignedSell` and `supertrendReadySell` are true.
- If ` emaAlignedSell` becomes true first, wait for `supertrendReadySell` on the next valid flip.
- If `supertrendReadySell` becomes true first, wait for `emaAlignedSell` (cross or existing) before entry.



4. Reset:
- After triggering a SELL, reset both flags.
- If Supertrend returns to uptrend, reset `supertrendReadySell` until the next flip with MACD check.

5. Only after both flags are true, and TF2/TF3 momentum filters hold, trigger SELL on the next Renko bar.

#### TF3 and TF2 - Momentum Filter
- The current MACD Histogram value must be lesser than the previous value on either of TF2 or TF3.
#### TF3 - Volatility filter
Pass volatility filter if either:
a) ATR rising for 2 consecutive bars (ATR_t > ATR_t-1 and ATR_t-1 > ATR_t-2), OR
b) ATR_t / ATR_EMA >= 1.05 (i.e. 5%) and ATR_t / ATR_t-1 >= 1.02 (i.e. 2%). (Percent adjustable)
ATR EMA is 9 period EMA of current ATR which is 14 period

#### TF2 (HA 1H) - Trend + Momentum Confirmation
1. 20 EMA < 9 EMA (or crosses from â‰¥ to <)
2. HA Close < HA Open
3. RSI < 40
4. Current RSI < Previous RSI

1. Trade Setup: SELL (At Entry)
When a SELL trade is executed:
entryPrice = Renko close price at SELL entry
refClose = Close price of the highest bullish Renko brick (Close > Open) during the Supertrend uptrend phase immediately before the Supertrend flipped to downtrend
renkoBrickSize = size (price range) of a single Renko brick
priceThreshold = refClose + renkoBrickSize (used for price-based exit)

Position sizing
ï‚· Risk Control
Risk â‰¤ 1% of total equity per trade (adjustable).
ï‚· Margin Cap
Margin used per trade â‰¤ 5% of equity (adjustable).
ï‚· Max Trade Value
Max Trade Value = min ((Equity X Margin Cap/Margin requirement), x% of Equity)


SELL Trade Exit Logic (Renko + Supertrend)
Price-Based Exit (Each Renko Bar)

On every new Renko brick:
If currentRenkoClose >= (refClose + renkoBrickSize) â†’ Exit SELL trade immediately
This indicates price moved at least one Renko brick above the last bullish reference close - signalling loss beyond tolerance.

Supertrend Flip Exit (Conditional)
â€¢	Continuously monitor the Supertrend direction.
When Supertrend flips from downtrend to uptrend:
If currentRenkoClose < entryPrice (i.e., the SELL trade is in profit) â†’ Exit the trade
Else (if currentRenkoClose >= entryPrice) â†’ Do not exit
Continue holding the SELL trade.
Wait for the Supertrend to flip back to downtrend, then evaluate the next up-flip for potential exit only if the trade is in profit at that time.

â€¢	Repeat this flip-evaluate cycle until either:
The price-based exit is hit, or
A Supertrend flip occurs while in profit

Order of Evaluation (Per Renko Bar)
Price Check:

If renkoClose >= (refClose + renkoBrickSize) â†’ exit SELL
Supertrend Flip Check:
If Supertrend flips from down to up and renkoClose < entryPrice â†’ exit SELL
Else: continue holding


Pseudocode snippet:
if renkoClose >= (refClose + renkoBrickSize):
exitTrade("SELL")
elif prevSupertrend == 'down' and currentSupertrend == 'up':
if renkoClose < entryPrice:
exitTrade("SELL")
# else: hold trade

Reset After Exit
After closing the SELL trade:
Reset:
entryPrice
refClose
Quantity
Supertrend state trackers (e.g. prevSupertrendState)
Notes -

Print a log of action taken by bot when executing a trade, exiting a trade and when not executing a trade.
Liquidity check - Entry should be market order only, and trade should be executed only if the percentage spread is less than or equal to 0.1% (adjustable).
Percentage spread = ((Ask Price - Bid Price)/(Ask+Bid/2)) X 100
I will be providing list of MIS stock eligible for trading.

Renko brick size - weekly job
Summary: brick size is computed once per week (at renko_rebuild_time) and persists for the week. Do not change during trading week. Use ATR (14) computed on 5-min Heikin-Ashi candles. After computing raw value apply raw = max (raw, renko_min_floor) and then round using Decimal quantize to renko_round_decimals with ROUND_HALF_UP.
Common inputs
n = renko_atr_sample_candles (default 375)
divisor = renko_divisor (default 4.0)
round_decimals = renko_round_decimals (default 3)
Method 1 â€” highest_atr_div4 (user preference)
Compute ATR (14) for each of the last n 5-min Heikin-Ashi candles â†’ atr_vals.
max_atr = max(atr_vals).
raw_brick = max_atr / renko_divisor.
raw_brick = max (raw_brick, renko_min_floor).
renko_brick_size = Decimal(raw_brick).quantize(Decimal(10) ** -renko_round_decimals, rounding=ROUND_HALF_UP).
Persist renko_brick_size for the week.
Method 2 â€” percentile_midpoint_div4 (user preference)
Compute ATR (14) for each of the last n 5-min Heikin-Ashi candles â†’ atr_vals.
Sort ascending. Let p_low = renko_percentile_low / 100 and p_high = renko_percentile_high / 100 (defaults: 5% and 95%).
Compute nearest-rank percentile values using index = round(p Ã— (n + 1)) clamped to [1, n].
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
________________________________________



Timing Requirement
The Renko brick size calculation and Renko chart generation process must run outside market hours.
This routine should be executed once per week, before the first trading session of the week.
By market open, the bot must already have the updated Renko data (with latest brick sizes) ready for all eligible stocks.

Other Timing Requirements
Entry Window: New trades may only be executed between 09:30 AM IST and 11:00 AM IST.
No Late Entries: After 11:00 AM IST, no new trades should be opened, even if valid signals appear.
Exit Logic: All trades must follow the defined exit rules (price-based exit and Supertrend flip exit).
End-of-Day Close: Any trade still open at 03:15 PM IST must be force-closed at market price, regardless of signals.

Position Sizing and Equity Handling
Equity Input (via UI): The user can set/update the equity value once daily before market open.
This equity value will be used for all position sizing calculations for that day.
Position size remains static for the trading day, regardless of intraday PnL.
Any equity updates during market hours apply only to the next trading day.






High level Flowchart â€“


