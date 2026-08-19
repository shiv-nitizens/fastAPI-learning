from datetime import datetime, timezone
from uuid import uuid4
from app.models.transaction import Transaction, TransactionType
from app.repositories.transaction_repository import create_transaction as save_transaction , get_all_transactions
from decimal import Decimal
from app.services.stock_service import get_stock_quote
import asyncio

async def create_transaction(transaction):
    total_value = transaction.shares * transaction.price

    transaction_model = Transaction(
        id=uuid4(),
        symbol=transaction.symbol,
        type=transaction.type,
        shares=transaction.shares,
        price=transaction.price,
        total_value=total_value,
        created_at=datetime.now(timezone.utc)
    )

    await save_transaction(transaction_model)

    return transaction_model

async def get_transactions():
    return await get_all_transactions()

def calculate_position(transactions):
    shares = 0
    invested_value = Decimal("0")

    for transaction in transactions:

        if transaction.type == TransactionType.BUY:
            shares += transaction.shares
            invested_value += (
                Decimal(transaction.shares) * transaction.price
            )

        elif transaction.type == TransactionType.SELL:
            average_cost = invested_value / Decimal(shares)

            cost_of_sold_shares = (
                Decimal(transaction.shares) * average_cost
            )

            shares -= transaction.shares
            invested_value -= cost_of_sold_shares

    return {
        "shares": shares,
        "invested_value": invested_value
    }

async def get_portfolio():
    transactions = await get_all_transactions()

    positions = {}

    for transaction in transactions:
        if transaction.symbol not in positions:
            positions[transaction.symbol] = []

        positions[transaction.symbol].append(transaction)

    result = []

    total_invested_value = Decimal("0")
    total_market_value = Decimal("0")
    total_profit_loss = Decimal("0")

    for symbol, symbol_transactions in positions.items():
        position = calculate_position(symbol_transactions)

        stock_quote = await get_stock_quote(symbol)
        current_price = Decimal(str(stock_quote.price))

        market_value = Decimal(position["shares"]) * current_price
        profit_loss = market_value - position["invested_value"]

        result.append({
            "symbol": symbol,
            "shares": position["shares"],
            "invested_value": position["invested_value"],
            "current_price": current_price,
            "market_value": market_value,
            "profit_loss": profit_loss
        })

        total_invested_value += position["invested_value"]
        total_market_value += market_value
        total_profit_loss += profit_loss

        await asyncio.sleep(1)

    return {
        "positions": result,
        "total_invested_value": total_invested_value,
        "total_market_value": total_market_value,
        "total_profit_loss": total_profit_loss
    }