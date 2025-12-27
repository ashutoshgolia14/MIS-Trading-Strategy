from domain.strategy.models import StrategyState

def next_state(current: StrategyState, bias, flags: dict) -> StrategyState:
    if current == StrategyState.IDLE:
        if bias.name != "NEUTRAL":
            return StrategyState.WAITING_CONFIRMATION
        return current

    if current == StrategyState.WAITING_CONFIRMATION:
        if flags.get("ema_trend_up") and flags.get("supertrend_up"):
            return StrategyState.READY
        return current

    if current == StrategyState.READY:
        return StrategyState.IN_POSITION

    if current == StrategyState.IN_POSITION:
        if not flags.get("ema_trend_up"):
            return StrategyState.EXIT_PENDING
        return current

    if current == StrategyState.EXIT_PENDING:
        return StrategyState.IDLE

    return current
