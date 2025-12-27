from enum import Enum
import os

class RunMode(str, Enum):
    TEST = "TEST"
    PROD = "PROD"

def get_run_mode() -> RunMode:
    return RunMode(os.getenv("MIS_RUN_MODE", "TEST"))
