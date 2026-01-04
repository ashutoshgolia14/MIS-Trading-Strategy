from datetime import time
from datetime import datetime

from domain.strategy.context import StrategyContext
from app.wiring.pipeline import Pipeline

from execution.trading_engine import TradingEngine
from execution.executor import ExecutionManager
from execution.policy.session import MarketSessionPolicy
from execution.risk import RiskManager
from execution.sizing import PositionSizer

from infrastructure.adapters.broker.prod_broker import ProdBroker


def run_runtime(price_stream, brick_size: int):

    pipeline = Pipeline(brick_size=brick_size)

    trading_engine = TradingEngine(
        policy=MarketSessionPolicy(
            entry_start=time(9, 15),
            entry_end=time(11, 00),
            force_close=time(15, 30),
        ),
        risk=RiskManager(max_qty=5),
        sizer=PositionSizer(fixed_qty=1),
        executor=ExecutionManager(ProdBroker()),
    )

    for price in price_stream:
        strategy_context = StrategyContext(
            ts=datetime.now(),
            renko_brick=None,
            indicators_tf1=None,
            indicators_tf2=None,
            indicators_tf3=None,
            indicators_tf4=None,
        )

        trading_context = pipeline.process_tick(
            context=strategy_context,
            price=price,
            symbol="NIFTY"
        )

        if trading_context is None:
            continue

        trading_engine.evaluate_and_execute(trading_context)