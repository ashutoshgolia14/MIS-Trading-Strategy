from enum import Enum

class Timeframe(str, Enum):
    TF1_DAILY = "DAILY"
    TF2_1H = "1H"
    TF3_15M = "15M"
    TF4_RENKO = "RENKO"
