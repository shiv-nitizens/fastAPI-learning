from fastapi import APIRouter, status
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.services.transaction_service import create_transaction


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