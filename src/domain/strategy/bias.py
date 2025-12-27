from domain.strategy.models import Bias

def compute_bias(tf1_snapshot, tf2_snapshot) -> Bias:
    if tf1_snapshot is None or tf2_snapshot is None:
        return Bias.NEUTRAL

    if (
        tf1_snapshot.ema20 > tf1_snapshot.ema20_prev
        and tf2_snapshot.ema20 > tf2_snapshot.ema20_prev
    ):
        return Bias.BULLISH

    if (
        tf1_snapshot.ema20 < tf1_snapshot.ema20_prev
        and tf2_snapshot.ema20 < tf2_snapshot.ema20_prev
    ):
        return Bias.BEARISH

    return Bias.NEUTRAL
