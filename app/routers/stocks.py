from fastapi import APIRouter,HTTPException
from app.config import settings
from app.schemas.stock import StockQuote,StockSearchResult
import httpx

router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"]
)
@router.get("/search",response_model=list[StockSearchResult])
async def search_stocks(q: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://www.alphavantage.co/query",
            params={
                "function": "SYMBOL_SEARCH",
                "keywords": q,
                "apikey": settings.alpha_vantage_api_key
            }
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="Stock data provider is unavailable"
        )

    data = response.json()

    if "Note" in data or "Information" in data or "Error Message" in data:
        raise HTTPException(
            status_code=502,
            detail="Stock data provider returned an error"
        )

    matches = data.get("bestMatches", [])

    results = []

    for match in matches:
        results.append(
            StockSearchResult(
                symbol=match["1. symbol"],
                name=match["2. name"],
                type=match["3. type"],
                region=match["4. region"],
                currency=match["8. currency"]
            )
        )

    return results

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