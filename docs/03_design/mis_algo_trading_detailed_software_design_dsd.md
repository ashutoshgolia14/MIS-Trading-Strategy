
# MIS Algo Trading System
## Detailed Software Design (DSD)

**Status:** 🔒 Frozen  
**Derived From:**  
- Software Architecture Specification (SW-AD – Rev B, Frozen)  
- Software Requirements Specification (SRS – Rev B, Frozen)  
- System Architecture Specification (SyAD – Frozen)

**Change Policy:**  
Any modification to this document requires formal change control and impact analysis.

---

## 1. Purpose

This document defines the **Detailed Software Design (DSD)** for the MIS Algo Trading System.

The DSD:
- Elaborates the frozen Software Architecture into design-level detail
- Defines modules, responsibilities, data/state ownership, flows, and failure behavior
- Provides an implementation-ready baseline without prescribing code or algorithms

---

## 2. Design Principles

### 2.1 Separation of Concerns
Each module has a single, well-defined responsibility. Strategy logic, timing, risk, execution, and persistence are strictly separated.

### 2.2 Determinism
For identical input sequences, the system shall produce identical outputs, including after restart.

### 2.3 Single Source of Truth
All mutable state has exactly one owning component.

### 2.4 Dependency Direction
Dependencies flow strictly:
Strategy → Runtime → Services → Adapters

### 2.5 Fail-Safe by Default
On any critical failure, trading halts and the system enters a safe state.

---

## 3. Module Decomposition

### 3.1 Strategy Core
- Evaluates Renko-based trade entry/exit
- Applies higher and lower timeframe confirmations
- Produces trade intent only

### 3.2 Renko Engine
- Builds Renko bricks from market data
- Applies deterministic fallback pricing

### 3.3 Symbol Runtime
- Maintains per-symbol execution state
- Serializes decision flow

### 3.4 Scheduler (Time Governance)
- Enforces entry window
- Triggers end-of-day force close

### 3.5 Risk Management
- Computes position sizing
- Enforces margin and equity constraints

### 3.6 Execution Manager
- Submits market orders
- Handles partial fills and broker responses

### 3.7 Persistence Layer
- Persists all trading-relevant state

### 3.8 Recovery Manager
- Restores state on restart
- Reconciles with broker positions

### 3.9 Logging Service
- Records all decisions, executions, and failures

---

## 4. Critical Trading Flow

Market Data → Renko Engine → Strategy Core → Symbol Runtime → Scheduler → Risk Management → Execution Manager → Broker

Each step is gated; rejection at any stage terminates the flow.

---

## 5. Data & State Model

### 5.1 Persisted State
- Symbol runtime state
- Session and timing state
- Risk and equity snapshot
- Execution state

### 5.2 Non-Persisted State
- Strategy evaluation context
- Derived indicators

---

## 6. Error & Failure Handling

### 6.1 Failure Categories
- F1: Data failures
- F2: Decision/runtime failures
- F3: Execution failures
- F4: System/infrastructure failures

### 6.2 Safety Behavior
- Trading halts on critical failure
- System enters safe state
- Recovery required before resumption

---

## 7. Recovery Design

- Load persisted state
- Reconcile with broker
- Restore symbol runtimes
- Resume only from safe boundary

---

## 8. Architectural Decisions (ADR – Summary)

The following design decisions are explicitly recorded to preserve architectural intent:

- Per-symbol runtime **discards stale evaluation contexts** to guarantee deterministic outcomes.
- **Broker-reported positions are authoritative** during recovery and reconciliation.
- **Partial state commits are forbidden** to prevent split-brain recovery scenarios.
- Execution retries are **not permitted** within a single decision cycle to preserve determinism.

---

## 9. Inspection & Freeze

This DSD:
- Is fully aligned with frozen SW-AD and SRS
- Introduces no new behavior
- Is implementation-ready

**DSD Status:** 🔒 Frozen

---

**End of Detailed Software Design**
