def derive_flags(snapshot):
    return {
        "ema_trend_up": snapshot.ema20 > snapshot.ema20_prev,
        "macd_hist_rising": snapshot.macd_hist > snapshot.macd_hist_prev,
        "rsi_above_mid": snapshot.rsi > 50,
        "supertrend_up": snapshot.supertrend_dir == "up",
    }
