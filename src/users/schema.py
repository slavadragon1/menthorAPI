from pydantic import BaseModel


class User(BaseModel):
    user: str = ""


class AllUsers(BaseModel):
    users: list[User] = []


class UserNotFoundError(BaseModel):
    error: str = "User not found"
