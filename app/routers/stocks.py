from fastapi import APIRouter,HTTPException
from app.config import settings
from app.schemas.stock import StockQuote,StockSearchResult
import httpx
from app.services.stock_service import get_stock_quote

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
    return await get_stock_quote(symbol)