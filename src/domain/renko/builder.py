from domain.renko.models import RenkoBrick
from datetime import datetime


class RenkoBuilder:
    def __init__(self, brick_size: float):
        self.brick_size = brick_size
        self.last_close = None

    def process_price(self, price: float, ts: datetime):
        if self.last_close is None:
            self.last_close = price
            return None

        diff = price - self.last_close

        if abs(diff) < self.brick_size:
            return None

        direction = "up" if diff > 0 else "down"
        brick = RenkoBrick(
            open=self.last_close,
            close=self.last_close + self.brick_size * (1 if diff > 0 else -1),
            high=max(price, self.last_close),
            low=min(price, self.last_close),
            direction=direction,
            timestamp=ts,
        )

        self.last_close = brick.close
        return brick
