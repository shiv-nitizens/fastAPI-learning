from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: UUID
    email: str
    username: str
    password_hash: str
    created_at: datetime