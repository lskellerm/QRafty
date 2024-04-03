"""Basic sanity test for the FastAPI application."""

import pytest
from httpx import AsyncClient, Response


@pytest.mark.asyncio
async def test_home(client: AsyncClient) -> None:
    """
    Basic sanity test for the FastAPI application, ensuring test setup is correct.

    Args:
        client (AsyncClient): httpx AsyncClient for testing the FastAPI application

    Returns: None
    """
    print("Testing the root endpoint of the FastAPI application")
    response: Response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    print("Test passed successfully!")
