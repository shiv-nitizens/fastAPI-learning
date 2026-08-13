from fastapi import FastAPI
from app.routers.stocks import router as stocks_router
from app.config import settings
from app.routers.transaction import router as transaction_router

app = FastAPI()
app.include_router(stocks_router)
app.include_router(transaction_router)

@app.get("/")
def home():
    return {
        "message":"welcome puta madre..."
    }
