"""Root of the application, inits the FastAPI app"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.auth.router import auth_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager that starts the application and closes it when done

    Args:
        app (FastAPI): The FastAPI application

    Yields:
        Iterator[FastAPI]: The FastAPI application
    """
    yield


app = FastAPI(lifespan=lifespan)

for router in auth_routers:
    app.include_router(router, prefix="/auth", tags=["auth"])


@app.get("/")
async def root():
    """
    Root endpoint of the FastAPI application

    Returns:
        dict: A simple dictionary
    """
    return {"message": "Hello World"}
