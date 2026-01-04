from typing import Optional

from domain.renko.builder import RenkoBuilder
from domain.strategy.context import StrategyContext, TradingContext
from domain.strategy.evaluator import evaluate_strategy


class Pipeline:
    """
    Strategy pipeline.

    Converts StrategyContext into TradingContext
    by evaluating strategy state transitions.
    """

    def __init__(self, brick_size: int):
        self.renko_builder = RenkoBuilder(brick_size)
        self._strategy_snapshot = None

    def process_tick(
        self,
        context: StrategyContext,
        price: float,
        symbol,
    ) -> Optional[TradingContext]:

        # 1. Update Renko
        renko_brick = self.renko_builder.process_price(price, context.ts)
        if renko_brick is None:
            return None

        # 2. Evaluate strategy
        new_snapshot = evaluate_strategy(
            snapshot=self._strategy_snapshot,
            context=context,
        )
        self._strategy_snapshot = new_snapshot

        if new_snapshot.last_decision is None:
            return None

        # 3. Build TradingContext (explicit conversion)
        return TradingContext(
            timestamp=context.ts,
            symbol=symbol,
            side=new_snapshot.last_decision.side,
            decision=new_snapshot.last_decision,
        )
