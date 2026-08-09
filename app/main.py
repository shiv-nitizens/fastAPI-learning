from fastapi import FastAPI
from app.routers.stocks import router as stocks_router
from app.routers.portfolio import router as portfolio_router
from app.config import settings

app = FastAPI()
app.include_router(stocks_router)
app.include_router(portfolio_router)

@app.get("/")
def home():
    return {
        "message":"welcome puta madre..."
    }
