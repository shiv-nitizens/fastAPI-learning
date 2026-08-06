from fastapi import APIRouter,HTTPException
from app.schemas.portfolio import PortfolioCreate

router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"]
)

stocks = [
    {"symbol": "AAPL", "name": "Apple Inc."},
    {"symbol": "NVDA", "name": "NVIDIA Corporation"},
    {"symbol": "MSFT", "name": "Microsoft Corporation"},
    {"symbol": "TSLA", "name": "Tesla Inc."},
]

@router.get("/search")
def search_stocks(q:str):
    result = []
    
    for stock in stocks:
        if q.lower() in stock["name"].lower() or q.lower() in stock["symbol"].lower():
            result.append(stock)

    return result

@router.get("/{symbol}")
def get_stock(symbol:str):
    for stock in stocks:
        if stock["symbol"] == symbol.upper():
            return stock

    raise HTTPException(
        status_code=404,
        detail="Stock not found"
    )
