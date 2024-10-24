"""Custom exceptions for the auth module"""

from fastapi_users.exceptions import FastAPIUsersException


class UserDoesNotExist(FastAPIUsersException):
    """Raised when a user does not exist in the database"""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)
