# MIS Algo Trading System
## Detailed Software Design (DSD)

**Revision:** Rev C  
**Supersedes:** Rev B  
**Change Trigger:** ADR-001 — Introduce TradingEngine as Explicit Execution Owner  
**Status:** 🔒 Active (Authoritative)

**Derived From:**  
- Software Architecture Specification (SW-AD – Rev C)  
- Software Requirements Specification (SRS – Frozen)  
- System Architecture Specification (SyAD – Frozen)

---

## 1. Purpose

This document defines the **Detailed Software Design (DSD)** for the MIS Algo Trading System.

Revision C introduces the **TradingEngine** to make execution ownership, policy enforcement, and position lifecycle management explicit and singular.

---

## 2. Design Principles

- Determinism for identical input sequences
- One-decision-per-Renko-brick
- Single source of truth for mutable state
- Explicit execution ownership
- Fail-safe behavior by default

---

## 3. Module Decomposition

### 3.1 Strategy Core
- Evaluates Renko-based trade entry/exit
- Applies higher and lower timeframe confirmations
- Produces trade intent only

---

### 3.2 Renko Engine
- Builds Renko bricks deterministically
- Emits at most one brick per evaluation

---

### 3.3 Application Pipeline

**Responsibilities**
- Event routing
- Context assembly

**Explicit Non-Responsibilities**
- Execution control
- Policy enforcement
- Position lifecycle management

---

### 3.4 TradingEngine (**NEW**)

**Responsibilities**
- Own execution lifecycle (ENTER / HOLD / EXIT)
- Enforce policy evaluation ordering
- Invoke execution services

**Non-Responsibilities**
- Strategy evaluation
- Indicator computation
- Routing or wiring

---

### 3.5 Scheduler (Time Governance)
- Enforces entry window
- Triggers end-of-day force close

---

### 3.6 Risk Management
- Computes position sizing
- Enforces margin and equity constraints

---

### 3.7 Execution Manager
- Submits market orders
- Handles partial fills without retry

---

### 3.8 Persistence Layer
- Persists trading-relevant state atomically

---

### 3.9 Recovery Manager
- Restores state on restart
- Reconciles with broker positions

---

### 3.10 Logging Service
- Logs all decisions, executions, and failures

---

## 4. Critical Trading Flow

Market Data → Renko Engine → Strategy Core → Application Pipeline → TradingEngine → Scheduler → Risk Management → Execution Manager → Broker

---

## 5. State Ownership

| State Category | Owner |
|---------------|-------|
| Strategy state | Strategy Core |
| Execution lifecycle | TradingEngine |
| Policy evaluation | TradingEngine |
| Broker position truth | Broker |
| Routing/orchestration | Pipeline |

---

## 6. Error & Failure Handling

- Trading halts on critical failure
- System enters safe state
- Recovery required before resumption

---

## 7. Recovery Design

- Load persisted state
- Reconcile with broker-reported positions
- Resume only from safe boundary

---

## 8. Architectural Decisions (ADR – Summary)

- Renko-brick completion is the sole decision trigger
- Execution ownership is centralized in TradingEngine (ADR-001)
- Broker-reported positions are authoritative
- Partial state commits are forbidden
- Execution retries are not permitted

---

## 9. Inspection & Status

This DSD:
- Is aligned with SW-AD Rev C and frozen SRS
- Is implementation-ready

**DSD Status:** 🔒 Active

---

**End of Detailed Software Design (Rev C)**