from dataclasses import dataclass

@dataclass(frozen=True)
class IndicatorSnapshot:
    ema20: float
    ema20_prev: float
    macd_hist: float
    macd_hist_prev: float
    rsi: float
    supertrend_dir: str
