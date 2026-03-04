"""
coins.py

API routes for Coin operations.

Routes should stay lightweight and delegate
database operations to the CRUD layer.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.coin import CoinCreate, CoinResponse
from app.crud.coin import create_coin, get_coins


router = APIRouter(prefix="/coins", tags=["Coins"])


@router.post("/", response_model=CoinResponse)
def create_coin_endpoint(
    coin: CoinCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new coin.

    Example request body:
    {
        "symbol": "BTC",
        "name": "Bitcoin",
        "image_url": "https://..."
    }
    """

    return create_coin(db, coin)


@router.get("/", response_model=list[CoinResponse])
def get_all_coins(
    db: Session = Depends(get_db)
):
    """
    Retrieve all coins from the database.
    """

    return get_coins(db)