from datetime import datetime, timezone
from uuid import uuid4
from app.models.transaction import Transaction
from app.repositories.transaction_repository import create_transaction as save_transaction

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