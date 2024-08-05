"""Mocks for the auth module."""

from typing import Dict, Any


class MockedUserManager:
    """Class to mock the FastAPI UserManager class from the auth service"""

    def __init__(self, user_exists: bool = False, email_exists: bool = False) -> None:
        self.user_exists: bool = user_exists
        self.email_exists: bool = email_exists

    async def get_by_username(self, username: str) -> Dict[str, Any] | None:
        """
        Function to simulate getting an existing user by their username, flag set by the user_exists attribute.

        Args:
            username (str): The username of the user to retrieve

        Returns:
            Dict[str, Any]: Response dictionary with the username if the user exists, otherwise an empty dictionary
        """
        if self.user_exists:
            return {
                "name": "Test User",
                "username": username,
                "email": "user@example.com",
            }
        return None

    async def get_by_email(self, email: str) -> Dict[str, Any] | None:
        """
        Function to simulate getting an existing user by their email, flag set by the email_exists attribute.

        Args:
            email (str): The email of the user to retrieve

        Returns:
            Dict[str, Any]: Response dictionary with the email if the user exists, otherwise an empty dictionary
        """
        if self.email_exists:
            return {
                "name": "Test User",
                "username": "testuser",
                "email": email,
            }
        return None
