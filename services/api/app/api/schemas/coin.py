"""
coin.py

Defines the Pydantic schemas for Coin.

Schemas control:
- request validation
- response serialization
- API contracts
"""

from pydantic import BaseModel
from datetime import datetime


class CoinBase(BaseModel):
    """
    Shared properties for Coin objects.
    """
    symbol: str
    name: str
    image_url: str | None = None


class CoinCreate(CoinBase):
    """
    Schema used when creating a new coin.
    """
    pass


class CoinResponse(CoinBase):
    """
    Schema returned by the API when reading coins.
    """
    id: int
    created_at: datetime

    class Config:
        from_attributes = True