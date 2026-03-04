"""
portfolio.py

Pydantic schemas for portfolio-related API requests and responses.

Schemas serve as the validation and serialization layer between:
- API request bodies
- database models
- API responses

This keeps our API contracts separate from our database models,
which is a best practice in production FastAPI applications.
"""

from pydantic import BaseModel
from datetime import datetime


class PortfolioCreate(BaseModel):
    """
    Schema used when a client wants to add a coin to their portfolio.

    Example request body:

    {
        "coin_symbol": "BTC",
        "amount": 0.5
    }

    coin_symbol:
        The symbol of the cryptocurrency (BTC, SOL, XRP, etc)

    amount:
        How much of that asset the user owns
    """

    coin_symbol: str
    amount: float


class PortfolioResponse(BaseModel):
    """
    Schema returned back to the client when retrieving portfolio data.

    This schema defines exactly what fields are exposed to the API
    consumer, which prevents accidentally leaking internal database
    fields.
    """

    id: int
    coin_symbol: str
    amount: float
    created_at: datetime

    class Config:
        """
        Allows Pydantic to convert SQLAlchemy model objects
        directly into response objects.
        """
        from_attributes = True