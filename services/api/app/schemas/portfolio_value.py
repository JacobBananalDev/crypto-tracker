"""
portfolio_value.py

Schemas used for portfolio valuation responses.
"""

from pydantic import BaseModel
from typing import List


class PortfolioAssetValue(BaseModel):
    """
    Represents the value of a single asset in the portfolio.
    """

    symbol: str
    amount: float
    price_usd: float
    value_usd: float


class PortfolioValueResponse(BaseModel):
    """
    Represents the total portfolio valuation.
    """

    total_value_usd: float
    assets: List[PortfolioAssetValue]