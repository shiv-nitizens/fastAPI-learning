from app.database.mongodb import db
from bson.decimal128 import Decimal128

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