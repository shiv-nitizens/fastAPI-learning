from pydantic import BaseModel

class PortfolioCreate(BaseModel):
    symbol:str
    shares:int
    buy_price:float

class PortfolioResponse(BaseModel):
    symbol: str
    shares: int
    buy_price: float

class PortfolioEntry(BaseModel):
    id:UUID
    symbol:str
    shares:int
    buy_price:float
    invested_value:float
