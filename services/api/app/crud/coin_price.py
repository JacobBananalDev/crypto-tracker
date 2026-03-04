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

def get_latest_price(db, coin_id: int):
    """
    Retrieve the most recent price for a coin.
    """

    return (
        db.query(CoinPrice)
        .filter(CoinPrice.coin_id == coin_id)
        .order_by(CoinPrice.timestamp.desc())
        .first()
    )
    
def get_price_history(db, coin_id: int):
    """
    Retrieve all stored price snapshots for a coin.
    """

    return (
        db.query(CoinPrice)
        .filter(CoinPrice.coin_id == coin_id)
        .order_by(CoinPrice.timestamp.desc())
        .all()
    )