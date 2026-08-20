from pydantic import BaseModel

class WatchListCreate(BaseModel):
    symbol: str