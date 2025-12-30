# DSD Amendment — ADR-001
## Introduction of TradingEngine as Explicit Execution Owner

**Project:** MIS Trading Strategy  
**Baseline:** Frozen Detailed Software Design (Phase 13)  
**Amendment Trigger:** ADR-001  
**Amendment Type:** Controlled Design Evolution  
**Status:** Approved (Pre-Implementation)

---

## 1. Amendment Scope

This amendment updates the **Detailed Software Design (DSD)** to introduce a new architectural component named **TradingEngine**, as mandated by **ADR-001**.

The amendment is **additive and refactoring-only**:
- No functional trading logic is changed
- No strategy rules are altered
- No execution semantics are modified

The objective is to make **execution ownership, policy enforcement, and position lifecycle management explicit, singular, and authoritative**.

---

## 2. New Component: TradingEngine

### 2.1 Responsibility

The **TradingEngine** SHALL be the sole owner of:

- Trading execution sequencing
- Policy enforcement ordering
- Position lifecycle state (ENTER / HOLD / EXIT)
- Invocation of `TradeExecutor`

The TradingEngine SHALL be the **only component** allowed to:
- Call `TradeExecutor.execute(...)`
- Apply `PolicyEvaluator`
- Transition execution-related lifecycle state

---

### 2.2 Explicit Non-Responsibilities

The TradingEngine SHALL NOT:
- Evaluate strategy signals
- Perform indicator calculations
- Perform routing or wiring
- Access infrastructure adapters directly

---

## 3. Updated Component Responsibilities

### 3.1 Application Pipeline (Updated)

The Pipeline is redefined as a **pure orchestration and routing component**.

**Pipeline SHALL:**
- Route events (price ticks, Renko completion)
- Assemble `StrategyContext`
- Forward completed contexts to TradingEngine

**Pipeline SHALL NOT:**
- Track position lifecycle
- Apply policies
- Invoke `TradeExecutor`
- Own execution-related state

---

### 3.2 Execution Layer (Unchanged)

- `TradeExecutor` remains the only execution gateway
- Broker ports and adapters remain unchanged

---

## 4. Updated Control Flow (Textual)

```
Price Tick
  → RenkoBuilder
    → StrategyEvaluator
      → TradingEngine
        → PolicyEvaluator
          → TradeExecutor
```

All execution authority converges at **TradingEngine**.

---

## 5. State Ownership Clarification

| State Type | Owner |
|----------|------|
| Strategy state | Domain (Strategy) |
| Execution lifecycle | TradingEngine |
| Broker position truth | Broker / Infrastructure |
| Orchestration flags | TradingEngine |

---

## 6. Safety & Determinism Impact

- One-decision-per-brick rule preserved
- No retry semantics introduced
- Deterministic execution order enforced
- Recovery logic simplified (single owner)

---

## 7. Traceability

- **ADR:** ADR-001
- **Impacted Phase:** Phase 14.2
- **CAL Impact:** None

---

**End of DSD Amendment**

