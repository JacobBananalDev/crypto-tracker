"""
coin.py

CRUD operations for the Coin model.

CRUD functions interact directly with the database
using SQLAlchemy sessions.
"""

from sqlalchemy.orm import Session
from app.models.coin import Coin
from app.schemas.coin import CoinCreate


def create_coin(db: Session, coin: CoinCreate) -> Coin:
    """
    Create a new coin in the database.
    """

    db_coin = Coin(
        symbol=coin.symbol,
        name=coin.name,
        image_url=coin.image_url
    )

    db.add(db_coin)
    db.commit()
    db.refresh(db_coin)

    return db_coin


def get_coins(db: Session):
    """
    Retrieve all coins from the database.
    """
    return db.query(Coin).all()


def get_coin_by_symbol(db: Session, symbol: str):
    """
    Retrieve a single coin by its symbol.
    """
    return db.query(Coin).filter(Coin.symbol == symbol).first()