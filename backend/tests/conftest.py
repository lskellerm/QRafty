"""Common fixtures which will be throughout the tests"""

from typing import AsyncGenerator

import pytest_asyncio

from fastapi import FastAPI
from asgi_lifespan import LifespanManager

from httpx import ASGITransport, AsyncClient

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
    AsyncTransaction,
)

from src.main import app as test_app
from src.config import settings
from src.database import get_async_session

TEST_DATABASE_URL = settings.TEST_DATABASE_URL


@pytest_asyncio.fixture(scope="session")  # type: ignore
async def async_db_engine() -> AsyncGenerator[AsyncEngine, None]:
    """
    Fixture which creates a new async database engine for testing

    Returns:
        AsyncGenerator[AsyncSession, None]: The newly created database engine

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]: New database engine for testing, yielded to the tests after the scope of the session
    """
    engine = create_async_engine(TEST_DATABASE_URL)

    if not engine:
        raise Exception("Engine not created")
    yield engine


@pytest_asyncio.fixture(scope="function")  # type: ignore
async def async_db_session(
    async_db_engine: AsyncEngine,
) -> AsyncGenerator[AsyncSession, None]:
    """
    Fixture which creates a new database session for testing, binding the session to an existing transaction,
    ensuring that the session is rolled back after each test is completed.

    Returns:
        AsyncGenerator[AsyncClient, None]: The Async database session for testing

    Yields:
        Iterator[AsyncGenerator[AsyncClient, None]]: The Async database session for testing
    """
    async with async_db_engine.connect() as connection:
        # Start a new non-ORM transaction
        transaction: AsyncTransaction = await connection.begin()

        try:
            # Bind a new AsyncSession to the newly created AsyncTransaction
            async_session = async_sessionmaker(
                bind=connection, expire_on_commit=False, class_=AsyncSession
            )

            # Yield the new AsyncSession to the tests
            async with async_session() as session:
                yield session

                # Rollback any changes made within the same transaction context after the tests finish
                await transaction.rollback()

        except Exception as e:
            # Rollback any changes made within the same transaction context if an exception occurs, ensuring transactions are rolled back regardless
            await transaction.rollback()
            raise e

        # Close the transaction after the tests are done
        finally:
            await transaction.close()


@pytest_asyncio.fixture(scope="session")  # type: ignore
async def app() -> AsyncGenerator[FastAPI, None]:
    """
    Fixture which creates a new FastAPI application for testing, and closes it after the tests are done,
    utilizing the asgi_lifespan LifespanManager for managing the lifespan of the application

    Yields:
        test_app: FastAPI application for testing
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

    Returns:
        AsyncGenerator[AsyncClient, None]: The Async client for testing

    Yields:
        Iterator[AsyncGenerator[AsyncClient, None]]: The Async client for testing
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
