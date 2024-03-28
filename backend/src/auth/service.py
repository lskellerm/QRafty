"""Authentication and User specific business logic"""

import uuid
from fastapi_users import BaseUserManager, UUIDIDMixin
from .models import User
from .config import SECRET


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    UserManager class containing the core logic for handling common user operations, inheriting
    paramaters and logic from the fastapi_users BaseUserManager class

    Args:
        UUIDIDMixin (UUIDIDMixin): Mixin class for the User model, containing the UUID ID field
        BaseUserManager (BaseUserManager): BaseUserManager class from fastapi_users
    """

    reset_pasword_token_secret = SECRET
    verification_token_secret = SECRET

    # TODO: Implement custom business logic for the UserManager
