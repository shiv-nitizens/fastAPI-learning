from fastapi import APIRouter, status
from app.schemas.portfolio import PortfolioCreate, PortfolioEntry
from app.services.portfolio_service import add_to_portfolio as add_portfolio_service,get_portfolio as get_portfolio_service

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

@router.get("", response_model=list[PortfolioEntry])
async def get_portfolio():
    return await get_portfolio_service()
    
@router.post(
    "",
    response_model=PortfolioEntry,
    status_code=status.HTTP_201_CREATED
)
async def add_to_portfolio(entry: PortfolioCreate):
    portfolio_entry = await add_portfolio_service(entry)
    return portfolio_entry