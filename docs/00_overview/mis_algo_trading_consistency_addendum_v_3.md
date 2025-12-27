# MIS Algo Trading – Consistency Addendum (v3)

> **Status:** FINAL – Locked Operational Decisions (Runtime Mode Added)  
> **Supersedes:** Consistency Addendum (v2)

This addendum incorporates the **runtime mode separation (TEST vs PROD)** and locks all operational wiring decisions related to market data and order execution.  
It does **not modify strategy logic, algorithms, or risk rules**.

This document has **higher precedence** than all algorithm and architecture documents except **Final Requirements (v2)**.

---

## 1. Runtime Mode (FINAL)

### Definition

A global configuration parameter is introduced:

```
runtime_mode: TEST | PROD
```

This parameter determines **which external adapters are active**. Strategy, Renko, risk, and state logic remain unchanged.

---

## 2. TEST Mode Semantics (FINAL)

### Market Data Source

- **Yahoo Finance (yfinance)**
- No registration required
- Used for:
  - Historical OHLC (Daily, 1H, 15m, 5m)
  - Simulated intraday price progression

⚠️ Notes:
- Data may be delayed
- No true tick stream
- Suitable for **functional testing only**, not live trading realism

### Order Execution

- **Simulated Order Adapter**
- Orders are filled internally
- Partial fills may be simulated deterministically

### Capital Handling

- Fully simulated
- Uses same Capital & Risk Algorithm

### Intended Use

- Logic validation
- Indicator correctness
- Renko correctness
- End-to-end dry runs

---

## 3. PROD Mode Semantics (FINAL)

### Market Data Source

- **Dhan WebSocket APIs**
- Real-time bid/ask and LTP

### Order Execution

- **Dhan Order APIs**
- MIS intraday orders

### Capital Handling

- Real account capital
- Broker is source of truth

### Intended Use

- Live trading only

---

## 4. Adapter Binding Rules (FINAL)

```
IF runtime_mode == TEST:
    MarketDataAdapter  = YahooMarketDataAdapter
    OrderAdapter       = SimulatedOrderAdapter

IF runtime_mode == PROD:
    MarketDataAdapter  = DhanMarketDataAdapter
    OrderAdapter       = DhanOrderAdapter
```

No hybrid combinations are permitted.

---

## 5. Invariants (Reconfirmed)

- Strategy logic is identical in TEST and PROD
- Risk rules are identical in TEST and PROD
- Persistence rules are identical in TEST and PROD
- Only adapters differ

---

## 6. Authority & Precedence (Reconfirmed)

1. Final Requirements (v2)
2. Consistency Addendum (v3)
3. Algorithm Documents
4. Architecture Document
5. Code

---

## 7. Status

With this addendum:

- Runtime wiring is fully specified
- No ambiguity remains between testing and production behavior
- The system remains implementation-ready

Any future change requires:
- Addendum update
- Version bump

---

**End of Consistency Addendum (v3)**

