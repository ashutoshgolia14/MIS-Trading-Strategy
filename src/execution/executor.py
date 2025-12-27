from execution.models import (
    ExecutionOrder,
    ExecutionResult,
    OrderStatus,
    OrderSide,
)
from execution.risk import RiskManager
from execution.sizing import PositionSizer
from execution.ports import BrokerPort

class TradeExecutor:
    def __init__(self, broker: BrokerPort, risk: RiskManager, sizer: PositionSizer):
        self.broker = broker
        self.risk = risk
        self.sizer = sizer

    def execute(self, decision, symbol: str) -> ExecutionResult:
        if decision.action != "ENTER_LONG":
            return ExecutionResult(
                status=OrderStatus.REJECTED,
                reason="No executable action",
            )

        qty = self.sizer.size()
        order = ExecutionOrder(
            symbol=symbol,
            side=OrderSide.BUY,
            quantity=qty,
            reason=decision.reason,
        )

        if not self.risk.validate(order):
            return ExecutionResult(
                status=OrderStatus.REJECTED,
                reason="Risk check failed",
            )

        return self.broker.place_order(order)
