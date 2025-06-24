

from typing import TypeVar, Generic
from pydantic import BaseModel

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    message: str
    data: T