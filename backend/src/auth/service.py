"""Authentication and User specific business logic"""

import uuid
import re
from typing import Union
from fastapi_users import BaseUserManager, UUIDIDMixin, InvalidPasswordException
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

    # TODO: Implement custom business logic for the UserManager

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

        Raises:
            InvalidPasswordException: If the password is invalid.
        """
        # Regex pattern search for a password with at least 1 uppercase letter, 1 digit, 1 special character and a minimum length of 8 characters
        pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{8,}$"

        if not re.match(pattern, password):
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters long, contain at least one uppercase letter, one digit and one special character"
            )

        return await super().validate_password(password, user)
