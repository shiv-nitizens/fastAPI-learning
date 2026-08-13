from pydantic import BaseModel
from uuid import UUID

class PortfolioCreate(BaseModel):
    symbol:str
    shares:int
    buy_price:float

class PortfolioResponse(BaseModel):
    symbol: str
    shares: int
    buy_price: float
    current_price: Decimal
    market_value: Decimal
    profit_loss: Decimal

class PortfolioEntry(BaseModel):
    id:UUID
    symbol:str
    shares:int
    buy_price:float
    invested_value:float
