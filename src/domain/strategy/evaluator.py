from domain.strategy.bias import compute_bias
from domain.strategy.flags import derive_flags
from domain.strategy.state import next_state
from domain.strategy.models import StrategyDecision, StrategySnapshot

def evaluate_strategy(snapshot: StrategySnapshot, context) -> StrategySnapshot:

    if snapshot is None:
        snapshot = StrategySnapshot.bootstrap(context)

    bias = compute_bias(context.indicators_tf1, context.indicators_tf2)
    flags = derive_flags(snapshot)
    new_state = next_state(snapshot.state, bias, flags)

    decision = None
    if snapshot.state != new_state:
        if new_state.name == "IN_POSITION":
            decision = StrategyDecision(
                action="ENTER_LONG",
                reason="Bias confirmed and entry conditions met",
            )
        elif new_state.name == "EXIT_PENDING":
            decision = StrategyDecision(
                action="EXIT",
                reason="Trend invalidated",
            )

    return StrategySnapshot(
        ema20=snapshot.ema20,
        ema20_prev=snapshot.ema20_prev,
        macd_hist=snapshot.macd_hist,
        macd_hist_prev=snapshot.macd_hist_prev,
        rsi=snapshot.rsi,
        supertrend_dir=snapshot.supertrend_dir,
        bias=bias,
        state=new_state,
        last_decision=decision,
    )
