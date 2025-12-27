from execution.policy.models import PolicyVerdict, PolicyDecision

class PolicyEvaluator:
    def __init__(self, policies, force_close_policy=None):
        self.policies = policies
        self.force_close_policy = force_close_policy

    def evaluate(self, decision, ts, ever_entered=False):
        # Forced square-off takes precedence
        if self.force_close_policy is not None:
            res = self.force_close_policy.evaluate(ts, ever_entered)
            if res.verdict == PolicyVerdict.BLOCKED:
                return res

        last = PolicyDecision(PolicyVerdict.ALLOWED)
        for p in self.policies:
            res = p.evaluate(decision, ts)
            if res.verdict == PolicyVerdict.BLOCKED:
                return res
            last = res
        return last
