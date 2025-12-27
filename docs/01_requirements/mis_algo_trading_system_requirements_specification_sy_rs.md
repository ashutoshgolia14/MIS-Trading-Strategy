# MIS Algo Trading System
## System Requirements Specification (SyRS)

**Status:** 🟡 Revised after Inspection  
**Derived From:** Stakeholder Requirements (Uploaded Project Files)  
**Traceability Mode:** Option A – Explicit stakeholder referencing  
**Change Control:** Via formal inspection only

---

## 1. Purpose

This document defines the **System Requirements** for the MIS Algo Trading System.

System Requirements describe:
- End-to-end **system behavior**
- External interactions and constraints
- Timing, operational, and safety-related behavior

This document is the authoritative basis for:
- System Architecture (SyAD)
- System-level verification and validation

---

## 2. References (Stakeholder Requirements)

The following documents are treated as **authoritative stakeholder requirements**:

- *MIS Multitimeframe RSI MACD Histogram Renko HeikenAshi EMA – Final*
- *Developer Spec – MIS Multi Timeframe Renko HeikenAshi RSI MACD EMA – Final*

---

## 3. System Context

The MIS Algo Trading System is an automated intraday trading system that:
- Trades MIS-enabled equities via a broker
- Uses multi-timeframe technical analysis
- Executes trades based on Renko chart events

External actors:
- Broker system
- Market data provider
- User (configuration & monitoring)

---

## 4. System Boundary Definition

### 4.1 Inside the System

The following capabilities are part of the system:
- Trade signal evaluation and validation
- Timing enforcement (entry window, force close)
- Risk and position sizing computation
- Order decision and submission
- Trading state persistence and recovery

### 4.2 Outside the System

The following are external to the system:
- Exchange matching and settlement
- Broker internal order routing and retries
- Market data source reliability
- UI rendering and client-side behavior

---

## 5. System Requirement Conventions

- All requirements use **“shall”** statements
- Each requirement has a unique `SYS-` identifier
- Requirements are atomic and testable
- Derived requirements are explicitly marked

---

## 6. System Requirements

### 6.1 Trading Decision & Strategy Execution

**SYS-TRD-001**  
The system shall evaluate trade entry and exit decisions only upon completion of a Renko brick.

- Trace: Stakeholder Spec – Renko-based execution

---

**SYS-TRD-002**  
The system shall derive directional bias using higher timeframe Heikin-Ashi charts as defined in the stakeholder strategy (Directional Bias – TF1).

- Trace: Stakeholder Spec – Directional Bias (TF1)

---

**SYS-TRD-003**  
The system shall validate trade entries using multi-timeframe momentum and volatility conditions prior to order placement.

- Trace: Stakeholder Spec – TF2 / TF3 confirmation

---

### 6.2 Timing & Market Session Control

**SYS-TIM-001**  
The system shall allow new trade entries only within the configured intraday entry window.

- Trace: Stakeholder Spec – Entry Window

---

**SYS-TIM-002**  
The system shall prevent initiation of new trades outside the defined entry window regardless of signal validity.

- Trace: Stakeholder Spec – No Late Entries

---

**SYS-TIM-003**  
The system shall forcibly close all open positions at the configured end-of-day force close time.

- Trace: Stakeholder Spec – End-of-Day Close

---

### 6.3 Renko Brick Management

**SYS-RNK-001**  
The system shall compute Renko brick size once per trading week and apply it consistently throughout that week.

- Trace: Stakeholder Spec – Renko Weekly Job

---

**SYS-RNK-002**  
The system shall generate Renko bricks using live market prices derived from bid/ask midpoint data.

- Trace: Developer Spec – Renko Formation Rules

---

### 6.4 Order Execution & Broker Interaction

**SYS-EXE-001**  
The system shall execute all trade entries and exits using market orders.

- Trace: Stakeholder Spec – Liquidity & Order Type

---

**SYS-EXE-002**  
The system shall validate market spread prior to trade execution and shall not trade when the spread exceeds the configured threshold.

- Trace: Stakeholder Spec – Liquidity Check

---

**SYS-EXE-003**  
The system shall accept partial order fills and shall not retry execution for the unfilled remainder.

- Trace: Developer Spec – Partial Fill Handling

---

### 6.5 Risk & Position Management

**SYS-RSK-001**  
The system shall compute position size based on a configured risk percentage of user-defined equity.

- Trace: Stakeholder Spec – Risk Control

---

**SYS-RSK-002**  
The system shall enforce a maximum margin usage per trade as a percentage of total equity.

- Trace: Stakeholder Spec – Margin Cap

---

**SYS-RSK-003**  
The system shall use a fixed equity value per trading day for all risk calculations.

- Trace: Stakeholder Spec – Equity Handling

---

### 6.6 Persistence & Recovery

**SYS-REC-001**  
The system shall persist all trading-relevant state to allow recovery after restart.

- Trace: Developer Spec – Persisted State

---

**SYS-REC-002**  
The system shall reconcile persisted trade state with broker-reported positions upon restart.

- Trace: Developer Spec – Restart Behavior

---

### 6.7 Deterministic Behavior Under Concurrency [DERIVED]

**SYS-TRD-CONC-001 [DERIVED]**  
The system shall ensure deterministic trading behavior under concurrent market events such that duplicate, overlapping, or stale trade actions do not occur.

- Derived from: Concurrency and multi-brick Renko gap analysis

---

### 6.8 Logging & Auditability

**SYS-LOG-001**  
The system shall log all trade decisions, executions, exits, and skipped actions with reasons.

- Trace: Stakeholder Spec – Logging Notes

---

## 7. System Operational Constraints

The following constraints define *when* the system operates but do not describe functional behavior:

- Entry window timing
- End-of-day force close time
- Weekly Renko brick rebuild timing

These constraints are system-level and configurable.

---

## 8. Stakeholder to System Requirement Trace Matrix

| Stakeholder Section | System Requirement IDs |
|--------------------|------------------------|
| Directional Bias – TF1 | SYS-TRD-002 |
| Entry Window | SYS-TIM-001, SYS-TIM-002 |
| End-of-Day Close | SYS-TIM-003 |
| Risk Control | SYS-RSK-001, SYS-RSK-002 |
| Renko Weekly Job | SYS-RNK-001 |
| Liquidity Check | SYS-EXE-002 |

---

## 9. Completion Status

- Inspection findings addressed
- System boundary made explicit
- SYS vs SW concerns resolved
- Ready for System Architecture derivation

---

**End of System Requirements Specification**

