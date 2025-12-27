# Requirements Traceability Matrix (RTM)

## Project: MIS Multi‑Timeframe Renko Trading Strategy

**Source of Truth**  
- Stakeholder Requirements: MIS Multitimeframe RSI MACD histogram_ renko_ Heikenashi_ EMA_Final.docx  
- Developer Specification: Developer Spec - Mis Multi Timeframe Renko Heikenashi Rsi Macd EMA_Final.docx

---

## Stakeholder → Software Trace (Top-Level)

This table establishes **root traceability** from stakeholder intent to executable software requirements. It is the authoritative WHY → WHAT mapping.

| Stakeholder Req ID | Stakeholder Requirement | Source Doc | Software Req IDs |
|------------------|------------------------|------------|------------------|
| STK-MIS-01 | Intraday MIS trading only | Stakeholder DOCX | MIS-REQ-01 |
| STK-MIS-02 | Entry allowed only between 09:30–11:00 IST | Stakeholder DOCX | MIS-REQ-02 |
| STK-MIS-03 | Forced square-off at 15:15 IST | Stakeholder DOCX | MIS-REQ-03 |
| STK-MIS-04 | Weekly Renko brick size calculation | Stakeholder DOCX | MIS-REQ-04, MIS-REQ-13, MIS-REQ-14 |
| STK-STR-01 | Multi-timeframe confirmation required | Stakeholder DOCX | MIS-REQ-17–MIS-REQ-21 |
| STK-STR-02 | EMA + Supertrend order-independent entry | Stakeholder DOCX | MIS-REQ-18, MIS-REQ-19 |
| STK-RISK-01 | Risk per trade ≤ 1% equity | Stakeholder DOCX | MIS-REQ-23 |
| STK-RISK-02 | Margin usage cap per trade | Stakeholder DOCX | MIS-REQ-24 |
| STK-EXIT-01 | Price-based Renko stop mandatory | Stakeholder DOCX | MIS-REQ-26 |
| STK-EXIT-02 | Profit-only Supertrend exit | Stakeholder DOCX | MIS-REQ-27 |
| STK-SYS-01 | Safe restart & persistence | Stakeholder DOCX | MIS-REQ-31, MIS-REQ-32 |

---

## RTM Legend
- ✅ Covered & Implemented
- ⚠ Partially Covered / Needs Review
- ❌ Missing / To Be Implemented

---

## 1. Trading Scope & Constraints

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-01 | Intraday MIS trading only | Stakeholder | Config + runtime checks | ❌ | ⚠ |
| MIS-REQ-02 | Entry window 09:30–11:00 IST | Stakeholder | Time guard in entry logic | ❌ | ⚠ |
| MIS-REQ-03 | Force close all positions at 15:15 IST | Stakeholder | Force-close scheduler | ❌ | ⚠ |
| MIS-REQ-04 | Weekly Renko rebuild before trading week | Dev Spec | Renko job module | ❌ | ⚠ |

---

## 2. Data & Time Handling

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-05 | All timestamps tz-aware Asia/Kolkata | Dev Spec | Time utils | ❌ | ⚠ |
| MIS-REQ-06 | Use bid/ask midpoint for Renko | Dev Spec | Tick adapter | ❌ | ⚠ |
| MIS-REQ-07 | Decimal arithmetic with ROUND_HALF_UP | Dev Spec | Math utils | ❌ | ⚠ |

---

## 3. Indicator Calculations

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-08 | Heikin-Ashi intrabar logic | Dev Spec | Indicator module | ❌ | ⚠ |
| MIS-REQ-09 | RSI(14) | Both | Indicator module | ❌ | ⚠ |
| MIS-REQ-10 | MACD histogram (12,26,9) | Both | Indicator module | ❌ | ⚠ |
| MIS-REQ-11 | EMA20 & EMA9-of-EMA20 | Both | Indicator module | ❌ | ⚠ |
| MIS-REQ-12 | Supertrend (10,3) | Both | Indicator module | ❌ | ⚠ |

---

## 4. Renko Logic

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-13 | Weekly ATR-based Renko brick size | Dev Spec | Renko builder | ❌ | ⚠ |
| MIS-REQ-14 | Percentile-based Renko option | Dev Spec | Renko builder | ❌ | ⚠ |
| MIS-REQ-15 | Multi-brick append on large moves | Dev Spec | Renko builder | ❌ | ⚠ |
| MIS-REQ-16 | Evaluate strategy only on last appended brick | Dev Spec | Strategy engine | ❌ | ⚠ |

---

## 5. Entry Logic

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-17 | TF1 Daily HA bias rules | Stakeholder | Strategy engine | ❌ | ⚠ |
| MIS-REQ-18 | EMA alignment flags | Both | Flag engine | ❌ | ⚠ |
| MIS-REQ-19 | Supertrend readiness with MACD history | Both | Flag engine | ❌ | ⚠ |
| MIS-REQ-20 | TF2 / TF3 momentum filter | Both | Strategy engine | ❌ | ⚠ |
| MIS-REQ-21 | TF3 volatility filter | Both | Strategy engine | ❌ | ⚠ |
| MIS-REQ-22 | Spread ≤ max_spread_pct | Stakeholder | Execution guard | ❌ | ⚠ |

---

## 6. Position Sizing & Risk

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-23 | Risk % based sizing | Both | Risk module | ❌ | ⚠ |
| MIS-REQ-24 | Margin cap per trade | Both | Risk module | ❌ | ⚠ |
| MIS-REQ-25 | Lot size & qty step compliance | Dev Spec | Order sizing | ❌ | ⚠ |

---

## 7. Exit Logic

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-26 | Renko price-based stop | Both | Exit engine | ❌ | ⚠ |
| MIS-REQ-27 | Supertrend flip profit-only exit | Both | Exit engine | ❌ | ⚠ |
| MIS-REQ-28 | Exit priority ordering | Both | Exit engine | ❌ | ⚠ |

---

## 8. Concurrency & Persistence

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-29 | Per-symbol mutex | Dev Spec | Execution layer | ❌ | ⚠ |
| MIS-REQ-30 | Latest-snapshot-only policy | Dev Spec | Concurrency control | ❌ | ⚠ |
| MIS-REQ-31 | Atomic persistence per symbol | Dev Spec | Persistence layer | ❌ | ⚠ |
| MIS-REQ-32 | Restart reconciliation | Dev Spec | Startup logic | ❌ | ⚠ |

---

## 9. Logging & Observability

| Req ID | Requirement | Source | Implementation | Tests | Status |
|------|-------------|--------|----------------|-------|--------|
| MIS-REQ-33 | Trade & decision logging | Stakeholder | Logger | ❌ | ⚠ |
| MIS-REQ-34 | Configurable logging level | Dev Spec | Logger | ❌ | ⚠ |

---

## Summary

- Requirements are **fully defined** (excellent input quality).
- Most logic appears **implemented**, but **test coverage & explicit traceability are missing**.
- No requirement is currently marked ❌ because code exists, but **validation is required**.

**Next phase**: Design ↔ Code alignment + Unit Test gap closure.

