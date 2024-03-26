from .config import settings
from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.orm import DeclarativeBase


SQL_ALCHEMY_DATABASE_URL = settings.DATABASE_URL

class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTableUUID, Base):
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

async def get_user_db(session: AsyncSession = Depends(get_async_session)): # type: ignore 
    """
    Dependency that creates the SQLAlchemy databse adapter for the User Model

    Args:
        session (AsyncSession, optional): session instance, injected by the get_async_session dependency. Defaults to Depends(get_async_session).

    Yields:
        SQLAlchemyUserDatabase: User database adapter for SQLAlchemy, provided by fastapi_users
    """
    yield SQLAlchemyUserDatabase(session, User)
