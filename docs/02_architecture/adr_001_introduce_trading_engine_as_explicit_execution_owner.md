# ADR-001: Introduce TradingEngine as Explicit Execution Owner

**Project:** MIS Trading Strategy  
**Phase:** 14 (Pre-Implementation)  
**Status:** Proposed  
**Date:** 2025-01-XX  
**Decision Type:** Architectural Design Record (ADR)

---

## 1. Context

During Phase 14.1A inspection and CAL sign-off, a design discussion resurfaced regarding **execution ownership and orchestration responsibilities** in the current architecture.

The current design uses the **Application Pipeline** as the top-level orchestrator that:
- Routes events (price ticks → Renko completion)
- Invokes strategy evaluation
- Applies policy gating
- Coordinates execution via `TradeExecutor`
- Tracks limited session-level state (e.g. `_position_open`, `_ever_entered`)

While this design is **DSD-aligned and correct**, concerns were raised about **implicit execution ownership** being partially embedded in the Pipeline, which may limit long-term evolvability and clarity.

---

## 2. Problem Statement

Without an explicit **TradingEngine** abstraction, the system risks:

- Implicit execution ownership spread across Pipeline logic
- Policy enforcement being orchestrated rather than owned
- Position lifecycle state being managed indirectly
- Increased risk of duplicated or inconsistent execution logic as the system evolves

These risks are **not defects today**, but represent **future architectural fragility**.

---

## 3. Decision Drivers

The decision is driven by the need to:

- Make execution ownership **explicit, singular, and authoritative**
- Centralize policy enforcement and execution sequencing
- Clearly separate **routing/orchestration** from **trading control**
- Improve restart, recovery, and lifecycle invariants
- Enable safer long-term evolution without hidden coupling

---

## 4. Options Considered

### Option A — Retain Current Design (Pipeline-Centric Orchestration)

**Description**  
Pipeline remains the coordinator that invokes strategy, policy, and execution components.

**Pros**
- No design changes required
- Fully aligned with frozen DSD
- Minimal refactoring

**Cons**
- Execution ownership remains implicit
- Pipeline carries session lifecycle knowledge
- Harder to reason about invariants as features grow

---

### Option B — Introduce TradingEngine (Explicit Execution Owner)

**Description**  
Introduce a `TradingEngine` component that:
- Owns position lifecycle
- Owns policy enforcement order
- Owns execution sequencing
- Exposes a single, explicit entry point (e.g. `on_event(...)`)

Pipeline becomes a **pure router**, delegating all trading control to TradingEngine.

**Pros**
- Explicit execution authority
- Single place for lifecycle invariants
- Cleaner separation of concerns
- Stronger safety and auditability

**Cons**
- Requires architectural update
- Requires DSD and SW-AD amendments
- Slight upfront complexity

---

## 5. Decision

**Decision:** **Option B — Introduce TradingEngine**

The system will introduce a **TradingEngine** abstraction to act as the **sole owner of trading execution, policy enforcement, and position lifecycle management**.

This is a **design evolution**, not a corrective fix.

---

## 6. Consequences

### Positive
- Execution ownership becomes explicit and enforceable
- Pipeline simplifies to routing and wiring only
- Clear lifecycle invariants (enter, hold, exit)
- Easier restart and recovery semantics
- Reduced risk of future architectural drift

### Negative
- Requires controlled design updates
- Requires careful refactoring
- Slightly increased initial complexity

---

## 7. Impacted Artifacts

The following artifacts will require controlled updates:

- Detailed Software Design (DSD)
- Software Architecture Document (SW-AD)
- Application wiring diagrams
- Phase 14.2 implementation plan

No CAL items are affected.

---

## 8. Implementation Guidance (Non-Normative)

- `TradingEngine` SHALL be the only component allowed to:
  - Invoke `TradeExecutor`
  - Apply `PolicyEvaluator`
  - Manage position lifecycle flags
- Pipeline SHALL:
  - Forward events
  - Perform no trading decisions
  - Perform no execution gating

---

## 9. Status & Next Steps

- ADR accepted
- Proceed to update DSD & SW-AD before Phase 14.2 coding
- Implement TradingEngine as first task in Phase 14.2

---

**End of ADR-001**

