from fastapi import APIRouter,HTTPException
from app.config import settings
from app.schemas.stock import StockQuote
import httpx

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

@router.get("/{symbol}", response_model=StockQuote)
async def get_stock(symbol: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://www.alphavantage.co/query",
            params={
                "function": "GLOBAL_QUOTE",
                "symbol": symbol,
                "apikey": settings.alpha_vantage_api_key
            }
        )
        if response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail="Stock data provider is unavailable"
            )

        data = response.json()

        if "Note" in data:
            raise HTTPException(
                status_code=502,
                detail="Stock data provider rejected the request"
            )

        if "Information" in data:
            raise HTTPException(
                status_code=502,
                detail="Stock data provider returned an error"
            )

        quote = data.get("Global Quote")


        if not quote:
            raise HTTPException(
                status_code=404,
                detail="Stock quote not found"
            )

        stock = StockQuote(
            symbol=quote["01. symbol"],
            open=float(quote["02. open"]),
            high=float(quote["03. high"]),
            low=float(quote["04. low"]),
            price=float(quote["05. price"]),
            volume=int(quote["06. volume"]),
            latest_trading_day=quote["07. latest trading day"],
            previous_close=float(quote["08. previous close"]),
            change=float(quote["09. change"]),
            change_percent=float(
                quote["10. change percent"].replace("%", "")
            )
        )
    return stock