"""
coin_price.py

CRUD operations for storing coin price snapshots.
"""

from sqlalchemy.orm import Session
from app.models.coin_price import CoinPrice


def create_coin_price(
    db: Session,
    coin_id: int,
    price_usd: float,
    market_cap: float,
    volume_24h: float
):
    """
    Insert a new price snapshot for a coin.
    """

    price = CoinPrice(
        coin_id=coin_id,
        price_usd=price_usd,
        market_cap=market_cap,
        volume_24h=volume_24h
    )

    db.add(price)
    db.commit()
    db.refresh(price)

    return price