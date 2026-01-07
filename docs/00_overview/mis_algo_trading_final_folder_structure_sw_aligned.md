# MIS Algo Trading – Final Software-Aligned Folder Structure

## Purpose

This document defines the **authoritative, software-aligned folder structure**
for the MIS Algo Trading project.

This structure was finalized during **Phase 11** to introduce a `src/`-based
layout while preserving existing system behavior and compilation correctness.

All future development phases must conform to this structure unless explicitly
approved through a formal phase change.

---

## Top-Level Project Structure

```
MIS-Trading-Strategy/
├── README.md
├── config/
│   └── config.yaml
├── docs/
│   └── (process and design documentation)
├── tests/
│   └── (unit, integration, functional, system tests)
├── src/
│   └── (all application source code)
```

### Key Rules
- **All executable source code resides under `src/`**
- The project root contains **no business logic**
- Execution is performed using:
  ```bash
  python -m src
src/ – Application Source Tree
```
src/
├── __init__.py
├── __main__.py
│
├── app/
│   ├── bootstrap.py
│   ├── env.py
│   ├── backtest/
│   │   ├── data_loader.py
│   │   ├── recorder.py
│   │   ├── report.py
│   │   └── runner.py
│   └── wiring/
│       ├── context_builder.py
│       ├── pipeline.py
│       └── runtime.py
│
├── domain/
│   ├── indicators/
│   │   ├── calculators.py
│   │   └── models.py
│   ├── renko/
│   │   ├── builder.py
│   │   └── models.py
│   ├── strategy/
│   │   ├── evaluator.py
│   │   ├── flags.py
│   │   ├── models.py
│   │   ├── state.py
│   │   ├── bias.py
│   │   └── context.py
│   └── timeframe/
│       └── timeframe.py
│
├── execution/
│   ├── executor.py
│   ├── models.py
│   ├── ports.py
│   ├── risk.py
│   ├── sizing.py
│   └── policy/
│       ├── evaluator.py
│       ├── force_close.py
│       ├── models.py
│       └── session.py
│
├── infrastructure/
│   ├── adapters/
│   │   └── broker/
│   │       ├── base.py
│   │       ├── prod_broker.py
│   │       └── test_broker.py
│   ├── config/
│   │   ├── errors.py
│   │   ├── loader.py
│   │   └── schema.py
│   ├── logging/
│   │   └── logger.py
│   └── persistence/
│       └── state_store.py
│
├── common/
│   └── decimal.py
│
└── data/
    └── sample_prices.csv
```

### Architectural Intent by Layer
|Layer | Responsibility |
|------|----------------|
|app/ | Application orchestration and runtime wiring |
|domain/ | Pure business and trading logic |
|execution/ | Order execution, risk, sizing, policies |
|infrastructure/ | External systems, IO, brokers, config |
|common/ | Shared utilities |
|data/ | Runtime input data |

### Change Control
Changes to this structure **MUST**:
- be approved via a documented Phase Change
- include a change rationale, date, and scope impact
- update this file and the phase history artifact

---
