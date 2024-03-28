from .config import settings
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


SQL_ALCHEMY_DATABASE_URL = settings.DEV_DATABASE_URL


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy databse models

    Args:
        DeclarativeBase (DeclarativeBase): Base class used for declarative class definitions
    """

    pass


# Create the async engine and the async session maker, expire_on_commit is set to False to avoid session expiration
engine = create_async_engine(SQL_ALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that creates a new session and then yields it

    Returns:
        AsyncGenerator[AsyncSession, None]: A fresh SQLAlchemy session to interact with the database

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: A new async session
    """
    async with async_session_maker() as session:
        yield session
