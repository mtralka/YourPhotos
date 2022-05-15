from uuid import UUID

from pydantic import BaseModel

from .base import CamelModel


class Token(CamelModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int | UUID | None = None
