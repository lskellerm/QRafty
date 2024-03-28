"""Authentication and User Management specific dependencies"""

from typing import Annotated
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from .models import User
from .service import UserManager


async def get_user_db(  # type: ignore
    async_session: Annotated[AsyncSession, Depends(get_async_session)],
):
    """
    Dependency that creates the SQLAlchemy database adapter for the User Model (comes from fastapi_users)

    Args:
        session (AsyncSession, optional): session instance, injected by the get_async_session dependency. Defaults to Depends(get_async_session).

    Yields:
        SQLAlchemyUserDatabase: User database adapter for SQLAlchemy, provided by fastapi_users
    """
    yield SQLAlchemyUserDatabase(async_session, User)


async def get_user_manager(
    user_db: Annotated[SQLAlchemyUserDatabase[User], Depends(get_user_db)],  # type: ignore
):
    """
    Dependency that creates the UserManager instance for the User model, which will later be injecteed at runtime

    Args:
        user_db (SQLAlchemyUserDatabase[User], optional): User database adapter, injected by the get_user_db dependency. Defaults to Depends(get_user_db).

    Yields:
        UserManager: UserManager instance for the User model
    """
    yield UserManager(user_db)  # type: ignore
