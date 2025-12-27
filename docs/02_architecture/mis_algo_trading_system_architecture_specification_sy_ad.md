# MIS Algo Trading System
## System Architecture Specification (SyAD)

**Status:** 🟡 Draft (Formal)  
**Derived From:** System Requirements Specification (SyRS – Revised)  
**Traceability:** Every architecture element traces to ≥1 System Requirement  
**Change Policy:** Modifications allowed until SyAD freeze

---

## 1. Purpose

This document defines the **System Architecture** of the MIS Algo Trading System.

The System Architecture:
- Describes the **structural decomposition** of the system
- Defines **system elements, their responsibilities, and interactions**
- Allocates System Requirements to architectural elements
- Forms the architectural basis for **Software Architecture derivation**

---

## 2. Architectural Scope

This architecture covers:
- The complete trading system as a whole
- Software system boundaries
- External actors and interfaces
- Runtime and lifecycle behavior

This document does **not** define:
- Software module design
- Folder structure
- Programming language or implementation choices

---

## 3. Architectural Drivers

The following System Requirements drive this architecture:

| Driver | System Requirement |
|------|-------------------|
| Deterministic trading | SYS-TRD-001, SYS-TRD-CONC-001 |
| Timing enforcement | SYS-TIM-001 to SYS-TIM-003 |
| Risk control | SYS-RSK-001 to SYS-RSK-003 |
| Recoverability | SYS-REC-001, SYS-REC-002 |
| Renko lifecycle | SYS-RNK-001, SYS-RNK-002 |

---

## 4. System Decomposition (Structural View)

### 4.1 System-Level Elements

The MIS Algo Trading System is decomposed into the following architectural elements:

1. **Trading Decision Subsystem**
2. **Execution & Broker Interface Subsystem**
3. **Market Data Ingestion Subsystem**
4. **Risk & Capital Management Subsystem**
5. **Timing & Session Control Subsystem**
6. **Persistence & Recovery Subsystem**
7. **Monitoring & Logging Subsystem**

---

## 5. Architectural Element Descriptions

### 5.1 Trading Decision Subsystem

**Responsibilities**
- Evaluate trade entry and exit conditions
- Enforce Renko-based decision timing
- Apply multi-timeframe strategy rules

**Allocated System Requirements**
- SYS-TRD-001
- SYS-TRD-002
- SYS-TRD-003
- SYS-TRD-CONC-001

---

### 5.2 Execution & Broker Interface Subsystem

**Responsibilities**
- Submit market orders
- Enforce liquidity and spread constraints
- Handle partial fills

**Allocated System Requirements**
- SYS-EXE-001
- SYS-EXE-002
- SYS-EXE-003

---

### 5.3 Market Data Ingestion Subsystem

**Responsibilities**
- Receive live market data
- Provide price inputs for Renko generation

**Allocated System Requirements**
- SYS-RNK-002

---

### 5.4 Risk & Capital Management Subsystem

**Responsibilities**
- Compute position sizing
- Enforce margin and equity constraints

**Allocated System Requirements**
- SYS-RSK-001
- SYS-RSK-002
- SYS-RSK-003

---

### 5.5 Timing & Session Control Subsystem

**Responsibilities**
- Enforce entry window rules
- Trigger end-of-day force close
- Govern weekly Renko rebuild timing

**Allocated System Requirements**
- SYS-TIM-001
- SYS-TIM-002
- SYS-TIM-003
- SYS-RNK-001

---

### 5.6 Persistence & Recovery Subsystem

**Responsibilities**
- Persist trading state
- Restore state after restart
- Reconcile with broker positions

**Allocated System Requirements**
- SYS-REC-001
- SYS-REC-002

---

### 5.7 Monitoring & Logging Subsystem

**Responsibilities**
- Log trading decisions and actions
- Provide audit trail
- Ensure logs relevant to trading and compliance are durably persisted and available after restart

**Allocated System Requirements**
- SYS-LOG-001

---

## 6. System Interaction View

### 6.1 External Interfaces

| External Actor | Interaction |
|---------------|-------------|
| Broker | Order placement, position queries |
| Market Data Provider | Tick and OHLC data |
| User | Configuration input, monitoring |

---

## 7. Runtime & Lifecycle View

### 7.1 Startup
- Load persisted state
- Reconcile with broker
- Initialize timing controls

### 7.2 Normal Operation
- Continuous market data ingestion
- Renko-based evaluation cycles
- Controlled trade execution

### 7.3 Shutdown & Restart
- Graceful shutdown with state persistence
- Deterministic recovery on restart

---

## 8. System Architecture Constraints

- Deterministic behavior under concurrency
- No trade execution outside timing constraints
- No decision evaluation outside Renko events

---

## 9. Traceability Summary

Every architectural element is explicitly traceable to one or more System Requirements.

No architectural element exists without justification.

---

## 10. Readiness for Software Architecture

This System Architecture:
- Fully satisfies the System Requirements
- Provides a clear basis for Software Architecture derivation
- Introduces no contradiction with the frozen Software Architecture

---

## 11. Next Steps

1. Review and inspect System Architecture
2. Freeze System Architecture (SyAD)
3. Proceed to Software Requirements (SRS)

---

**End of System Architecture Specification**

