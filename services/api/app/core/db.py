"""
db.py

This module is responsible for:

- Creating the database engine
- Creating session factory
- Providing a database dependency for FastAPI

We use SQLAlchemy 2.0 style.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create the SQLAlchemy engine
# The engine is the entry point to the database.
# It does NOT execute queries directly — sessions do.
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # Logs SQL queries (good for development)
)


# Create a configured "Session" class
# A session represents a database conversation.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    FastAPI dependency that provides a database session.

    It:
    - Opens a session
    - Yields it to the request
    - Closes it automatically after the request finishes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()