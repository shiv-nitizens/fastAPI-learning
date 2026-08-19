from app.database.mongodb import db
from bson.decimal128 import Decimal128
from decimal import Decimal
from app.models.transaction import Transaction, TransactionType

async def create_transaction(transaction):
    document = {
        "id": transaction.id,
        "symbol": transaction.symbol,
        "type": transaction.type.value,
        "shares": transaction.shares,
        "price": Decimal128(transaction.price),
        "total_value": Decimal128(transaction.total_value),
        "created_at": transaction.created_at
    }

    result = await db.transactions.insert_one(document)

    return result.inserted_id

async def get_all_transactions():
    cursor = db.transactions.find()
    documents = await cursor.to_list(length=None)

    transactions = []

    for document in documents:
        price = Decimal(document["price"].to_decimal())
        total_value = Decimal(document["total_value"].to_decimal())

        transaction = Transaction(
            id=document["id"],
            symbol=document["symbol"],
            type=TransactionType(document["type"]),
            shares=document["shares"],
            price=price,
            total_value=total_value,
            created_at=document["created_at"]
        )

        transactions.append(transaction)

    return transactions

async def get_transactions_by_symbol(symbol):
    cursor = db.transactions.find({
        "symbol": symbol
    })

    documents = await cursor.to_list(length=None)

    for document in documents:
        document.pop("_id", None)

        document["price"] = Decimal(
            document["price"].to_decimal()
        )

        document["total_value"] = Decimal(
            document["total_value"].to_decimal()
        )

    return documents