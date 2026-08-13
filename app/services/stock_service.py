import httpx
from fastapi import HTTPException

from app.config import settings
from app.schemas.stock import StockQuote

async def get_stock_quote(symbol: str):
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

    if "Note" in data or "Information" in data:
        print(data)
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

    return StockQuote(
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