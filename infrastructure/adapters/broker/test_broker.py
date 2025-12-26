from execution.ports import BrokerPort
from execution.models import ExecutionResult, OrderStatus

class TestBroker(BrokerPort):
    def place_order(self, order):
        return ExecutionResult(
            status=OrderStatus.FILLED,
            fill_price=100.0,
        )
