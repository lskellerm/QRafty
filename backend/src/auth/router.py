"""Core endpoints for authentication and authorization, also includes FastAPIUsers object configuration."""

import uuid
from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from src.auth.dependencies import get_user_manager  # type: ignore
from src.auth.authentication import auth_backend  # type: ignore
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead


# List of routers for the auth endpoints
auth_routers: list[APIRouter] = []

# Configure the FastAPIUsers object with the UserManager and the AuthenticationBackend objects
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,  # type: ignore
    [auth_backend],
)


# Register and append all auth routes to the routers list
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
auth_routers.append(register_router)
