from uuid import UUID

class WatchList:
    def __init__(
        self,
        id: UUID,
        user_id: UUID,
        symbol: str
    ):
        self.id = id
        self.user_id = user_id
        self.symbol = symbol