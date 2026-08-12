from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from app.models.transaction import TransactionType
from decimal import Decimal

class TransactionCreate(BaseModel):
    symbol: str
    type: TransactionType
    shares: int
    price: Decimal


class TransactionResponse(BaseModel):
    id: UUID
    symbol: str
    type: TransactionType
    shares: int
    price: Decimal
    total_value: Decimal
    created_at: datetime