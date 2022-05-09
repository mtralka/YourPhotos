
from .base import CamelModel


class Token(CamelModel):
    access_token: str
    token_type: str


class TokenPayload(CamelModel):
    sub: int | None = None
