
# MIS Algo Trading System
## Software Architecture (Rev C – Trading Engine)
**Revision**: Rev C
**Change Trigger**: ADR-001 — Introduce TradingEngine as Explicit Execution Owner
**Status:** 🟡 Revised after Architecture Review  
**Derived From:**  
- Software Requirements Specification (SRS – Frozen)  
- System Architecture Specification (SyAD – Frozen)

**Revision Note:**  
This revision introduces **explicit Software Requirement (SWR) traceability and interface clarity** only.  
No architectural structure, responsibility, or layering has been modified.

---

## 1. Purpose

This document defines the **Software Architecture** of the MIS Algo Trading System and provides
explicit traceability between architectural elements and frozen **Software Requirements (SRS)**.

The architecture:
- Realizes all frozen Software Requirements
- Enforces separation of concerns
- Provides a stable basis for implementation and testing

---

## 2. Architectural Overview

### 2.1 Architectural Views (ISO/IEC 42010)

This Software Architecture is described using the following standard views:

- **Logical View** – decomposition of software into logical components and responsibilities
- **Runtime View** – interaction of components during normal operation
- **Constraint View** – rules and constraints governing architecture usage

The software is structured into the following logical layers:

1. **Core Strategy Layer** – pure trading logic
2. **Application / Orchestration Layer** – per-symbol runtime control
3. **Runtime Services Layer** – execution, scheduling, recovery, logging
4. **Adapters Layer** – broker, market data, UI boundaries
5. **Persistence Layer** – state durability

(This structure is unchanged from the originally frozen architecture.)

---

## 3. Architectural Elements & Responsibilities (Logical View)

### 3.1 Strategy Core

**Responsibilities**
- Evaluate Renko-based trade entry and exit logic
- Apply higher-timeframe directional bias
- Apply lower-timeframe momentum and volatility confirmation

**Realizes Software Requirements**
- SWR-TRD-001 (Renko-only evaluation)
- SWR-TRD-002 (Higher-timeframe directional bias)
- SWR-TRD-004 (Lower-timeframe confirmation)

---

### 3.2 Renko Engine

**Responsibilities**
- Generate Renko bricks from live market prices using configured brick size
- Apply deterministic fallback price source when bid/ask data is unavailable

**Realizes Software Requirements**
- SWR-RNK-001 (Renko processing)
- SWR-RNK-002 (Deterministic fallback price source)

---

### 3.3 Symbol Runtime

**Responsibilities**
- Maintain per-symbol execution context
- Ensure deterministic behavior under concurrent market events

**Realizes Software Requirements**
- SWR-TRD-003 (Deterministic trade decision outcomes)

---

#### 3.3.1 Application Pipeline
The Application Pipeline is a conceptual orchestration model that is executed at runtime by the per-symbol Symbol Runtime component.

**Responsibilities**
- Event routing
- Context assembly

**Explicit Non-Responsibilities**
- Execution control
- Policy enforcement
- Position lifecycle management

---

### 3.5 Scheduler / Time Governance

**Responsibilities**
- Enforce intraday entry window
- Trigger end-of-day force close

**Realizes Software Requirements**
- SWR-TIM-001 (Entry window enforcement)
- SWR-TIM-002 (End-of-day force close)

---

### 3.6 TradingEngine (Execution Control Layer)

**Responsibilities**
- Own execution lifecycle (ENTER / HOLD / EXIT)
- Enforce policy evaluation ordering
- Invoke execution services

**Non-Responsibilities**
- Strategy evaluation
- Indicator computation
- Routing or wiring

### 3.7 Execution Manager

**Responsibilities**
- Submit market orders via broker interface
- Enforce spread validation
- Handle partial fills without retry

**Realizes Software Requirements**
- SWR-EXE-001 (Market order execution)
- SWR-EXE-002 (Spread validation)
- SWR-EXE-003 (Partial fill handling)

---

### 3.8 Risk Management Service

**Responsibilities**
- Compute position size based on risk percentage
- Enforce margin usage limits
- Apply fixed equity per trading day

**Realizes Software Requirements**
- SWR-RSK-001 (Risk-based position sizing)
- SWR-RSK-002 (Margin usage limits)
- SWR-RSK-003 (Fixed daily equity)

---

### 3.9 Persistence Layer

**Responsibilities**
- Persist trading-relevant state for restart recovery

**Realizes Software Requirements**
- SWR-REC-001 (State persistence)

---

### 3.10 Recovery Manager

**Responsibilities**
- Reconcile persisted state with broker-reported positions on startup

**Realizes Software Requirements**
- SWR-REC-002 (Recovery & reconciliation)

---

### 3.11 Logging Service

**Responsibilities**
- Log all trading decisions and actions with categorization for audit

**Realizes Software Requirements**
- SWR-LOG-001 (Logging & auditability)

---

## 4. Software Interface View

This section defines the **logical interfaces** between software architectural elements.
Interfaces describe responsibility boundaries and interaction intent only.

| Provider | Consumer | Purpose |
|--------|----------|---------|
| Market Data Adapter | Renko Engine | Provide normalized price inputs |
| Renko Engine | Strategy Core | Emit completed Renko brick events |
| Strategy Core | Symbol Runtime | Trade decision intent |
| Symbol Runtime | TradingEngine | Evaluated strategy context |
| TradingEngine | Scheduler | Timing policy evaluation |
| TradingEngine | Risk Management Service | Position sizing and risk validation |
| TradingEngine | Execution Manager | Authorized order execution |
| Execution Manager | Broker Adapter | Order submission |
| Persistence Layer | Stateful Components | State persistence |
| Logging Service | All Components | Audit logging |


The Execution Manager does not act until TradingEngine has coordinated scheduler and risk decisions.

---
 
### 4.3 Event Ingress Modes
The system supports multiple event ingress modes:
- **Live Mode** — events sourced from real-time market data adapters
- **Backtest Mode** — events sourced from historical data feeds
- **Replay Mode** — events sourced from recorded execution traces

All ingress modes SHALL converge at the same orchestration boundary
and SHALL be subject to identical architectural constraints.

---

## 5. Architectural Constraints (Constraint View)

- No strategy logic outside Strategy Core
- No broker interaction outside Execution Manager
- Per-symbol runtime isolation is mandatory
- All external interactions occur via adapters
- Only TradingEngine may invoke Execution Manager
- Execution policies SHALL NOT be enforced outside TradingEngine
- Scheduler and Risk Management influence execution authorization but do not directly invoke execution.


---

## 6. Architectural Decisions (ADR – Summary)

- Renko-brick–driven evaluation is the sole trigger for trade decisions
- Per-symbol runtime isolation is mandatory
- Broker interaction is centralized via the Execution Manager
- Architecture is layered with strict dependency direction
- ADR-001: Execution ownership centralized in TradingEngine


---

## 7. Freeze Declaration

This Software Architecture revision:
- Is fully aligned with frozen SRS and SyAD
- Introduces no new behavior or structure
- Is **FINAL and READY FOR FREEZE** upon approval

Any future changes require formal change control.

---

**End of Software Architecture (Rev B)**