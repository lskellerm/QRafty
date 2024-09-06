"""Core endpoints for authentication and authorization, also includes FastAPIUsers object configuration."""

from uuid import UUID

from fastapi import APIRouter, status
from fastapi_users import FastAPIUsers
from fastapi_users.router.common import ErrorCode

from src.auth.dependencies import get_user_manager
from src.auth.authentication import auth_backend
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead
from src.auth.constants import AuthErrorCode


# List of routers for the auth endpoints
auth_routers: list[APIRouter] = []

# Configure the FastAPIUsers custom wrapper object with the UserManager and the AuthenticationBackend objects
fastapi_users = FastAPIUsers[User, UUID](
    get_user_manager,
    [auth_backend],
)


# Register the FastAPIUsers register router with the UserRead and UserCreate schemas
register_router = fastapi_users.get_register_router(UserRead, UserCreate)

# Change the password validation error message of the register endpoint
register_router.routes[0].responses[status.HTTP_400_BAD_REQUEST]["content"][  # type: ignore
    "application/json"
]["examples"][ErrorCode.REGISTER_INVALID_PASSWORD]["value"]["detail"][
    "reason"
] = "Password should be at least 8 characters long, contain at least one uppercase letter, one digit and one special character"

# Add a new response example for the case when the user already exists with the provided username
register_router.routes[0].responses[status.HTTP_400_BAD_REQUEST]["content"][  # type: ignore
    "application/json"
]["examples"][AuthErrorCode.REGISTER_USERNAME_ALREADY_EXISTS] = {
    "summary": "A user with this username already exists.",
    "value": {
        "detail": {
            "code": AuthErrorCode.REGISTER_USERNAME_ALREADY_EXISTS,
            "reason": "A user  with this username already exists, please choose another username",
        }
    },
}

# Add a new response example for the case when the user's password contains their email, username, or name
register_router.routes[0].responses[status.HTTP_400_BAD_REQUEST]["content"][  # type: ignore
    "application/json"
]["examples"][AuthErrorCode.REGISTER_INVALID_PASSWORD_CONTAINS_USER_INFO] = {
    "summary": "Password validation failed, contains user information",
    "value": {
        "detail": {
            "code": AuthErrorCode.REGISTER_INVALID_PASSWORD_CONTAINS_USER_INFO,
            "reason": "Password should not contain your email, username or name for security reasons",
        }
    },
}

# Change the path operation name for the register endpoint, to better integrate with the OpenAPI spec client code generation
register_router.routes[0].name = "register"  # type: ignore


# Append all auth related routes to to the list of auth routers, used to then append them to the main FastAPI app routes
auth_routers.append(register_router)
