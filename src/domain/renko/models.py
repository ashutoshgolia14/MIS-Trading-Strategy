from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class RenkoBrick:
    open: float
    close: float
    high: float
    low: float
    direction: str
    timestamp: datetime
