class PositionSizer:
    def __init__(self, fixed_qty: int):
        self.fixed_qty = fixed_qty

    def size(self) -> int:
        return self.fixed_qty
