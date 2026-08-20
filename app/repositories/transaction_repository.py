from app.database.mongodb import db
from bson.decimal128 import Decimal128
from decimal import Decimal
from app.models.transaction import Transaction, TransactionType

async def create_transaction(transaction):
    document = {
        "id": transaction.id,
        "user_id": transaction.user_id,
        "symbol": transaction.symbol,
        "type": transaction.type.value,
        "shares": transaction.shares,
        "price": Decimal128(transaction.price),
        "total_value": Decimal128(transaction.total_value),
        "created_at": transaction.created_at
    }

    result = await db.transactions.insert_one(document)

    return result.inserted_id

async def get_transactions_by_symbol(symbol,user_id):
    cursor = db.transactions.find({
        "user_id":user_id,
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

async def get_transactions_by_user_id(user_id):
    cursor = db.transactions.find({
        "user_id": user_id
    })

    documents = await cursor.to_list(length=None)

    transactions = []

    for document in documents:
        transaction = Transaction(
            id=document["id"],
            user_id=document["user_id"],
            symbol=document["symbol"],
            type=TransactionType(document["type"]),
            shares=document["shares"],
            price=Decimal(document["price"].to_decimal()),
            total_value=Decimal(document["total_value"].to_decimal()),
            created_at=document["created_at"]
        )

        transactions.append(transaction)

    return transactions