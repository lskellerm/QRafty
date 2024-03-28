"""Pydantic models for the User Model, used for data validation and serialization"""

import uuid
from pydantic import Field
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    """
    Pydantic model for reading User data, used for serialization and response payloads

    Args:
        schemas (BaseUser): FastAPI_Users BaseUser Pydantic model provided as a mixin
    """

    name: str = Field(..., description="Name of the User being read", max_length=30)
    username: str = Field(..., description="User's display name", max_length=30)


class UserCreate(schemas.BaseUserCreate):
    """
    Pydantic model for creating User data, dedicated to User registration,
    consisting of mandatory password email and password field

    Args:
        schemas (BaseUserCreate): FastAPI_Users BaseUserCreate Pydantic model provided as a mixin
    """

    name: str = Field(..., description="Name of the User being created", max_length=30)
    username: str = Field(..., description="User's display name", max_length=30)


class UserUpdate(schemas.BaseUserUpdate):
    """
    Pydantic model for updating User data, used for User profile updates, containing an optional email field

    Args:
        schemas (BaseUserUpdate): FastAPI_Users BaseUserUpdate Pydantic model provided as a mixin
    """

    name: str | None = Field(
        ..., description="Name of the User being updated", max_length=30
    )
