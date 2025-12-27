from datetime import datetime
from execution.executor import TradeExecutor
from execution.risk import RiskManager
from execution.sizing import PositionSizer
from infrastructure.adapters.broker.test_broker import TestBroker
from app.wiring.pipeline import Pipeline

def run_once():
    executor = TradeExecutor(
        broker=TestBroker(),
        risk=RiskManager(max_qty=5),
        sizer=PositionSizer(fixed_qty=1),
    )

    pipeline = Pipeline(brick_size=10, executor=executor)

    dummy_indicator = {
        "ema20": 110,
        "ema20_prev": 100,
        "macd_hist": 1,
        "macd_hist_prev": 0,
        "rsi": 60,
        "supertrend_dir": "up",
    }

    prices = [100, 105, 111, 120]
    for p in prices:
        result = pipeline.process_tick(
            price=p,
            ts=datetime.now(),
            indicator_data=dummy_indicator,
            symbol="TEST",
        )
        if result:
            print(result)

if __name__ == "__main__":
    run_once()
