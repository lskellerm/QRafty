from src.config import settings
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

# Get the environment variable to determine which database to use at runtime
ENV = settings.ENVIRONMENT

# Dynamically set the database URL based on the environment, allowing for configuration for various environments
SQL_ALCHEMY_DATABASE_URL = (
    settings.DEV_DATABASE_URL if ENV == "development" else settings.TEST_DATABASE_URL
)


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy databse models

    Args:
        DeclarativeBase (DeclarativeBase): Base class used for declarative class definitions
    """

    pass


# Create the async engine and the async session maker, expire_on_commit is set to False to avoid session expiration
if SQL_ALCHEMY_DATABASE_URL is not None:  # pragma: no cover
    engine = create_async_engine(SQL_ALCHEMY_DATABASE_URL)
    async_session_maker = async_sessionmaker(
        engine,
        expire_on_commit=False,
        autocommit=False,  # autocommit is set to False to allow for fine-grained control over transactions
    )


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:  # pragma: no cover
    """
    Dependency that creates a new session and then yields it

    Returns:
        AsyncGenerator[AsyncSession, None]: A fresh SQLAlchemy session to interact with the database.
    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: A new async session
    """
    async with async_session_maker() as session:
        yield session
