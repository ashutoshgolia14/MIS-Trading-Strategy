# 📦 MIS-Trading-Strategy

### 🔗 Auto-generated Raw GitHub File Index

> ⚠️ **Auto-generated from canonical JSON index**  
> Do not edit manually. Regenerate from JSON if repo changes.

> **Repository:** https://github.com/ashutoshgolia14/MIS-Trading-Strategy  
> **Branch:** `main`


## 🏠 Root

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `README.md` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/README.md) |


## ⚙️ Core

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `__init__.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/__init__.py) |
| `__main__.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/__main__.py) |

## 🧩 Application Layer (`src/app`)


## Bootstrap

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `bootstrap.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/bootstrap.py) |
| `env.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/env.py) |


## Backtest

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `data_loader.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/backtest/data_loader.py) |
| `recorder.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/backtest/recorder.py) |
| `report.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/backtest/report.py) |
| `runner.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/backtest/runner.py) |


## Wiring & Runtime

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `context_builder.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/wiring/context_builder.py) |
| `pipeline.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/wiring/pipeline.py) |
| `runtime.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/app/wiring/runtime.py) |

## 📊 Domain Layer (`src/domain`)


## Indicators

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `calculators.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/indicators/calculators.py) |
| `models.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/indicators/models.py) |


## Renko

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `builder.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/renko/builder.py) |
| `models.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/renko/models.py) |


## Strategy

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `context.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/strategy/context.py) |
| `models.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/strategy/models.py) |
| `evaluator.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/strategy/evaluator.py) |
| `flags.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/strategy/flags.py) |
| `bias.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/strategy/bias.py) |
| `state.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/strategy/state.py) |


## Timeframe

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `timeframe.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/domain/timeframe/timeframe.py) |

## 🚀 Execution Layer (`src/execution`)


## Execution

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `executor.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/executor.py) |
| `models.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/models.py) |
| `ports.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/ports.py) |
| `risk.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/risk.py) |
| `sizing.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/sizing.py) |
| `policy/evaluator.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/policy/evaluator.py) |
| `policy/force_close.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/policy/force_close.py) |
| `policy/models.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/policy/models.py) |
| `policy/session.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/execution/policy/session.py) |

## 🏗️ Infrastructure (`src/infrastructure`)


## Infrastructure

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `adapters/broker` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/{'base.py': 'src/infrastructure/adapters/broker/base.py', 'prod_broker.py': 'src/infrastructure/adapters/broker/prod_broker.py', 'test_broker.py': 'src/infrastructure/adapters/broker/test_broker.py'}) |
| `config/errors.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/infrastructure/config/errors.py) |
| `config/loader.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/infrastructure/config/loader.py) |
| `config/schema.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/infrastructure/config/schema.py) |
| `logging/logger.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/infrastructure/logging/logger.py) |
| `persistence/state_store.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/infrastructure/persistence/state_store.py) |


## 🧰 Common

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `decimal.py` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/common/decimal.py) |


## 📂 Data

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `sample_prices.csv` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/src/data/sample_prices.csv) |

## 📚 Documentation (`docs`)


## 00_overview

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `mis_algo_trading_final_folder_structure_sw_aligned.md` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/docs/00_overview/mis_algo_trading_final_folder_structure_sw_aligned.md) |


## 02_architecture

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `mis_algo_trading_software_architecture_specfication_sw_ad.md` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/docs/02_architecture/mis_algo_trading_software_architecture_specfication_sw_ad.md) |
| `mis_algo_trading_software_architecture_rev_b_srs_traceability_aligned.md` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/docs/02_architecture/mis_algo_trading_software_architecture_rev_b_srs_traceability_aligned.md) |


## 03_design

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `mis_algo_trading_detailed_software_design_dsd.md` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/docs/03_design/mis_algo_trading_detailed_software_design_dsd.md) |


## 09_reviews_audit

| 📄 File | 🔗 Raw Link |
|--------|------------|
| `phase_14_Corrective_Action_Log.md` | [View](https://raw.githubusercontent.com/ashutoshgolia14/MIS-Trading-Strategy/main/docs/09_reviews_audit/phase_14_Corrective_Action_Log.md) |
