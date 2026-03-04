"""
price_updater.py

Background service that periodically fetches
crypto prices and stores them in the database.
"""

import time
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.crud.coin import get_coins
from app.crud.coin_price import create_coin_price
from app.services.coingecko import fetch_prices_batch


def update_prices():
    """
    Background loop that updates prices every minute.
    """

    while True:

        db = SessionLocal()

        try:

            coins = get_coins(db)

            if not coins:
                continue

            coin_ids = [coin.name.lower() for coin in coins]

            try:
                price_data = fetch_prices_batch(coin_ids)
            except Exception as e:
                print(f"[PRICE WORKER] Error: {e}")
                time.sleep(60)
                continue
            
            for coin in coins:

                data = price_data.get(coin.name.lower())

                if not data:
                    continue

                create_coin_price(
                    db,
                    coin_id=coin.id,
                    price_usd=data["usd"],
                    market_cap=data.get("usd_market_cap"),
                    volume_24h=data.get("usd_24h_vol")
                )

                print(f"[PRICE WORKER] Updated {coin.symbol}")

        finally:
            db.close()

        # Wait 120 seconds before next update
        time.sleep(120)