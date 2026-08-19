from datetime import datetime
from enum import Enum
from uuid import UUID
from decimal import Decimal

class TransactionType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class Transaction:
    def __init__(
        self,
        id: UUID,
        user_id: UUID,
        symbol: str,
        type: TransactionType,
        shares: int,
        price: Decimal,
        total_value: Decimal,
        created_at: datetime
    ):
        self.id = id
        self.user_id = user_id
        self.symbol = symbol
        self.type = type
        self.shares = shares
        self.price = price
        self.total_value = total_value
        self.created_at = created_at