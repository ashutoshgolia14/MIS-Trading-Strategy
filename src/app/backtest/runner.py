from datetime import time

from domain.strategy.context import StrategyContext
from app.wiring.pipeline import Pipeline

from app.backtest.data_loader import load_csv
from app.backtest.recorder import BacktestRecorder
from app.backtest.report import generate_report

from execution.trading_engine import TradingEngine
from execution.executor import ExecutionManager
from execution.policy.session import MarketSessionPolicy
from execution.risk import RiskManager
from execution.sizing import PositionSizer

from infrastructure.adapters.broker.test_broker import TestBroker


def run_backtest(csv_path: str, brick_size: int):

    price_data = load_csv(csv_path)
    recorder = BacktestRecorder()

    pipeline = Pipeline(brick_size=brick_size)

    trading_engine = TradingEngine(
        policy=MarketSessionPolicy(
            entry_start=time(9, 15),
            entry_end=time(11, 00),
            force_close=time(15, 30),
        ),
        risk=RiskManager(max_qty=5),
        sizer=PositionSizer(fixed_qty=1),
        executor=ExecutionManager(TestBroker()),
    )

    for row in price_data:
        strategy_context = StrategyContext(
            ts=row["ts"],
            renko_brick=None,
            indicators_tf1=row.get("indicators_tf1"),
            indicators_tf2=row.get("indicators_tf2"),
            indicators_tf3=None,
            indicators_tf4=row.get("indicators_tf4"),
        )

        trading_context = pipeline.process_tick(
            context=strategy_context,
            price=row["price"],
            symbol="NIFTY"
        )

        if trading_context is None:
            continue

        result = trading_engine.evaluate_and_execute(trading_context)
        recorder.record_execution(result, row["ts"])

    return generate_report(recorder)
