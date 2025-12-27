from app.backtest.data_loader import load_csv
from app.backtest.recorder import BacktestRecorder
from app.backtest.report import generate_report
from app.wiring.pipeline import Pipeline
from execution.executor import TradeExecutor
from execution.risk import RiskManager
from execution.sizing import PositionSizer
from infrastructure.adapters.broker.test_broker import TestBroker

def run_backtest(csv_path, brick_size=10):
    executor = TradeExecutor(TestBroker(), RiskManager(5), PositionSizer(1))
    pipeline = Pipeline(brick_size, executor)
    recorder = BacktestRecorder()
    dummy = {'ema20':110,'ema20_prev':100,'macd_hist':1,'macd_hist_prev':0,'rsi':60,'supertrend_dir':'up'}
    for row in load_csv(csv_path):
        recorder.record_tick()
        result = pipeline.process_tick(row['price'], row['ts'], dummy, 'TEST')
        if result:
            recorder.record_execution(result, row['ts'])
    generate_report(recorder)

if __name__ == '__main__':
    run_backtest('data/sample_prices.csv')
