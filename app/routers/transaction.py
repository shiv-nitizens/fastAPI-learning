from fastapi import APIRouter, status,Depends
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.services.transaction_service import create_transaction,get_transactions as get_transactions_service,get_portfolio as get_portfolio_service,get_transactions_by_symbol as get_transactions_by_symbol_service
from app.schemas.portfolio import PortfolioSummary
from app.security.auth import get_current_user

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post(
    "",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_transaction_endpoint(transaction: TransactionCreate,user = Depends(get_current_user)):
    return await create_transaction(transaction,user)

@router.get("")
async def get_transactions(
    user=Depends(get_current_user)
):
    return await get_transactions_service(user)


@router.get("/portfolio", response_model=PortfolioSummary)
async def get_portfolio_endpoint(
    user=Depends(get_current_user)
):
    return await get_portfolio_service(user)

@router.get("/{symbol}")
async def get_transactions_by_symbol_endpoint(
    symbol: str,
    user=Depends(get_current_user)
):
    return await get_transactions_by_symbol_service(symbol, user)