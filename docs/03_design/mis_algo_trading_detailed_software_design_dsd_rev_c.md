# MIS Algo Trading — Detailed Software Design (DSD)

**Revision:** Rev C  
**Supersedes:** Rev B  
**Change Trigger:** ADR-001 — Introduce TradingEngine as Explicit Execution Owner  
**Status:** Active (Authoritative)

---

## 1. Purpose

This document defines the **Detailed Software Design (DSD)** for the MIS Algo Trading System.

Revision C introduces the **TradingEngine** component to make execution ownership, policy enforcement, and position lifecycle management **explicit, singular, and authoritative**.

---

## 2. Design Principles

- Deterministic behavior for identical input sequences
- One-decision-per-Renko-brick
- No partial state commits
- No execution retries
- Explicit ownership of all mutable state
- Broker-reported positions are authoritative on recovery

---

## 3. Core Components

### 3.1 Renko Engine
- Builds completed Renko bricks deterministically
- Emits at most one brick per evaluation
- Contains no strategy or execution logic

### 3.2 Strategy Domain
- Evaluates trading bias and signals
- Maintains a deterministic state machine
- Produces **trade intent only**
- Has no execution authority

---

## 4. TradingEngine (Execution Authority)

### 4.1 Role

The **TradingEngine** is the **sole execution authority** in the system.

It is the only component allowed to:
- Enforce execution policies
- Manage position lifecycle (ENTER / HOLD / EXIT)
- Invoke the execution layer

### 4.2 Responsibilities

The TradingEngine SHALL:
- Receive evaluated strategy intent
- Apply policy evaluation deterministically
- Maintain execution lifecycle state
- Invoke `TradeExecutor` at most once per decision cycle

### 4.3 Non-Responsibilities

The TradingEngine SHALL NOT:
- Evaluate strategy logic
- Compute indicators
- Perform routing or wiring
- Access broker adapters directly

---

## 5. Application Pipeline

The Application Pipeline is a **pure orchestration and routing component**.

### Pipeline SHALL:
- Route price ticks and Renko completion events
- Assemble `StrategyContext`
- Forward completed contexts to TradingEngine

### Pipeline SHALL NOT:
- Track position lifecycle
- Enforce policies
- Invoke TradeExecutor
- Own execution-related state

---

## 6. Execution Layer

### 6.1 TradeExecutor
- Executes broker-level orders
- Accepts execution intent only
- Contains no strategy or policy logic

### 6.2 Broker Adapters
- Implement broker ports
- Infrastructure-only
- No business logic

---

## 7. Runtime Control Flow

Price Tick  
→ Renko Engine  
→ Strategy Domain  
→ Application Pipeline  
→ TradingEngine  
→ Policy Evaluation  
→ TradeExecutor  
→ Broker Adapter

---

## 8. State Ownership

| State Category | Owner |
|---------------|------|
| Strategy state | Strategy Domain |
| Execution lifecycle | TradingEngine |
| Policy evaluation | TradingEngine |
| Broker position truth | Broker |
| Routing / orchestration | Pipeline |

---

## 9. Safety & Determinism Guarantees

- One-decision-per-brick enforced
- No retries
- Centralized execution authority
- Deterministic execution ordering
- Simplified recovery via single execution owner

---

## 10. Traceability

- **ADR:** ADR-001
- **SW-AD:** Rev C
- **Phase:** 14.2+

---

**End of Detailed Software Design (Rev C)**
