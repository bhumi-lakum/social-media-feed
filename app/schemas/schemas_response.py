"""
    RESPONSE SCHEMA FILE
"""

from typing import Union

from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    Base Response Schema
    """

    success: bool
    message: str
    data: Union[dict, list] = None


class FailureResponse(BaseResponse):
    """
    Failure Response Schema
    """

    errorCode: int = None
