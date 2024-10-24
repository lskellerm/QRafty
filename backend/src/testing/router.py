"""Contains route endpoints only avaiable in the testing environment."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status

from src.auth.dependencies import get_user_manager
from src.auth.service import UserManager

from src.testing.exceptions import UserDoesNotExist
from src.testing.constants import TestingErrorCode, ErrorModel


router = APIRouter(prefix="/testing", tags=["testing"])


@router.delete(
    "/users/{username}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="user:delete",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorModel,
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "summary": "User attempted to be deleted was not found",
                    "value": {
                        "detail": {
                            "code": TestingErrorCode.USER_NOT_FOUND,
                            "reason": "User not found",
                        }
                    },
                }
            },
        }
    },
)
async def delete_by_username(
    request: Request,
    username: str,
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
) -> None:
    """
    Delete a user by their username, note that this endpoint is only available in the testing environment
    as a convenience for performing cleanup operations in end-to-end tests.

    NOT MEANT TO BE USED IN PRODUCTION, as it does not perform any authentication checks.

    Args:
        request (Request): The request instance
        username (str): The username of the user to delete
        user_manager (UserManager): The user manager instance, used to handle all business logic for the User model

    Raises:
        HTTPException: If the user is not found
    """
    try:
        await user_manager.delete_by_username(username, request=request)
    except UserDoesNotExist as e:
        raise HTTPException(
            status_code=404,
            detail={
                "code": TestingErrorCode.USER_NOT_FOUND,
                "reason": e.reason,
            },
        )
