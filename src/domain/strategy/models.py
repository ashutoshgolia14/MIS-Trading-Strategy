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
    ema20: float
    ema20_prev: float
    macd_hist: float
    macd_hist_prev: float
    rsi: float
    supertrend_dir: str
    state: StrategyState
    bias: Bias
    last_decision: Optional[StrategyDecision] = None

    @classmethod
    def bootstrap(cls, context):
        """
        Create an initial snapshot so that strategy evaluation
        never sees a None snapshot.
        """
        # Conservative initialization:
        # If a Renko brick exists, use its close;
        # otherwise fall back to zero.
        if context.renko_brick is not None:
            initial_ema = context.renko_brick.close
        else:
            initial_ema = 0.0

        initial_macd = 0.0
        initial_rsi = 50.0
        initial_supertrend = "down"

        return cls(
            ema20=initial_ema,
            ema20_prev=initial_ema,
            macd_hist=initial_macd,
            macd_hist_prev=initial_macd,
            rsi=initial_rsi,
            supertrend_dir=initial_supertrend,
            state=StrategyState.IDLE,
            bias=Bias.NEUTRAL,
            last_decision=None
        )
