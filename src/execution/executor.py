from execution.models import ExecutionOrder, ExecutionResult
from execution.ports import BrokerPort

class ExecutionManager:
    def __init__(self, broker: BrokerPort):
        self.broker = broker

    def execute(self, order: ExecutionOrder) -> ExecutionResult:
        return self.broker.place_order(order)
