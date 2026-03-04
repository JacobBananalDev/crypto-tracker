"""
coin_price.py

Pydantic schemas for CoinPrice responses.
"""

from pydantic import BaseModel
from datetime import datetime


class CoinPriceResponse(BaseModel):

    id: int
    coin_id: int
    price_usd: float
    market_cap: float | None
    volume_24h: float | None
    timestamp: datetime

    class Config:
        from_attributes = True