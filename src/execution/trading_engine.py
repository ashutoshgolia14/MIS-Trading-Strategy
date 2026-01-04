from execution.executor import ExecutionManager
from execution.models import ExecutionOrder, ExecutionResult
from execution.policy.session import MarketSessionPolicy
from execution.risk import RiskManager
from execution.sizing import PositionSizer

class TradingEngine:
    def __init__(
        self,
        policy: MarketSessionPolicy,
        risk: RiskManager,
        sizer: PositionSizer,
        executor: ExecutionManager,
    ):
        self.policy = policy
        self.risk = risk
        self.sizer = sizer
        self.executor = executor

        # lifecycle state (OWNED HERE)
        self._position_open = False
        self._ever_entered = False

    def evaluate_and_execute(self, context) -> ExecutionResult:
        """
        Central execution authority.
        Owns position lifecycle and execution decisions.
        """

        # 1. Resolve lifecycle intent
        intent = context.decision.action

        if intent == "ENTER" and self._position_open:
            return ExecutionResult.no_op("Position already open")

        if intent == "EXIT" and not self._position_open:
            return ExecutionResult.no_op("No open position")

        # 2. Session / policy enforcement
        policy_decision = self.policy.evaluate(
            context.decision,
            context.timestamp,
        )

        if not policy_decision.allowed:
            # forced exit overrides lifecycle
            if policy_decision.force_exit and self._position_open:
                intent = "EXIT"
            else:
                return ExecutionResult.denied("Session policy blocked")

        # 3. HOLD means nothing to do
        if intent == "HOLD":
            return ExecutionResult.no_op("Hold")

        # 4. Build execution order
        qty = self.sizer.size()
        order = ExecutionOrder(
            symbol=context.symbol,
            side=context.side,
            quantity=qty,
        )

        # 5. Risk validation
        if not self.risk.validate(order):
            return ExecutionResult.denied("Risk validation failed")

        # 6. Execute
        result = self.executor.execute(order)

        # 7. Update lifecycle on success
        if result.success:
            if intent == "ENTER":
                self._position_open = True
                self._ever_entered = True
            elif intent == "EXIT":
                self._position_open = False

        return result
