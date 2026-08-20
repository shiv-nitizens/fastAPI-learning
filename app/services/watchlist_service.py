from uuid import uuid4
from fastapi import HTTPException

from app.models.watchlist import WatchList
from app.repositories.watchlist_repository import (
    add_watchlist as save_watchlist,
    get_watchlist_by_user_id,
    remove_from_watchlist as delete_watchlist
)


async def add_to_watchlist(data, user):

    if await watchlist_exists(user["id"], data.symbol):
        raise HTTPException(
            status_code=409,
            detail="Stock already in watchlist"
        )

    watchlist = WatchList(
        id=uuid4(),
        user_id=user["id"],
        symbol=data.symbol
    )
    await save_watchlist(watchlist)
    return watchlist


async def get_watchlist(user):
    return await get_watchlist_by_user_id(user["id"])


async def remove_from_watchlist(symbol, user):
    return await delete_watchlist(
        user["id"],
        symbol
    )