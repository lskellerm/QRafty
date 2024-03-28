"""Module for creating and configuration the fastapi_users AuthenticationBackend and BearerTransport objects."""

from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from .jwt import get_jwt_strategy  # type: ignore


# Register the Transport Scheme as a BearerTransport object with the tokenUrl set to the login endpoint
bearer_transport = BearerTransport(tokenUrl="/login")

# Create an instance of the AuthenticationBackend class with the JWTStrategy object as a dependency
auth_backend = AuthenticationBackend(  # type: ignore
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,  # type: ignore
)
