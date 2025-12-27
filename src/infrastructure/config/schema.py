from dataclasses import dataclass
from datetime import time

@dataclass(frozen=True)
class TradingPolicyConfig:
    entry_window_start: time
    entry_window_end: time
    force_close_time: time

DEFAULT_TRADING_POLICY = TradingPolicyConfig(
    entry_window_start=time(9, 30),
    entry_window_end=time(11, 0),
    force_close_time=time(15, 15),
)
