# MIS Algo Trading System
## Final Folder Structure (Aligned with Phase-10 Frozen Code + V-Model)

**Status:** 🟢 Updated & Code-Aligned  
**Baseline:** Phase-10 Frozen Code (Authoritative)  
**Traceability:** V-Model (StRS, SyRS, SRS, SW Arch, DSD, UTS – Frozen)

---

## 1. Alignment Statement

This document **supersedes the earlier folder-structure draft** and is now:
- **Derived directly from the Phase-10 frozen codebase**
- **Verified against architectural intent from SW Arch & DSD**
- Considered the **new authoritative folder-structure reference**

No assumptions were made beyond what exists in code.

---

## 2. Top-Level Repository Structure (As‑Is)

```
mis_algo_trading/
│
├── app/                    # Application layer & orchestration
├── domain/                 # Pure domain logic (strategy, renko, indicators)
├── execution/              # Execution, risk, sizing, policies
├── infrastructure/         # External adapters & technical services
├── common/                 # Shared low‑level utilities
├── data/                   # Test / sample data
├── config.yaml             # Default configuration entry point
└── README.md               # Usage & bootstrap notes
```

---

## 3. Application Layer (`app/`)

**Responsibility:**
- System startup
- Environment selection (test / prod)
- Wiring domain + execution + infrastructure
- Backtest runners

```
app/
├── main.py                 # Application entry point
├── env.py                  # Environment resolution (test / prod)
├── bootstrap.py            # System bootstrap & initialization
│
├── config/                 # App‑level config loaders
│
├── wiring/                 # Dependency wiring & pipelines
│   ├── pipeline.py         # Tick → strategy → execution pipeline
│   ├── runtime.py          # Runtime coordination
│   └── context_builder.py  # Object graph construction
│
└── backtest/               # Backtesting application flow
    ├── data_loader.py
    ├── recorder.py
    └── report.py
```

---

## 4. Domain Layer (`domain/`)

```
domain/
├── strategy/
├── renko/
├── indicators/
└── timeframe/
```

---

## 5. Execution Layer (`execution/`)

```
execution/
├── executor.py
├── ports.py
├── models.py
├── risk.py
├── sizing.py
└── policy/
```

---

## 6. Infrastructure Layer (`infrastructure/`)

```
infrastructure/
├── adapters/
├── persistence/
├── logging/
└── config/
```

---

## 7. Common Utilities (`common/`)

```
common/
└── decimal.py
```

---

## 8. Data (`data/`)

```
data/
└── sample_prices.csv
```

---

## 9. V-Model Alignment & Traceability

This section explicitly aligns the **code-aligned folder structure** with the frozen **V-Model artifacts**, ensuring full lifecycle traceability.

---

### 9.1 Stakeholder & System Level (Left side of V)

| V-Model Artifact | Coverage in Folder Structure |
|-----------------|------------------------------|
| **StRS** (Stakeholder Req) | Reflected indirectly via `config.yaml`, `app/`, and `execution/` where business constraints (MIS trading, timing windows, force close) are enforced |
| **SyRS** (System Req) | Implemented primarily in `app/` (startup, lifecycle, environment), `infrastructure/` (broker, data feeds), and `execution/` (order placement & limits) |

---

### 9.2 Software Requirements Specification (SRS)

| SRS Concern | Folder(s) |
|------------|-----------|
| Strategy rules & indicators | `domain/strategy`, `domain/indicators`, `domain/timeframe`, `domain/renko` |
| Entry / Exit conditions | `domain/strategy`, enforced by `execution/policy` |
| Risk management | `execution/risk.py`, `execution/sizing.py` |
| Timing constraints (entry window, EOD close) | `app/wiring`, `execution/policy` |
| Persistence & recovery | `infrastructure/persistence` |
| Logging & auditability | `infrastructure/logging` |

---

### 9.3 Software Architecture (SWA / SAD)

| Architectural Layer | Code Folder |
|--------------------|-------------|
| Application Layer | `app/` |
| Domain Layer (Pure Logic) | `domain/` |
| Execution / Control Layer | `execution/` |
| Infrastructure / Adapters | `infrastructure/` |
| Cross-cutting utilities | `common/` |

**Dependency rule enforced:**
`app → domain → execution → infrastructure`  
(No reverse dependencies exist in Phase-10 code.)

---

### 9.4 Detailed Software Design (DSD)

| DSD Element | Implementation Location |
|------------|--------------------------|
| Strategy evaluator & rules | `domain/strategy` |
| Renko builder & bricks | `domain/renko` |
| Indicator computation | `domain/indicators` |
| Execution manager | `execution/executor.py` |
| Risk & quantity sizing | `execution/risk.py`, `execution/sizing.py` |
| Bootstrap & wiring | `app/bootstrap.py`, `app/wiring` |
| Persistence & restart recovery | `infrastructure/persistence` |

---

### 9.5 Verification & Validation (Right side of V)

| V-Model Phase | Folder / Mechanism |
|--------------|--------------------|
| Unit Verification | (Planned) unit tests per module, mapped 1:1 to DSD elements |
| Integration Verification | `app/backtest` runners exercising real pipelines |
| System Validation | Backtest + live wiring symmetry via `app/wiring/pipeline.py` |
| Acceptance Validation | Config-driven runs aligned with StRS & SyRS |

---

### 9.6 Phase-11 Impact Control

With this alignment in place:
- Any Phase-11 change **must reference** one or more of:
  - SRS requirement
  - SW Architecture rule
  - DSD element
- Folder structure changes are **not permitted** unless driven by V-Model updates

---

## 10. Final Verdict

✅ Folder structure is **fully aligned with Phase‑10 frozen code** and **V‑Model artifacts**.

📌 This document is now the **authoritative folder‑structure reference**.

