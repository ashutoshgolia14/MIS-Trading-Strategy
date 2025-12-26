from dataclasses import dataclass
from enum import Enum
from typing import Optional

class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderStatus(str, Enum):
    NEW = "NEW"
    REJECTED = "REJECTED"
    SUBMITTED = "SUBMITTED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"

@dataclass(frozen=True)
class ExecutionOrder:
    symbol: str
    side: OrderSide
    quantity: int
    reason: str

@dataclass
class ExecutionResult:
    status: OrderStatus
    fill_price: Optional[float] = None
    reason: Optional[str] = None
