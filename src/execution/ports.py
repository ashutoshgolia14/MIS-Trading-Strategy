from abc import ABC, abstractmethod
from execution.models import ExecutionOrder, ExecutionResult

class BrokerPort(ABC):
    @abstractmethod
    def place_order(self, order: ExecutionOrder) -> ExecutionResult:
        pass
