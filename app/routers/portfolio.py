from fastapi import APIRouter,status
from app.schemas.portfolio import PortfolioCreate,PortfolioResponse
from app.storage.portfolio import portfolio

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

@router.get("")
def get_portfolio():
    return portfolio

@router.post(
    "",
    response_model=PortfolioResponse,
    status_code=status.HTTP_201_CREATED
    )
def add_to_portfolio(entry: PortfolioCreate):
    portfolio.append(entry)

    return entry