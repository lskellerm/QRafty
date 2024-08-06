"""Testing authentication endpoints"""

import pytest

from pytest import MonkeyPatch  # imported for type hinting
from typing import Dict

from fastapi import status
from httpx import AsyncClient, Response

from tests.auth.mocks import MockedUserManager


@pytest.mark.asyncio
class TestRegistration:
    """Test class for the registration endpoint, /auth/register,
    testing various scenarios and edge cases.
    """

    async def test_registration_success(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when a user is successfully registered."""
        print("Testing the registration endpoint with valid data")
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

    async def test_registration_missing_username(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the username is missing."""
        print("Testing the registration endpoint with missing username")
        del base_registration_payload["username"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    async def test_registration_missing_name(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the name is missing."""
        print("Testing the registration endpoint with missing name")
        del base_registration_payload["name"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    async def test_registration_missing_email(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the email is missing."""
        print("Testing the registration endpoint with missing email")
        del base_registration_payload["email"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    async def test_registration_missing_password(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the password is missing."""
        print("Testing the registration endpoint with missing password")
        del base_registration_payload["password"]
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert response.json()["detail"][0]["msg"] == "Field required"
        print("Test passed successfully!")

    async def test_registration_invalid_email(
        self, client: AsyncClient, base_registration_payload: Dict[str, str]
    ) -> None:
        """Test the registration endpoint when the email is invalid, either not containing an @-sign or nothing after or before it"""
        print("Testing the registration endpoint with invalid email")
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

    async def test_registration_short_password(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        invalid_password_message: str,
    ) -> None:
        """Test the registration endpoint when the password is too short."""
        print("Testing the registration endpoint with a password that is too short")
        base_registration_payload["password"] = "Short1!"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        print(response.json())
        assert response.json()["detail"]["reason"] == invalid_password_message
        print("Test passed successfully!")

    async def test_register_invalid_password_no_uppercase(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        invalid_password_message: str,
    ) -> None:
        """Test the registration endpoint when the password does not contain an uppercase letter."""
        print(
            "Testing the registration endpoint with a password that does not contain an uppercase letter"
        )
        base_registration_payload["password"] = "password123!"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"]["reason"] == invalid_password_message
        print("Test passed successfully!")

    async def test_register_invalid_password_no_digit(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        invalid_password_message: str,
    ) -> None:
        """Test the registration endpoint when the password does not contain a digit."""
        print(
            "Testing the registration endpoint with a password that does not contain a digit"
        )
        base_registration_payload["password"] = "Password!"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"]["reason"] == invalid_password_message
        print("Test passed successfully!")

    async def test_register_invalid_password_no_special_character(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        invalid_password_message: str,
    ) -> None:
        """Test the registration endpoint when the password does not contain a special character."""
        print(
            "Testing the registration endpoint with a password that does not contain a special character"
        )
        base_registration_payload["password"] = "Password1"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"]["reason"] == invalid_password_message
        print("Test passed successfully!")

    async def test_register_invalid_password_contains_username(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        invalid_password_contains_pii_info_message: str,
    ) -> None:
        """Test the registration endpoint when the password contains the username."""
        print(
            "Testing the registration endpoint with a password that contains the username"
        )
        base_registration_payload["password"] = "Testuser1!123"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            response.json()["detail"]["reason"]
            == invalid_password_contains_pii_info_message
        )
        print("Test passed successfully!")

    async def test_register_invalid_password_contains_email(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        invalid_password_contains_pii_info_message: str,
    ) -> None:
        """Test the registration endpoint when the password contains the email."""
        print(
            "Testing the registration endpoint with a password that contains the emai;"
        )
        base_registration_payload["password"] = "Meuser@example.com1233!"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            response.json()["detail"]["reason"]
            == invalid_password_contains_pii_info_message
        )

        print("Test passed successfully!")

    async def test_register_invalid_password_contains_name(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        invalid_password_contains_pii_info_message: str,
    ) -> None:
        """Test the registration endpoint when the password contains the name."""
        print(
            "Testing the registration endpoint with a password that contains the name"
        )
        base_registration_payload["password"] = "Test User1!123"
        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            response.json()["detail"]["reason"]
            == invalid_password_contains_pii_info_message
        )

        print("Test passed successfully")

    async def test_register_duplicate_email(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        monkeypatch: MonkeyPatch,
    ) -> None:
        """Test the registration endpoint when the email is already in use."""
        print("Testing the registration endpoint with a duplicate email")

        user_manager = MockedUserManager(user_exists=False, email_exists=True)

        # Mock the get_by_email method to return a user with the same email
        monkeypatch.setattr(
            "src.auth.dependencies.CustomSQLAlchemyUserDatabase.get_by_email",
            user_manager.get_by_email,
        )

        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"] == "REGISTER_USER_ALREADY_EXISTS"

    print("Test passed successfully!")

    async def test_register_duplicate_username(
        self,
        client: AsyncClient,
        base_registration_payload: Dict[str, str],
        monkeypatch: MonkeyPatch,
    ) -> None:
        """Test the registration endpoint when the username is already in use."""
        print("Testing the registration endpoint with a duplicate username")

        user_manager = MockedUserManager(user_exists=True, email_exists=False)

        # Mock the get_by_username method to return a user with the same username
        monkeypatch.setattr(
            "src.auth.dependencies.CustomSQLAlchemyUserDatabase.get_by_username",
            user_manager.get_by_username,
        )

        response: Response = await client.post(
            "/auth/register",
            json=base_registration_payload,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"] == "Username already exists"
