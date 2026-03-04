"""
portfolio.py

API routes responsible for portfolio operations.

These endpoints allow clients to:
- add crypto assets to a portfolio
- retrieve portfolio holdings

The route layer should remain thin and delegate
business logic to the CRUD/service layers.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.portfolio import PortfolioCreate
from app.crud.portfolio import create_portfolio_entry, get_portfolio
from app.crud.coin import get_coin_by_symbol


router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)


@router.post("/")
def add_to_portfolio(
    data: PortfolioCreate,
    db: Session = Depends(get_db)
):
    """
    Add a cryptocurrency holding to the portfolio.

    Steps performed:
    1. Validate the coin exists
    2. Create a portfolio entry
    3. Return the stored entry

    Example request

    POST /api/v1/portfolio

    {
        "coin_symbol": "BTC",
        "amount": 0.5
    }
    """

    # Look up the coin using its symbol
    coin = get_coin_by_symbol(db, data.coin_symbol.upper())

    # If the coin does not exist, return a 404 error
    if not coin:
        raise HTTPException(
            status_code=404,
            detail="Coin not found"
        )

    # Create the portfolio entry
    entry = create_portfolio_entry(
        db,
        coin.id,
        data.amount
    )

    return entry


@router.get("/")
def get_portfolio_holdings(
    db: Session = Depends(get_db)
):
    """
    Retrieve all portfolio holdings.

    This endpoint currently returns the entire portfolio.

    In the future this will likely support:
    - user-specific portfolios
    - pagination
    - asset aggregation
    """

    return get_portfolio(db)