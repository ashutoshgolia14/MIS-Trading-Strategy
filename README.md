# MIS Algo Trading – Unified Baseline (Phases 1–10)

## Phase 10 – Forced Square-off (Corrected)
- Forced square-off triggers if the system has **ever entered** a position
- Independent of current strategy state
- Idempotent (exactly one forced EXIT)
- Driven by `force_close_time` from config.yaml
