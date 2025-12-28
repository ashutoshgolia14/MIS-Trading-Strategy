
# MIS Algo Trading System
## System Requirements Specification (SY-RS)
### Revision B — Corrected & Gap-Free

---

## 1. Introduction

This document specifies the **System Requirements** for the MIS Algo Trading System.
It defines **system-level behavioral constraints** derived from:
- Stakeholder Requirements (Developer Spec, Strategy Spec)
- REM – Consistency Addendum v3

This revision incorporates all corrections approved during **Phase 13.1.1**.

---

## 2. System Scope

The system shall implement an automated intraday MIS trading system based on Renko price action and multi-timeframe technical indicators, supporting both TEST and PROD execution modes.

---

## 3. Execution Modes

### SY-RS-01 — Execution Mode Separation
The system shall support distinct TEST and PROD execution modes.

---

## 4. Trading Session & Lifecycle

### SY-RS-02 — Intraday Operation
The system shall operate strictly within intraday trading sessions.

### SY-RS-03 — Force-Close Requirement
The system shall ensure that no open positions remain beyond the configured force-close time.

---

## 5. Renko Brick Lifecycle (Corrected)

### SY-RS-NEW-01 — Renko Brick Size Computation Cadence
The system shall compute the Renko brick size once per trading week using the configured computation method.

### SY-RS-NEW-02 — Renko Brick Size Immutability
The system shall ensure that the computed Renko brick size remains unchanged throughout all trading sessions within the same trading week.

### SY-RS-NEW-03 — Renko Brick Size Execution Scope
The system shall apply the same Renko brick size consistently across all executions, restarts, and sessions occurring within the same trading week.

---

## 6. Multi-Timeframe & Decision Semantics (Corrected)

### SY-RS-NEW-04A — Continuous Indicator Data Updates
The system shall update lower-timeframe indicator inputs continuously as new price data is received.

### SY-RS-NEW-04B — Intrabar Indicator Computation
The system shall compute lower-timeframe indicators without waiting for the completion of time-based candles.

### SY-RS-NEW-05A — Renko Decision Timeframe Authority
The system shall restrict trade entry and exit decision authority exclusively to the Renko-based decision timeframe.

### SY-RS-NEW-05B — Context-Only Usage of Lower Timeframes
The system shall not permit indicators derived from non-Renko timeframes to independently trigger trade entry or exit actions.

### SY-RS-NEW-06 — Decision Evaluation Timing
The system shall evaluate trade entry and exit decisions only upon completion of Renko price structures.

---

## 7. Pricing Semantics (Corrected)

### SY-RS-NEW-07 — Primary Price Source Definition
The system shall derive price inputs for Renko construction using the midpoint of the best available bid and ask prices.

### SY-RS-NEW-08 — Price Source Application Scope
The system shall apply the bid-ask midpoint price exclusively for the construction of Renko price structures used in strategy evaluation.

### SY-RS-NEW-09 — Price Source Fallback Behavior
In the absence of valid bid and ask prices, the system shall apply a defined and deterministic fallback price source as configured.

---

## 8. Trade Limits & Session Control (Corrected)

### SY-RS-NEW-10 — Trading Session Definition
The system shall define a trading session as the configured intraday trading window bounded by session start and session end times.

### SY-RS-NEW-11 — Trade Count Limit per Session
The system shall permit at most one completed trade per instrument within a single trading session.

### SY-RS-NEW-12 — Session Trade Limit Persistence
The system shall enforce the per-session trade limit consistently across restarts and executions occurring within the same trading session.

---

## 9. Safety & Failure Handling (Corrected)

### SY-RS-NEW-13 — Critical Failure Classification
The system shall classify failures that may impact trading safety, data integrity, or execution correctness as critical failures.

### SY-RS-NEW-14 — Trading Halt on Critical Failure
Upon detection of a critical failure, the system shall immediately halt all trade entry and exit actions and prevent the placement of any new orders.

### SY-RS-NEW-15 — Safe State Enforcement
When trading is halted due to a critical failure, the system shall enter a safe state in which no automated trading actions may occur.

### SY-RS-NEW-16 — Controlled Recovery Requirement
The system shall not resume automated trading after a critical failure without an explicit recovery action.

---

## 10. TEST Mode Determinism (Corrected)

### SY-RS-NEW-17 — Deterministic Behavior in TEST Mode
When operating in TEST mode, the system shall produce deterministic trading behavior such that identical inputs and configuration result in identical trading decisions and outcomes.

### SY-RS-NEW-18 — Determinism Scope Definition
Deterministic behavior in TEST mode shall apply to strategy evaluation, order generation, and trade lifecycle management.

### SY-RS-NEW-19 — Isolation from Non-Deterministic Influences
In TEST mode, the system shall not depend on wall-clock time, live broker state, or non-deterministic data ordering.

---

## 11. Session Reset Semantics (Corrected)

### SY-RS-NEW-20 — Session Boundary as Reset Trigger
The system shall treat the end of a trading session as a logical boundary at which session-scoped state transitions occur.

### SY-RS-NEW-21 — Mandatory Session State Reset
Upon crossing a trading session boundary, the system shall reset all session-scoped trading state prior to the start of the next session.

### SY-RS-NEW-22 — Preservation of Non-Session State
The system shall preserve non-session-scoped state across trading session boundaries.

### SY-RS-NEW-23 — Session Reset Consistency Across Restarts
The system shall enforce session reset and preservation semantics consistently across restarts and executions.

---

## 12. Conclusion

This revision represents a **complete, gap-free System Requirements baseline** suitable for RTM update, SRS derivation, and audit.

---
