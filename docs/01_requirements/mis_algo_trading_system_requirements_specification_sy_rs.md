
# MIS Algo Trading System
## System Requirements Specification (SYRS)

**Revision:** B (Merged & Renumbered)  
**Status:** 🟢 Baselined after Phase 13.1.1 Inspection  
**Derived From:** Stakeholder Requirements + REM  
**Change Control:** Formal inspection only

---

## 1. Purpose

This document defines the **System Requirements** for the MIS Algo Trading System.
It represents a **merged and gap-free System Requirements baseline**, derived from:
- Stakeholder Requirements
- REM Consistency Addendum
- Phase 13.1.1 System Gap Corrections

---

## 2. System Scope & Context

The MIS Algo Trading System is an automated **intraday MIS trading system** that:
- Trades MIS-enabled equities via a broker
- Uses Renko-based decision logic with multi-timeframe indicators
- Operates in TEST and PROD execution modes

---

## 3. Execution Modes

### SYS-GEN-001 — Execution Mode Separation
The system shall support distinct TEST and PROD execution modes.

---

## 4. Trading Session & Lifecycle

### SYS-SES-001 — Intraday Operation
The system shall operate strictly within intraday trading sessions.

### SYS-SES-002 — Entry Window Enforcement
The system shall allow new trade entries only within the configured intraday entry window.

### SYS-SES-003 — No Late Entries
The system shall prevent initiation of new trades outside the defined entry window regardless of signal validity.

### SYS-SES-004 — Force-Close Requirement
The system shall forcibly close all open positions at the configured end-of-day force-close time.

---

## 5. Renko Brick Lifecycle & Pricing

### SYS-RNK-001 — Weekly Renko Brick Size Computation
The system shall compute the Renko brick size once per trading week.

### SYS-RNK-002 — Renko Brick Size Immutability
The system shall apply the computed Renko brick size consistently throughout the trading week.

### SYS-RNK-003 — Renko Brick Size Persistence
The system shall preserve the weekly Renko brick size across restarts and executions within the same week.

### SYS-RNK-004 — Midpoint Price Source
The system shall construct Renko bricks using the midpoint of the best available bid and ask prices.

### SYS-RNK-005 — Price Source Fallback
In the absence of valid bid and ask prices, the system shall apply a deterministic fallback price source.

---

## 6. Decision & Multi-Timeframe Semantics

### SYS-DEC-001 — Renko-Only Decision Authority
The system shall evaluate trade entry and exit decisions only upon completion of Renko bricks.

### SYS-DEC-002 — Continuous Lower-Timeframe Updates
The system shall update lower-timeframe indicator inputs continuously as new price data is received.

### SYS-DEC-003 — Intrabar Indicator Computation
The system shall compute lower-timeframe indicators without waiting for candle completion.

### SYS-DEC-004 — Context-Only Lower Timeframes
Indicators derived from non-Renko timeframes shall not independently trigger trade entries or exits.

---

## 7. Trade Limits & Execution Control

### SYS-TRD-001 — One Trade per Instrument per Session
The system shall permit at most one completed trade per instrument within a single trading session.

### SYS-TRD-002 — Session Trade Limit Persistence
The system shall enforce the per-session trade limit across restarts and executions.

### SYS-TRD-003 — Market Order Execution
The system shall execute all trade entries and exits using market orders.

### SYS-TRD-004 — Spread Validation
The system shall validate market spread prior to trade execution and shall not trade when the spread exceeds the configured threshold.

### SYS-TRD-005 — Partial Fill Acceptance
The system shall accept partial order fills and shall not retry execution for the unfilled remainder.

---

## 8. Risk & Position Management

### SYS-RSK-001 — Risk-Based Position Sizing
The system shall compute position size based on a configured risk percentage of user-defined equity.

### SYS-RSK-002 — Margin Usage Limit
The system shall enforce a maximum margin usage per trade as a percentage of total equity.

### SYS-RSK-003 — Fixed Daily Equity
The system shall use a fixed equity value per trading day for all risk calculations.

---

## 9. Safety & Failure Handling

### SYS-SAFE-001 — Critical Failure Classification
The system shall classify failures that impact trading safety, data integrity, or execution correctness as critical failures.

### SYS-SAFE-002 — Trading Halt on Critical Failure
Upon detection of a critical failure, the system shall immediately halt all trade entry and exit actions.

### SYS-SAFE-003 — Safe State Enforcement
When trading is halted, the system shall enter a safe state in which no automated trading actions may occur.

### SYS-SAFE-004 — Controlled Recovery
The system shall not resume automated trading after a critical failure without explicit recovery action.

---

## 10. TEST Mode Determinism

### SYS-TEST-001 — Deterministic TEST Behavior
In TEST mode, identical inputs and configuration shall produce identical trading outcomes.

### SYS-TEST-002 — Determinism Scope
Deterministic behavior shall apply to strategy evaluation, order generation, and trade lifecycle management.

### SYS-TEST-003 — Isolation from Non-Determinism
TEST mode behavior shall not depend on wall-clock time, live broker state, or non-deterministic ordering.

---

## 11. Session Reset Semantics

### SYS-SES-005 — Session Boundary Reset Trigger
The system shall treat the end of a trading session as a reset boundary.

### SYS-SES-006 — Mandatory Session State Reset
All session-scoped trading state shall be reset prior to the next session.

### SYS-SES-007 — Non-Session State Preservation
Non-session-scoped state shall be preserved across session boundaries.

### SYS-SES-008 — Restart Consistency
Session reset and preservation semantics shall be enforced consistently across restarts.

---

## 12. Persistence & Recovery

### SYS-REC-001 — Trading State Persistence
The system shall persist all trading-relevant state to allow recovery after restart.

### SYS-REC-002 — Broker Reconciliation
The system shall reconcile persisted trade state with broker-reported positions upon restart.

---

## 13. Logging & Auditability

### SYS-LOG-001 — Trade Decision Logging
The system shall log all trade decisions, executions, exits, and skipped actions with reasons.

---

## 14. Completion Status

This revision represents a **complete, merged, and gap-free System Requirements baseline**.
It is approved for:
- System Architecture derivation
- RTM update
- Software Requirements derivation

---

**End of System Requirements Specification (Rev B)**
