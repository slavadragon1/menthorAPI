from fastapi import APIRouter
from users.schema import AllUsers, User, UserNotFoundError
from crud import get_all_users, get_user_by_id


router = APIRouter(prefix='/users')


@router.get("/")
async def all_users() -> AllUsers:
    users = await get_all_users()
    return AllUsers(users=users)


@router.get("/{user_id}")
async def user(user_id: int) -> User | UserNotFoundError:
    user1 = await get_user_by_id(user_id)
    print(user1)
    if user1:
        return User(user=user1)
    return UserNotFoundError


@router.post("/")
async def new_user():
    return {"message": "create new user"}


@router.put("/{user_id}")
async def update_user(user_id: int):
    return {"message": "update user"}


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"message": "delete user"}
