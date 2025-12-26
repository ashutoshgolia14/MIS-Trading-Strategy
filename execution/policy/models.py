from enum import Enum
from dataclasses import dataclass
from typing import Optional

class PolicyVerdict(str, Enum):
    ALLOWED = "ALLOWED"
    BLOCKED = "BLOCKED"

@dataclass
class PolicyDecision:
    verdict: PolicyVerdict
    reason: Optional[str] = None
