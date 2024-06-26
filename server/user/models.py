from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    id: UUID
    email: str


class UserAuth(BaseModel):
    email: str
    password: str


class UserTokens(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None


class UserSession(User, UserTokens):
    pass
