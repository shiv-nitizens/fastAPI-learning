from decimal import Decimal
from pydantic import BaseModel


class PortfolioResponse(BaseModel):
    symbol: str
    shares: int
    invested_value: Decimal
    current_price: Decimal
    market_value: Decimal
    profit_loss: Decimal