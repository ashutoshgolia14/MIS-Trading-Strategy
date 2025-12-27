# Phase 11 — Structural Migration (`src/` Introduction)

## Objective
Introduce a `src/`-based folder structure and restore compilation
and execution without changing system behavior.

## Scope
- Move all application code under `src/`
- Add Python entry-point support (`python -m src`)
- Fix packaging and import resolution
- Finalize newly introduced structural files

## Explicit Non-Goals
- No trading logic changes
- No strategy or policy modifications
- No behavioral fixes
- No test additions

## Key Changes
- Introduced `src/` as top-level code container
- Added `src/__main__.py` entry-point shim
- Preserved existing import paths
- Ensured compile/run parity with Phase 10

## Validation
- Application runs via `python -m src`
- No import or module resolution errors
- Backtest path executes

## Status
Completed.