from execution.policy.models import PolicyDecision, PolicyVerdict

class ForceClosePolicy:
    """Forces a single EXIT when force_close_time is reached or exceeded."""

    def __init__(self, force_close_time):
        self.force_close_time = force_close_time
        self._done = False  # idempotency

    def evaluate(self, ts, ever_entered: bool):
        # If system never entered a position, nothing to force close
        if not ever_entered:
            return PolicyDecision(PolicyVerdict.ALLOWED)

        # If already forced, do nothing
        if self._done:
            return PolicyDecision(PolicyVerdict.ALLOWED)

        # If time reached/exceeded, force EXIT
        if ts.time() >= self.force_close_time:
            self._done = True
            return PolicyDecision(
                PolicyVerdict.BLOCKED,
                f"Forced square-off at {self.force_close_time}"
            )

        return PolicyDecision(PolicyVerdict.ALLOWED)
