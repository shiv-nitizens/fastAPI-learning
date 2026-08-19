from decimal import Decimal
from pydantic import BaseModel


class PortfolioResponse(BaseModel):
    symbol: str
    shares: int
    invested_value: Decimal
    current_price: Decimal
    market_value: Decimal
    profit_loss: Decimal

class PortfolioSummary(BaseModel):
    positions: list[PortfolioResponse]
    total_invested_value: Decimal
    total_market_value: Decimal
    total_profit_loss: Decimal