"""Auth domain level fixtures used throughout authencation unit & integration tests"""

import pytest


@pytest.fixture(scope="function")
def base_registration_payload():
    """
    Provides a base valid registration payload for usage across different tests
    """
    return {
        "username": "testuser",
        "email": "user@example.com",
        "password": "TestPassword1!",
        "name": "Test User",
    }


@pytest.fixture(scope="module")
def invalid_password_message():
    """
    Provides a base invalid password message for usage across different tests, removing the need to hardcode the message in each test
    """
    return "Password should be at least 8 characters long, contain at least one uppercase letter, one digit and one special character"


@pytest.fixture(scope="module")
def invalid_password_contains_pii_info_message():
    """
    Provides a base invalid password message for usage across different tests, removing the need to hardcode the message in each test
    """
    return (
        "Password should not contain your email, username or name for security reasons"
    )
