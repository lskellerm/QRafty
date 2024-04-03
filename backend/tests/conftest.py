"""File used to define fixtures which will be throughout the tests"""

from typing import AsyncGenerator

import pytest_asyncio

from fastapi import FastAPI
from asgi_lifespan import LifespanManager

from httpx import AsyncClient
from src.main import app as test_app


@pytest_asyncio.fixture  # type: ignore
async def app():
    """
    Fixture which creates a new FastAPI application for testing, and closes it after the tests are done,
    utilizing the asgi_lifespan LifespanManager for managing the lifespan of the application

    Yields:
        _type_: _description_
    """
    async with LifespanManager(test_app):
        print("The app is now running for testing")
        yield test_app


@pytest_asyncio.fixture  # type: ignore
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture which creates a new client for testing

    Args:
        app (FastAPI): The FastAPI application

    Returns:
        AsyncGenerator[AsyncClient, None]: The Async client for testing

    Yields:
        Iterator[AsyncGenerator[AsyncClient, None]]: The Async client for testing
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        print("Creating a new client for testing")
        yield client
