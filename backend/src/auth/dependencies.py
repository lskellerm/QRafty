"""Authentication and User Management specific dependencies"""

from typing import Annotated
from uuid import UUID


from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database import get_async_session
from src.auth.models import User
from src.auth.service import UserManager


class CustomSQLAlchemyUserDatabase(SQLAlchemyUserDatabase[User, UUID]):
    """
    Custom User Database adapter for SQLAlchemy, extending the SQLAlchemyUserDatabase class from fastapi_users
    for custom user operations:
        - get_by_username: Get a user by their username

    Args:
        SQLAlchemyUserDatabase (SQLAlchemyUserDatabase): Base class for the User Database adapter
    """

    async def get_by_username(self, username: str) -> User | None:
        statement = select(self.user_table).where(self.user_table.username == username)
        return await self._get_user(statement)  # type: ignore


async def get_user_db(
    async_session: Annotated[AsyncSession, Depends(get_async_session)],
):
    """
    Dependency that creates the SQLAlchemy database adapter for the User Model (comes from fastapi_users)

    Args:
        session (AsyncSession, optional): session instance, injected by the get_async_session dependency. Defaults to Depends(get_async_session).

    Yields:
        SQLAlchemyUserDatabase: UserDatabase instance for SQLAlchemy, adapter provided by fastapi_users
    """
    yield CustomSQLAlchemyUserDatabase(async_session, User)


async def get_user_manager(
    user_db: Annotated[SQLAlchemyUserDatabase[User, UUID], Depends(get_user_db)],
):
    """
    Dependency that creates the UserManager instance for the User model, which will later be injected at runtime

    Args:
        user_db (SQLAlchemyUserDatabase[User], optional): User database adapter, injected by the get_user_db dependency. Defaults to Depends(get_user_db).

    Yields:
    """
    yield UserManager(user_db)
