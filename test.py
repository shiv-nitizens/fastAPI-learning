import httpx

from app.config import settings


response = httpx.get(
    "https://www.alphavantage.co/query",
    params={
        "function": "SYMBOL_SEARCH",
        "keywords": "apple",
        "apikey": settings.alpha_vantage_api_key
    }
)

print(response.status_code)
print(response.json())