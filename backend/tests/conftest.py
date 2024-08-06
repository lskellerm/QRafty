"""Common fixtures which will be throughout the tests"""

from typing import AsyncGenerator

import pytest_asyncio

from fastapi import FastAPI
from asgi_lifespan import LifespanManager

from httpx import ASGITransport, AsyncClient

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)

from src.main import app as test_app
from src.config import settings
from src.database import get_async_session

TEST_DATABASE_URL = settings.TEST_DATABASE_URL


@pytest_asyncio.fixture(scope="session")  # type: ignore
async def async_db_engine() -> AsyncGenerator[AsyncEngine, None]:
    """
    Fixture which creates a new async database engine for testing

    Yields:
        Iterator[AsyncGenerator[AsyncEngine, None]]: New database engine for testing, to be bounded to the async session used by tests
    """
    # poolclass is set to NullPool to allow for multiple event loops (asyncio and pytest-asyncio) to share the same AsyncEngine
    # see https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#using-multiple-asyncio-event-loops
    engine = create_async_engine(TEST_DATABASE_URL, poolclass=NullPool)
    yield engine


@pytest_asyncio.fixture(scope="function")  # type: ignore
async def async_db_session(
    async_db_engine: AsyncEngine,
) -> AsyncGenerator[AsyncSession, None]:
    """
    Fixture which creates a new database session for testing, binding the session to the async database engine,
    and starting a new transaction for each test, ensuring that the database is in a clean state for each test.

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: The Async database session to be used by each unit test, explcitly starting a new transaction and rolling it back after each test
    """
    # Start an asnyc connection with the database engine
    async with async_db_engine.connect() as connection:
        # Begin a new transaction for each test, which ensures that each test is isolated from the others
        transaction = await connection.begin()

        # Create the async session to be yielded to the tests, binding it to the connection
        async_session = async_sessionmaker(
            bind=connection, expire_on_commit=False, class_=AsyncSession
        )

        async with async_session() as session:
            yield session

            # Finally, rollback the transaction that was started for the each test
            await transaction.rollback()


@pytest_asyncio.fixture(scope="session")  # type: ignore
async def app() -> AsyncGenerator[FastAPI, None]:
    """
    Fixture which creates a new FastAPI application for testing, and closes it after the tests are done,
    utilizing the asgi_lifespan LifespanManager for managing the lifespan of the application

    Yields:
        test_app: FastAPI application for testing, using the LifespanManager to manage the lifespan of the application, ensuring that the event loop is closed after the tests are done
    """
    async with LifespanManager(test_app):
        print("The app is now running for testing")
        yield test_app

    print("The app is now closed after testing")


@pytest_asyncio.fixture(scope="function")  # type: ignore
async def client(
    app: FastAPI, async_db_session: AsyncSession
) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture which creates a new client for testing

    Args:
        app (FastAPI): The FastAPI application

    Yields:
        Iterator[AsyncGenerator[AsyncClient, None]]: The Async client to be used for making asynchronous requests in unit tests
    """
    # Override the get_async_session dependency with the db_session fixture
    test_app.dependency_overrides[get_async_session] = lambda: async_db_session

    async with AsyncClient(
        transport=ASGITransport(app=app),  # type: ignore
        base_url="http://test",
    ) as client:
        print("Creating a new client for testing")
        yield client

    # Remove the dependency override after the tests are done
    test_app.dependency_overrides = {}
