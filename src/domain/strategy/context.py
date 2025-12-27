from dataclasses import dataclass
from datetime import datetime
from domain.renko.models import RenkoBrick

@dataclass(frozen=True)
class StrategyContext:
    ts: datetime
    renko_brick: RenkoBrick
    indicators_tf1: object
    indicators_tf2: object
    indicators_tf3: object
    indicators_tf4: object
