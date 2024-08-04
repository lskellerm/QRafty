"""Testing authentication endpoints"""

import pytest
from typing import Dict
from fastapi import status
from httpx import AsyncClient, Response


@pytest.mark.asyncio
class TestRegistration:
    """Test class for the registration endpoint, /auth/register,
    testing various scenarios and edge cases.
    """

    @pytest.mark.asyncio
    async def test_registration_success(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when a user is successfully registered."""
        print("Testing the registration endpoint with valid data``")
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["username"] == "testuser"
        assert "id" in response.json()
        assert "password" not in response.json()
        assert response.json()["is_active"] is True
        assert response.json()["is_superuser"] is False
        assert response.json()["name"] == "Test User"
        print("Test passed successfully!")

    @pytest.mark.asyncio
    async def test_registration_missing_username(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the username is missing."""
        print("Testing the registration endpoint with missing username``")
        del base_registration_payload["username"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    @pytest.mark.asyncio
    async def test_registration_missing_name(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the name is missing."""
        print("Testing the registration endpoint with missing name``")
        del base_registration_payload["name"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    @pytest.mark.asyncio
    async def test_registration_missing_email(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the email is missing."""
        print("Testing the registration endpoint with missing email``")
        del base_registration_payload["email"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    @pytest.mark.asyncio
    async def test_registration_missing_password(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the password is missing."""
        print("Testing the registration endpoint with missing password``")
        del base_registration_payload["password"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    @pytest.mark.asyncio
    async def test_registration_invalid_email(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the email is invalid, either not containing an @-sign or nothing after or before it"""
        print("Testing the registration endpoint with invalid email``")
        base_registration_payload["email"] = "invalidemail"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"][0]["msg"]
            == "value is not a valid email address: The email address is not valid. It must have exactly one @-sign."
        )

        base_registration_payload["email"] = "dsfasdf@gmail"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"][0]["msg"]
            == "value is not a valid email address: The part after the @-sign is not valid. It should have a period."
        )

        base_registration_payload["email"] = "@gmail.com"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"][0]["msg"]
            == "value is not a valid email address: There must be something before the @-sign."
        )

        base_registration_payload["email"] = "testuser@"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert (
            response.json()["detail"][0]["msg"]
            == "value is not a valid email address: There must be something after the @-sign."
        )

        print("Test passed successfully!")
