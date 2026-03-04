"""
portfolio.py

CRUD operations for portfolio data.

The CRUD layer is responsible for:
- communicating with the database
- performing queries
- returning ORM objects

Why separate CRUD from routes?

Routes handle:
    HTTP requests and responses

CRUD handles:
    database logic

This separation improves maintainability and testability.
"""

from sqlalchemy.orm import Session
from app.models.portfolio import Portfolio


def create_portfolio_entry(db: Session, coin_id: int, amount: float):
    """
    Create a new portfolio entry.

    Parameters
    ----------
    db : Session
        Active SQLAlchemy database session

    coin_id : int
        Foreign key referencing the coin in the coins table

    amount : float
        Amount of the asset the user owns

    Returns
    -------
    Portfolio
        The newly created portfolio entry
    """

    entry = Portfolio(
        coin_id=coin_id,
        amount=amount
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return entry


def get_portfolio(db: Session):
    """
    Retrieve all portfolio entries.

    In the future this will likely be filtered by user_id once
    authentication is added.

    Parameters
    ----------
    db : Session
        Active database session

    Returns
    -------
    List[Portfolio]
        All portfolio entries stored in the database
    """

    return db.query(Portfolio).all()