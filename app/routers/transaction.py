from fastapi import APIRouter, status
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.services.transaction_service import create_transaction,get_transactions as get_transactions_service,get_portfolio as get_portfolio_service


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post(
    "",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_transaction_endpoint(transaction: TransactionCreate):
    return await create_transaction(transaction)

@router.get(
    "",
    response_model=list[TransactionResponse])
async def get_transactions():
    return await get_transactions_service()

@router.get("/portfolio")
async def get_portfolio_endpoint():
    return await get_portfolio_service()