
# MIS Algo Trading System
## Software Requirements Specification (SRS)

**Status:** 🟡 Draft (Formal)  
**Derived From:**  
- System Requirements Specification (SyRS – Frozen)  
- System Architecture Specification (SyAD – Frozen)  

**Traceability Rule:** Every Software Requirement (SWR) shall trace to ≥1 System Requirement (SYS).  
**Change Policy:** Modifications allowed until SRS inspection & freeze.

---

## 1. Purpose

This document defines the **Software Requirements** for the MIS Algo Trading System.

Software Requirements:
- Specify **what the software shall do**
- Are derived strictly from **System Requirements and System Architecture**
- Do **not** prescribe software architecture or implementation design

This document forms the basis for:
- Software Architecture validation
- Software-level testing
- Integration and verification planning

---

## 2. References

- System Requirements Specification (SyRS – Revised, Frozen)
- System Architecture Specification (SyAD – Frozen)
- Stakeholder Requirements (Uploaded project files – reference only)

---

## 3. Software Scope & Boundary

### 3.1 Software In Scope

The software includes:
- Strategy evaluation logic
- Renko processing logic
- Timing and session enforcement logic
- Risk and position sizing logic
- Broker interaction logic
- Persistence and recovery logic
- Logging and monitoring logic

### 3.2 Out of Scope

The software does not include:
- Exchange matching
- Broker internal routing
- Market data source reliability
- UI rendering

---

## 4. Software Requirement Conventions

- All requirements use **"shall"** statements
- Software Requirements IDs use prefix `SWR-`
- Requirements are **atomic and testable**
- Traceability to System Requirements is mandatory

---

## 5. Software Requirements

### 5.1 Strategy Evaluation & Trading Logic

**SWR-TRD-001**  
The software shall evaluate trade entry and exit logic only when a Renko brick is completed.

- Trace: SYS-DEC-001

---

**SWR-TRD-002**  
The software shall compute and apply higher-timeframe directional bias logic as defined by the system strategy.

- Trace: SYS-DEC-002

---

**SWR-TRD-004**  
The software shall compute and apply lower-timeframe momentum and volatility confirmation logic prior to trade entry.

- Trace: SYS-DEC-004

---

**SWR-TRD-003**  
The software shall ensure deterministic trade decision outcomes when multiple Renko bricks are generated in rapid succession.

- Trace: SYS-TEST-001, SYS-TEST-003

---

### 5.2 Timing & Session Control

**SWR-TIM-001**  
The software shall enforce the configured intraday entry window for trade initiation.

- Trace: SYS-SES-002, SYS-SES-003

---

**SWR-TIM-002**  
The software shall trigger forced position closure at the configured end-of-day force close time.

- Trace: SYS-SES-004

---

### 5.3 Renko Processing

**SWR-RNK-001**  
The software shall calculate Renko bricks using the configured brick size and live market price inputs.

- Trace: SYS-RNK-001, SYS-RNK-002, SYS-RNK-004

---

**SWR-RNK-002**  
The software shall apply a deterministic fallback price source for Renko brick construction when valid bid/ask data is unavailable.

- Trace: SYS-RNK-005

---

### 5.4 Order Execution & Broker Interaction

**SWR-EXE-001**  
The software shall place market orders for trade entry and exit via the broker interface.

- Trace: SYS-TRD-003

---

**SWR-EXE-002**  
The software shall validate spread constraints prior to order placement.

- Trace: SYS-TRD-004

---

**SWR-EXE-003**  
The software shall accept partial order fills and shall not retry unfilled quantities.

- Trace: SYS-TRD-005

---

### 5.5 Risk & Position Management

**SWR-RSK-001**  
The software shall compute position size based on configured risk percentage and user-defined equity.

- Trace: SYS-RSK-001

---

**SWR-RSK-002**  
The software shall enforce margin usage limits per trade.

- Trace: SYS-RSK-002

---

**SWR-RSK-003**  
The software shall apply a fixed equity value for all risk calculations during a trading day.

- Trace: SYS-RSK-003

---

### 5.6 Persistence & Recovery

**SWR-REC-001**  
The software shall persist all trading-relevant state required to resume operation after restart.

- Trace: SYS-REC-001

---

**SWR-REC-002**  
The software shall reconcile persisted state with broker-reported positions during startup.

- Trace: SYS-REC-002

---

### 5.7 Logging & Monitoring

**SWR-LOG-001**  
The software shall log all trade decisions, executions, exits, and skipped actions with timestamps, reasons, and log categories suitable for filtering and audit.

- Trace: SYS-LOG-001

---

## 6. Traceability Summary

All Software Requirements are traceable to one or more System Requirements.

No software requirement exists without system-level justification.

---

## 7. Next Steps

1. Review Software Requirements (SRS)
2. Create Software Requirements Inspection Baseline
3. Perform SRS inspection
4. Freeze SRS
5. Validate frozen Software Architecture against SRS

---

**End of Software Requirements Specification**
