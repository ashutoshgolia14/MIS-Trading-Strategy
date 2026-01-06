---

# MIS Trading Strategy

A modular Python trading system that supports **strategy evaluation, backtesting, and a structured execution pipeline**, with a clear separation between **strategy logic** and **trade execution**.

This repository is under **active development** and currently supports **deterministic backtesting** and a **stubbed live runtime**.

---

## 📌 Project Philosophy

* **TradingEngine is the sole execution authority**
* Strategy evaluation and execution are **strictly separated**
* Execution policies (time, risk, sizing) are enforced **only inside the TradingEngine**
* Pipeline is **transformational**, not decision-making
* Architecture follows a staged V-model with explicit phases

---

## 🧠 High-Level Architecture

```
Market Data
   ↓
Pipeline (Renko + Strategy Evaluation)
   ↓
TradingContext (intent only)
   ↓
TradingEngine (execution authority)
   ↓
Executor → Broker
```

---

## ▶️ How to Run the Code

### Prerequisites

* Python **3.9+**
* No external dependencies beyond the standard library (current state)

---

### 🔹 Backtest Mode (Fully Functional)

Backtest mode reads historical prices from CSV, evaluates strategy logic, executes trades via a test broker, and prints a summary report.

#### Command

```bash
python -m src --mode backtest
```

#### What Happens

* Loads price data from:

  ```
  data/sample_prices.csv
  ```
* Builds Renko bricks
* Evaluates strategy decisions
* Executes trades via `TestBroker`
* Records executions
* Prints a backtest summary to stdout

#### Output Example

```
Backtest Summary
----------------
Ticks processed: <n>
Executions:      <n>
<timestamp> | <status> | <fill_price> | <reason>
```

✔ Deterministic
✔ Repeatable
✔ No external systems required

---

### 🔹 Live Mode (Structurally Correct, Operationally Stubbed)

Live mode uses the same execution pipeline as backtest but is **not connected to real market data**.

#### Command

```bash
python -m src --mode live
```

#### What Happens

* Uses a hardcoded price stream
* Generates timestamps via `datetime.now()`
* Executes trades via `ProdBroker` (placeholder)
* No reporting or persistence

⚠️ **Live trading is NOT production-ready**

---

## 🧩 Implemented Features (Verified)

### ✅ Strategy & Pipeline

* Renko brick construction
* Strategy state evaluation
* Snapshot-based decision tracking
* Deterministic transformation into `TradingContext`

### ✅ Execution Core

* Centralized `TradingEngine`
* Deterministic execution order:

  1. Session policy
  2. Risk validation
  3. Position sizing
  4. Order execution
* Clean executor → broker boundary
* ExecutionResult with status, fill price, and reason

### ✅ Backtesting

* CSV-based historical replay
* Test broker
* Execution recording
* Console reporting

---

## ⚠️ Partially Implemented (By Design)

These components exist structurally but are intentionally minimal:

* **Risk Management**

  * Stateless max-quantity checks only
* **Position Sizing**

  * Fixed quantity only
* **Session Policy**

  * Entry window & force-close evaluation
  * No lifecycle-driven liquidation yet
* **ProdBroker**

  * Placeholder adapter (no real connectivity)

---

## ❌ Not Implemented Yet

These are known gaps and planned work:

* Portfolio-aware risk management
* Force-close liquidation loops
* Trade persistence & recovery
* Structured logging & correlation IDs
* Configuration via files or CLI
* Real-time market data feeds
* Production-grade broker adapters
* Performance metrics & analytics

---

## 🗂 Project Structure

```
src/
├── __main__.py                 # CLI entry point
├── app/
│   ├── backtest/               # Backtesting subsystem
│   ├── wiring/                 # Pipeline & runtime wiring
│   ├── bootstrap.py            # Environment bootstrap (unused)
│   └── env.py                  # Run mode definition
├── domain/                     # Strategy, indicators, Renko
├── execution/                  # TradingEngine & execution logic
├── infrastructure/             # Brokers, logging, persistence
└── common/                     # Shared utilities
```

---

## 🛣 Roadmap (Planned Phases)

### Phase 15.1 — TradingEngine Code Alignment

* Harden execution lifecycle
* Improve internal clarity & invariants

### Phase 15.2 — Policy Enforcement

* Portfolio-aware risk checks
* Proper force-close execution

### Phase 15.3 — Persistence & Recovery

* Execution state storage
* Restart safety

### Phase 15.4 — Observability

* Structured logging
* Execution traceability

---

## ⚠️ Important Notes

* This project is **not yet suitable for real trading**
* Backtesting is the primary supported mode
* Live mode exists to validate execution wiring only

---

## ✅ Status

**Current Phase:** Implementation (Post-Architecture Alignment)
**Backtest:** ✅ Stable
**Live Trading:** ❌ Not production-ready

---