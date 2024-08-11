from fastapi import APIRouter


router = APIRouter(prefix='/tasks')


@router.get("/")
async def all_tasks():
    return {"message": "all tasks"}


@router.get("/{task_id}")
async def task(task_id: int):
    return {"message": f"user: {task_id}"}


@router.post("/")
async def new_task():
    return {"message": "create new user"}


@router.put("/{task_id}")
async def update_task(task_id: int):
    return {"message": "update user"}


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    return {"message": "delete user"}
