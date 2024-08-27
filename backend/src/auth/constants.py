"""Auth specific constants and error codes"""

from enum import Enum


# Error codes for the auth endpoints
class AuthErrorCode(str, Enum):
    REGISTER_USERNAME_ALREADY_EXISTS = "REGISTER_USERNAME_ALREADY_EXISTS"
