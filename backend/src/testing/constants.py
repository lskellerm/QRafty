"""Testing specific constants and error codes, used for testing the application in an end-to-end testing environment"""

from enum import Enum
from typing import Dict, Union

from pydantic import BaseModel


class ErrorModel(BaseModel):
    """
    ErrorModel class for returning error details in the response

    Args:
        BaseModel (pydantic.BaseModel): The base model class for the error model
    """

    detail: Union[str, Dict[str, str]]


class ErrorCodeReasonModel(BaseModel):
    """
    ErrorCodeReasonModel class for returning error code and reason in the response

    Args:
        BaseModel (pydantic.BaseModel): The base model class for the error code and reason model
    """

    code: str
    reason: str


# Error codes for the testing endpoints
class TestingErrorCode(str, Enum):
    USER_NOT_FOUND = "USER_NOT_FOUND"
