from domain.strategy.context import StrategyContext

def build_context(ts, brick, tf1, tf2, tf3, tf4) -> StrategyContext:
    return StrategyContext(
        ts=ts,
        renko_brick=brick,
        indicators_tf1=tf1,
        indicators_tf2=tf2,
        indicators_tf3=tf3,
        indicators_tf4=tf4,
    )
