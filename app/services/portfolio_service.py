from uuid import uuid4
from app.schemas.portfolio import PortfolioEntry

portfolio = []

def add_to_portfolio(entry):
    invested_value = entry.shares * entry.buy_price

    portfolio_entry = PortfolioEntry(
        id=uuid4(),
        symbol=entry.symbol,
        shares=entry.shares,
        buy_price=entry.buy_price,
        invested_value=invested_value
    )

    portfolio.append(portfolio_entry)

    return portfolio_entry