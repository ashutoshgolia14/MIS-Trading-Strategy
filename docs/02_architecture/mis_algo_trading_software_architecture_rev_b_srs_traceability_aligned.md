# MIS Algo Trading System
## Software Architecture (Rev B – SRS Traceability Aligned)

**Status:** 🔒 Frozen (Traceability Aligned Revision)  
**Derived From:**  
- Software Requirements Specification (SRS – Frozen)  
- System Architecture Specification (SyAD – Frozen)

**Revision Note:**  
This revision introduces **explicit Software Requirement (SWR) traceability** only.  
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

These views are documented textually in the sections below.



The software is structured into the following logical layers:

1. **Core Strategy Layer** – pure trading logic
2. **Application / Orchestration Layer** – per-symbol runtime control
3. **Runtime Services Layer** – execution, scheduling, recovery, logging
4. **Adapters Layer** – broker, market data, UI boundaries
5. **Persistence Layer** – state durability

(This structure is unchanged from the originally frozen architecture.)

---

## 3. Architectural Elements & Responsibilities (Logical View)

This section defines the logical decomposition of the software system into architectural elements and their responsibilities.



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

**Realizes Software Requirements**
- SWR-RNK-001 (Renko processing)

---

### 3.3 Symbol Runtime

**Responsibilities**
- Maintain per-symbol execution context
- Ensure deterministic behavior under concurrent market events

**Realizes Software Requirements**
- SWR-TRD-003 (Deterministic trade decision outcomes)

---

### 3.4 Scheduler / Time Governance

**Responsibilities**
- Enforce intraday entry window
- Trigger end-of-day force close

**Realizes Software Requirements**
- SWR-TIM-001 (Entry window enforcement)
- SWR-TIM-002 (End-of-day force close)

---

### 3.5 Execution Manager

**Responsibilities**
- Submit market orders via broker interface
- Enforce spread validation
- Handle partial fills without retry

**Realizes Software Requirements**
- SWR-EXE-001 (Market order execution)
- SWR-EXE-002 (Spread validation)
- SWR-EXE-003 (Partial fill handling)

---

### 3.6 Risk Management Service

**Responsibilities**
- Compute position size based on risk percentage
- Enforce margin usage limits
- Apply fixed equity per trading day

**Realizes Software Requirements**
- SWR-RSK-001 (Risk-based position sizing)
- SWR-RSK-002 (Margin usage limits)
- SWR-RSK-003 (Fixed daily equity)

---

### 3.7 Persistence Layer

**Responsibilities**
- Persist trading-relevant state for restart recovery

**Realizes Software Requirements**
- SWR-REC-001 (State persistence)

---

### 3.8 Recovery Manager

**Responsibilities**
- Reconcile persisted state with broker-reported positions on startup

**Realizes Software Requirements**
- SWR-REC-002 (Recovery & reconciliation)

---

### 3.9 Logging Service

**Responsibilities**
- Log all trading decisions and actions with categorization for audit

**Realizes Software Requirements**
- SWR-LOG-001 (Logging & auditability)

---

## 4. Architecture ↔ Software Requirements Traceability Summary (Justification View)

This section provides explicit justification for each architectural element by mapping it to frozen Software Requirements.



| Architecture Element | Software Requirements |
|---------------------|-----------------------|
| Strategy Core | SWR-TRD-001, SWR-TRD-002, SWR-TRD-004 |
| Renko Engine | SWR-RNK-001 |
| Symbol Runtime | SWR-TRD-003 |
| Scheduler | SWR-TIM-001, SWR-TIM-002 |
| Execution Manager | SWR-EXE-001, SWR-EXE-002, SWR-EXE-003 |
| Risk Management | SWR-RSK-001, SWR-RSK-002, SWR-RSK-003 |
| Persistence Layer | SWR-REC-001 |
| Recovery Manager | SWR-REC-002 |
| Logging Service | SWR-LOG-001 |

---

## 5. Architectural Constraints (Constraint View)

The following constraints govern all software design and implementation activities.



- No strategy logic outside Strategy Core
- No broker interaction outside Execution Manager
- Per-symbol runtime isolation is mandatory
- All external interactions occur via adapters

---

## 6. Architectural Decisions (ADR – Summary)

The following key architectural decisions were taken and are considered frozen:

- Renko-brick–driven evaluation is the sole trigger for trade decisions
- Per-symbol runtime isolation is mandatory
- Broker interaction is centralized via the Execution Manager
- Architecture is layered with strict dependency direction

These decisions are justified by the frozen System and Software Requirements.

---

## 7. Freeze Declaration

This Software Architecture revision:
- Is fully aligned with frozen SRS and SyAD
- Introduces no new behavior or structure
- Is **FINAL and FROZEN**

Any future changes require formal change control.

---

**End of Software Architecture (Rev B)**

