from execution.models import ExecutionOrder

class RiskManager:
    def __init__(self, max_qty: int):
        self.max_qty = max_qty

    def validate(self, order: ExecutionOrder) -> bool:
        if order.quantity <= 0:
            return False
        if order.quantity > self.max_qty:
            return False
        return True
