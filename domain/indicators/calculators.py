from domain.indicators.models import IndicatorSnapshot

def build_snapshot(
    ema20,
    ema20_prev,
    macd_hist,
    macd_hist_prev,
    rsi,
    supertrend_dir,
) -> IndicatorSnapshot:
    return IndicatorSnapshot(
        ema20=ema20,
        ema20_prev=ema20_prev,
        macd_hist=macd_hist,
        macd_hist_prev=macd_hist_prev,
        rsi=rsi,
        supertrend_dir=supertrend_dir,
    )
