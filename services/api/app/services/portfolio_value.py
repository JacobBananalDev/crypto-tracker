"""
portfolio_value.py

Service responsible for calculating the total value
of the user's portfolio based on the latest price data.
"""

from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.portfolio import Portfolio
from app.models.coin import Coin
from app.models.coin_price import CoinPrice


def calculate_portfolio_value(db: Session):
    """
    Calculate total portfolio value using latest coin prices.
    """

    portfolio_entries = db.query(Portfolio).all()

    assets = []
    total_value = 0

    for entry in portfolio_entries:

        # Get coin info
        coin = db.query(Coin).filter(Coin.id == entry.coin_id).first()

        # Get latest price
        price = (
            db.query(CoinPrice)
            .filter(CoinPrice.coin_id == entry.coin_id)
            .order_by(desc(CoinPrice.timestamp))
            .first()
        )

        if not price:
            continue

        value = entry.amount * price.price_usd

        assets.append(
            {
                "symbol": coin.symbol,
                "amount": entry.amount,
                "price_usd": price.price_usd,
                "value_usd": value
            }
        )

        total_value += value

    return {
        "total_value_usd": total_value,
        "assets": assets
    }