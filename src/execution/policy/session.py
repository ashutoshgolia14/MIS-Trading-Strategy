from datetime import time
from execution.policy.models import PolicyDecision, PolicyVerdict

class MarketSessionPolicy:
    def __init__(self, entry_start: time, entry_end: time, force_close: time):
        self.entry_start = entry_start
        self.entry_end = entry_end
        self.force_close = force_close

    def evaluate(self, decision, ts):
        # Allow exits anytime
        if decision.action and decision.action.startswith("EXIT"):
            return PolicyDecision(PolicyVerdict.ALLOWED)

        # Gate ENTRY actions
        if decision.action and decision.action.startswith("ENTER"):
            t = ts.time()
            if t < self.entry_start:
                return PolicyDecision(
                    PolicyVerdict.BLOCKED,
                    f"Entry not allowed before {self.entry_start}",
                )
            if t > self.entry_end:
                return PolicyDecision(
                    PolicyVerdict.BLOCKED,
                    f"Entry not allowed after {self.entry_end}",
                )

        return PolicyDecision(PolicyVerdict.ALLOWED)
