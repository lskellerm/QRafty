"""Root of the application, inits the FastAPI app"""

from typing import Any
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import auth_routers
from src.config import settings

#  Get current environment from settings, used to set visibility of OpenAPI docs
ENVIRONMENT = settings.ENVIRONMENT
SHOW_DOCS_ENVIRONMENTS = settings.SHOW_DOCS_ENVIRONMENTS

# Get the app name and list of allowed origins from the app settings
APP_NAME = settings.APP_NAME
if settings.ALLOWED_ORIGINS:
    origins = settings.ALLOWED_ORIGINS.split(",")


def custom_generate_uniq_id(route: APIRoute) -> str:
    """
    Custom function to generate unique ids for each endpoint of the application.

    Used for the OpenAPI specs to provide clearer and more readable ids for each endpoint, which will
    be used when generating TypeScript cleint for the Front-End application.

    Args:
        route (APIRoute): The APIRoute object
    Returns:
        str: Unique string id for the endpoint
    """
    return f"{route.tags[0]}-{route.name}"


# Create dictionary for basic FastAPI configuration
fastapi_config: dict[str, Any] = {
    "title": "QRafty API",
    "summary": "API to provide functionality for the QRafty Front-End application",
    "description": "QRafty API helps to manage and create QR codes, allowing the user to create, edit and delete fully custom QR codes.",
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


# If the current environment is not in the list of environments where the docs should be shown, hide the swagger docs
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENTS:
    fastapi_config["openapi_url"] = (
        None  # sets the url for docs as null, that is to hide the swagger docs
    )

# Create the instance of the FastAPI application, with custom lifespan and unique id generator, dumping the configuration
app = FastAPI(
    lifespan=lifespan,
    generate_unique_id_function=custom_generate_uniq_id,
    **fastapi_config,
)


# Add the CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # type: ignore
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the auth routers in the FastAPI application
for router in auth_routers:
    app.include_router(router, prefix="/auth", tags=["auth"])
