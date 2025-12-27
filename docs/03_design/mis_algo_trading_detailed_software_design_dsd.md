# MIS Algo Trading System
## Detailed Software Design (DSD)

**Status:** 🟡 Draft (Formal)  
**Derived From:**  
- Software Architecture (Rev B – Frozen, Traceability Aligned)  
- Software Requirements Specification (SRS – Frozen)

**Design Rule:** This document refines *how* the software fulfills frozen requirements, without changing architecture or scope.

---

## 1. Purpose

This document defines the **Detailed Software Design (DSD)** for the MIS Algo Trading System.

The DSD:
- Translates Software Architecture into **design-level components**
- Defines **interfaces, data models, and control flows**
- Provides a blueprint for implementation and unit testing

---

## 2. Design Principles

1. **Strict traceability** – every design element traces to SRS
2. **Single responsibility** – one concern per component
3. **Deterministic execution** – no race-dependent behavior
4. **Fail-safe defaults** – safety over aggressiveness
5. **Immutability where possible** – especially for snapshots

---

## 3. High-Level Component Interaction (Runtime Flow)

**Normal Trading Cycle (per symbol):**

1. Market Data Adapter receives tick
2. Renko Engine updates bricks
3. On brick completion → Symbol Runtime notified
4. Scheduler validates timing constraints
5. Strategy Core evaluates entry/exit
6. Risk Manager computes quantity
7. Execution Manager places order
8. Persistence Layer stores state
9. Logging Service records event

---

## 4. Component-Level Design

### 4.1 Strategy Core

**Responsibilities**
- Pure evaluation of trading logic
- No side effects

**Key Interfaces**
- `evaluate(snapshot: StrategySnapshot) -> TradeDecision`

**Design Notes**
- Stateless between calls
- Uses immutable snapshot objects

**Traces to:** SWR-TRD-001, SWR-TRD-002, SWR-TRD-004

---

### 4.2 Renko Engine

**Responsibilities**
- Convert ticks into Renko bricks

**Key Interfaces**
- `on_tick(price: float) -> Optional[RenkoBrick]`

**Design Notes**
- Brick size injected at startup
- Supports multi-brick formation

**Traces to:** SWR-RNK-001

---

### 4.3 Symbol Runtime

**Responsibilities**
- Orchestrate per-symbol lifecycle
- Enforce deterministic behavior under concurrent market events

**Key Interfaces**
- `on_renko_event(brick: RenkoBrick)`

**Design Notes**
- Single-threaded per symbol
- Latest snapshot wins; all older pending snapshots are explicitly discarded

**Traces to:** SWR-TRD-003

---

### 4.4 Scheduler / Time Governance

**Responsibilities**
- Validate entry window
- Trigger force close

**Key Interfaces**
- `is_entry_allowed(time) -> bool`
- `should_force_close(time) -> bool`

**Design Notes**
- Time-zone aware

**Traces to:** SWR-TIM-001, SWR-TIM-002

---

### 4.5 Execution Manager

**Responsibilities**
- Translate decisions into broker orders

**Key Interfaces**
- `execute(decision: TradeDecision, qty: int) -> ExecutionResult`

**Design Notes**
- Single execution authority
- Spread check before order
- Returned execution result is used for logging and test verification

**Traces to:** SWR-EXE-001, SWR-EXE-002, SWR-EXE-003

---

### 4.6 Risk Management Service

**Responsibilities**
- Compute position size

**Key Interfaces**
- `calculate_qty(equity, stop_distance) -> int`

**Design Notes**
- Uses fixed daily equity snapshot

**Traces to:** SWR-RSK-001, SWR-RSK-002, SWR-RSK-003

---

### 4.7 Persistence Layer

**Responsibilities**
- Persist trading state atomically

**Key Interfaces**
- `save(state: SymbolState)`
- `load(symbol) -> SymbolState`

**Design Notes**
- Atomic per-symbol writes

**Traces to:** SWR-REC-001

---

### 4.8 Recovery Manager

**Responsibilities**
- Restore and reconcile state on startup

**Key Interfaces**
- `recover(symbol) -> SymbolState`

**Design Notes**
- Broker is source of truth for open positions

**Traces to:** SWR-REC-002

---

### 4.9 Logging Service

**Responsibilities**
- Structured logging of events

**Key Interfaces**
- `log(event_type, payload)`

**Design Notes**
- Log categories mapped to SWRs

**Traces to:** SWR-LOG-001

---

## 5. Core Data Models

### 5.1 StrategySnapshot
- Renko state
- Indicator values
- Time context

### 5.2 TradeDecision
- Action (ENTER / EXIT / HOLD)
- Reason code

### 5.3 SymbolState
- Open position
- Last decision
- Persisted flags

---

## 6. Error Handling & Recovery

- All external failures are contained
- No partial state updates
- Safe retry only at orchestration level

---

## 7. Unit Test Mapping (Preview)

| Component | SWR Coverage |
|---------|--------------|
| Strategy Core | SWR-TRD-* |
| Renko Engine | SWR-RNK-001 |
| Scheduler | SWR-TIM-* |
| Execution Manager | SWR-EXE-* |
| Risk Manager | SWR-RSK-* |
| Persistence | SWR-REC-001 |
| Recovery | SWR-REC-002 |
| Logging | SWR-LOG-001 |

---

## 8. Next Steps

1. Review Detailed Software Design
2. Inspect & freeze DSD
3. Define unit test specifications
4. Begin implementation

---

**End of Detailed Software Design**

