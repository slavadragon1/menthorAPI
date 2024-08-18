from fastapi import APIRouter
from users.schema import AllUsers
from crud import get_all_users


router = APIRouter(prefix='/users')


@router.get("/")
async def all_users():
    users = await get_all_users()
    return AllUsers(users=users)


@router.get("/{user_id}")
async def user(user_id: int):
    return {"message": f"user: {user_id}"}


@router.post("/")
async def new_user():
    return {"message": "create new user"}


@router.put("/{user_id}")
async def update_user(user_id: int):
    return {"message": "update user"}


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"message": "delete user"}
