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
