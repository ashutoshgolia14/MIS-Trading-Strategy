from dataclasses import dataclass
from enum import Enum
from typing import Optional, Literal

class Bias(str, Enum):
    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    NEUTRAL = "NEUTRAL"

class StrategyState(str, Enum):
    IDLE = "IDLE"
    WAITING_CONFIRMATION = "WAITING_CONFIRMATION"
    READY = "READY"
    IN_POSITION = "IN_POSITION"
    EXIT_PENDING = "EXIT_PENDING"

@dataclass(frozen=True)
class StrategyDecision:
    action: Literal["ENTER_LONG", "EXIT", "HOLD"]
    reason: str

@dataclass
class StrategySnapshot:
    state: StrategyState
    bias: Bias
    last_decision: Optional[StrategyDecision] = None
