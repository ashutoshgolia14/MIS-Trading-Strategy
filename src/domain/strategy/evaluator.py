from domain.strategy.bias import compute_bias
from domain.strategy.flags import derive_flags
from domain.strategy.state import next_state
from domain.strategy.models import StrategyDecision, StrategySnapshot

def evaluate_strategy(snapshot: StrategySnapshot, context) -> StrategySnapshot:
    bias = compute_bias(context.indicators_tf1, context.indicators_tf2)
    flags = derive_flags(context.indicators_tf4)
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
        state=new_state,
        bias=bias,
        last_decision=decision,
    )
