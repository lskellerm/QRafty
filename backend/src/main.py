"""Root of the application, inits the FastAPI app"""

from typing import Any
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.auth.router import auth_routers
from src.config import settings

#  Get current environment from settings, used to set visibility of OpenAPI docs
ENVIRONMENT = settings.ENVIRONMENT
SHOW_DOCS_ENVIRONMENTS = settings.SHOW_DOCS_ENVIRONMENTS

fasapi_config: dict[str, Any] = {
    "title": "QRafty API",
    "summary": "API to provide functionality for the QRafty Front-End application",
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager that starts the application and closes it when done, to be used with FastAPI lifespan events (startup and shutdown)

    Args:
        app (FastAPI): The FastAPI application

    Yields:
        Iterator[FastAPI]: The FastAPI application, which is closed after the context manager is done
    """
    yield


if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENTS:
    fasapi_config["openapi_url"] = (
        None  # sets the url for docs as null, that is to hide the swagger docs
    )


app = FastAPI(lifespan=lifespan, **fasapi_config)

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
