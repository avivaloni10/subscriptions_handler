from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class SubscriptionSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestSubscription(BaseModel):
    parameter: SubscriptionSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T]
