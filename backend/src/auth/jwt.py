"""Module containing the JWT token generation and verification functions."""

from fastapi_users.authentication import JWTStrategy
from src.auth.config import SECRET_KEY, JWT_ALGORITHM, JWT_LIFETIME_SECONDS
from src.auth.models import User
from uuid import UUID


def get_jwt_strategy() -> JWTStrategy[User, UUID]:
    """
    Utility function to create a JWTStrategy object with the correct configuration, to be used as a dependency callable
    with the fastapi_users AuthenticationBackend class

    Returns:
        JWTStrategy: A JWTStrategy object with the correct auth configuration
    """
    return JWTStrategy(
        secret=SECRET_KEY,
        lifetime_seconds=JWT_LIFETIME_SECONDS,
        algorithm=JWT_ALGORITHM,
    )
