from pydantic import BaseModel


class User(BaseModel):
    pass


class AllUsers(BaseModel):
    users: list[User] = []
