from app.database.mongodb import db
from app.models.watchlist import WatchList

async def add_watchlist(data):
    document = {
        "id": data.id,
        "user_id": data.user_id,
        "symbol": data.symbol
    }
    result = await db.watchlist.insert_one(document)
    return result.inserted_id

async def get_watchlist_by_user_id(user_id):
    cursor = db.watchlist.find({
        "user_id": user_id
    })

    documents = await cursor.to_list(length=None)

    watchlists = []

    for document in documents:
        watchlist = WatchList(
            id=document["id"],
            user_id=document["user_id"],
            symbol=document["symbol"]
        )

        watchlists.append(watchlist)

    return watchlists

async def remove_from_watchlist(user_id, symbol):
    result = await db.watchlist.delete_one({
        "user_id": user_id,
        "symbol": symbol
    })

    return result.deleted_count

async def watchlist_exists(user_id, symbol):
    document = await db.watchlist.find_one({
        "user_id": user_id,
        "symbol": symbol
    })

    return document is not None

