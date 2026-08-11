from fastapi import APIRouter, status
from app.schemas.portfolio import PortfolioCreate, PortfolioEntry
from app.services.portfolio_service import add_to_portfolio as add_portfolio_service
from app.storage.portfolio import portfolio

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

@router.get("", response_model=list[PortfolioEntry])
def get_portfolio():
    return portfolio
    
@router.post(
    "",
    response_model=PortfolioEntry,
    status_code=status.HTTP_201_CREATED
)
def add_to_portfolio(entry: PortfolioCreate):
    portfolio_entry = add_portfolio_service(entry)
    return portfolio_entry