from domain.renko.builder import RenkoBuilder
from domain.indicators.calculators import build_snapshot
from domain.strategy.evaluator import evaluate_strategy
from domain.strategy.models import StrategySnapshot, StrategyState, Bias
from execution.executor import TradeExecutor
from execution.policy.evaluator import PolicyEvaluator
from execution.policy.session import MarketSessionPolicy
from execution.policy.force_close import ForceClosePolicy
from infrastructure.config.loader import load_trading_policy_config

from datetime import time


class Pipeline:
    def _init_policy(self):
        cfg = load_trading_policy_config()
        self._position_open = False
        self._ever_entered = False
        self._force_close = ForceClosePolicy(cfg.force_close_time)
        self.policy = PolicyEvaluator([
            MarketSessionPolicy(cfg.entry_window_start, cfg.entry_window_end, cfg.force_close_time)
        ], force_close_policy=self._force_close)

    def __init__(self, brick_size, executor: TradeExecutor):
        self._init_policy()

        self.renko = RenkoBuilder(brick_size=brick_size)
        self.executor = executor
        self.snapshot = StrategySnapshot(
            state=StrategyState.IDLE,
            bias=Bias.NEUTRAL,
        )

    def process_tick(self, price, ts, indicator_data, symbol):
        brick = self.renko.process_price(price, ts)
        if not brick:
            return None

        indicators = build_snapshot(**indicator_data)
        context = type("Ctx", (), {
            "ts": ts,
            "renko_brick": brick,
            "indicators_tf1": indicators,
            "indicators_tf2": indicators,
            "indicators_tf3": indicators,
            "indicators_tf4": indicators,
        })()

        self.snapshot = evaluate_strategy(self.snapshot, context)
        if self.snapshot.last_decision:
            pd = self.policy.evaluate(self.snapshot.last_decision, ts, self._ever_entered)
            # Forced square-off: generate EXIT regardless of strategy
            if pd.verdict.name == 'BLOCKED' and pd.reason and pd.reason.startswith('Forced square-off'):
                # synthesize EXIT decision
                class _Exit:
                    action = 'EXIT'
                    reason = pd.reason
                res = self.executor.execute(_Exit(), symbol)
                self._position_open = False
                return res
            if pd.verdict.name == 'BLOCKED':
                return None
            res = self.executor.execute(self.snapshot.last_decision, symbol)
            # Update position state on ENTER/EXIT
            if self.snapshot.last_decision.action.startswith('ENTER'):
                self._position_open = True
                self._ever_entered = True
            if self.snapshot.last_decision.action.startswith('EXIT'):
                self._position_open = False
            return res

        return None
