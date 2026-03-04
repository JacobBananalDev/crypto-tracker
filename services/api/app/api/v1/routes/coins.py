"""
coins.py

API routes for Coin operations.

Routes should stay lightweight and delegate
database operations to the CRUD layer.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.coin import CoinCreate, CoinResponse
from app.crud.coin import create_coin, get_coins, get_coin_by_symbol
from app.services.coingecko import fetch_coin_price
from app.schemas.coin_price import CoinPriceResponse
from app.crud.coin_price import create_coin_price, get_latest_price, get_price_history

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

@router.get("/{symbol}", response_model=CoinResponse)
def get_coin(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve a coin by its symbol.

    Example:
    /api/v1/coins/BTC
    """

    coin = get_coin_by_symbol(db, symbol.upper())

    if coin is None:
        raise HTTPException(
            status_code=404,
            detail="Coin not found"
        )

    return coin

@router.post("/{symbol}/price")
def fetch_and_store_price(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Fetch latest price from CoinGecko and store it.
    """

    coin = get_coin_by_symbol(db, symbol.upper())

    if not coin:
        raise HTTPException(status_code=404, detail="Coin not found")

    price_data = fetch_coin_price(coin.name.lower())

    if not price_data:
        raise HTTPException(status_code=400, detail="Price data not found")

    price = create_coin_price(
        db,
        coin_id=coin.id,
        price_usd=price_data["usd"],
        market_cap=price_data.get("usd_market_cap"),
        volume_24h=price_data.get("usd_24h_vol")
    )

    return price

@router.get("/{symbol}/price", response_model=CoinPriceResponse)
def get_coin_price(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve the latest stored price for a coin.
    """

    coin = get_coin_by_symbol(db, symbol.upper())

    if not coin:
        raise HTTPException(status_code=404, detail="Coin not found")

    price = get_latest_price(db, coin.id)

    if not price:
        raise HTTPException(status_code=404, detail="No price data available")

    return price

@router.get("/{symbol}/history", response_model=list[CoinPriceResponse])
def get_coin_price_history(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve historical prices for a coin.
    """

    coin = get_coin_by_symbol(db, symbol.upper())

    if not coin:
        raise HTTPException(status_code=404, detail="Coin not found")

    return get_price_history(db, coin.id)