from uuid import uuid4
from app.schemas.portfolio import PortfolioEntry
from app.repositories.portfolio_repository import create_portfolio_entry,get_all_portfolio_entries

async def get_portfolio():
    return await get_all_portfolio_entries()

async def add_to_portfolio(entry):
    invested_value = entry.shares * entry.buy_price

    portfolio_entry = PortfolioEntry(
        id=uuid4(),
        symbol=entry.symbol,
        shares=entry.shares,
        buy_price=entry.buy_price,
        invested_value=invested_value
    )

    await create_portfolio_entry(portfolio_entry)

    return portfolio_entry