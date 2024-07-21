"""Authentication and User specific business logic"""

import uuid
import re
from typing import Annotated, Union, Optional

from fastapi import HTTPException, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, InvalidPasswordException
from fastapi_users import schemas  # imported for type hinting


from src.auth.models import User
from src.auth.schemas import UserCreate
from src.auth.config import SECRET_KEY


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    UserManager class containing the core logic for handling common user operations, inheriting
    paramaters and logic from the fastapi_users BaseUserManager class

    Args:
        UUIDIDMixin (UUIDIDMixin): Mixin class for the User model, containing the UUID ID field
        BaseUserManager (BaseUserManager): BaseUserManager class from fastapi_users
    """

    reset_pasword_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def validate_password(  # type: ignore
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        """
        Validate the password for a user.

        Args:
            password (str): Password to validate
            user (User): User object to validate the password against

        Returns: None, if the password is valid

        Raises:
            InvalidPasswordException: If the password is invalid.
        """
        # Regex pattern search for a password with at least 1 uppercase letter, 1 digit, 1 special character and a minimum length of 8 characters
        pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{8,}$"

        if not re.match(pattern, password):
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters long, contain at least one uppercase letter, one digit and one special character"
            )

        # Check that the User's password does not contain their email, username, or name
        if any(
            keyword.lower() in password.lower()
            for keyword in [user.email, user.username, user.name]
        ):
            raise InvalidPasswordException(
                reason="Password should not contain your email, username or name for security reasons"
            )

    async def create(
        self,
        user_create: Annotated[schemas.UC, "UserCreate schema for FastAPIUsers"],
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> User:
        """
        Create a new user in the database.

        Args:
            user_create (UserCreate): UserCreate object with the user's data
            safe (bool, optional): Whether to create the user safely. Defaults to False.

        Returns:
            User: User object for the created user
        """
        existing_user = await self.user_db.get_by_username(user_create.username)  # type: ignore

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username already exists",
            )

        return await super().create(user_create, safe=safe, request=request)

    # TODO: Implement the remainder of custom User business logic for the UserManager
