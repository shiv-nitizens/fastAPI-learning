from fastapi import APIRouter, Depends, status

from app.schemas.watchlist import WatchListCreate
from app.services.watchlist_service import (
    add_to_watchlist,
    get_watchlist,
    remove_from_watchlist
)
from app.security.auth import get_current_user

router = APIRouter(
    prefix="/watchlist",
    tags=["Watchlist"]
)

@router.post("", status_code=status.HTTP_201_CREATED)
async def add_watchlist_endpoint(
    data: WatchListCreate,
    user=Depends(get_current_user)
):
    return await add_to_watchlist(data, user)


@router.get("")
async def get_watchlist_endpoint(
    user=Depends(get_current_user)
):
    return await get_watchlist(user)


@router.delete("/{symbol}")
async def remove_watchlist_endpoint(
    symbol: str,
    user=Depends(get_current_user)
):
    return await remove_from_watchlist(symbol, user)