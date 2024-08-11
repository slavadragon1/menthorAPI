from users.router import router as users_router
from tasks.router import router as tasks_router


def init_routes():
    from main import app
    app.include_router(users_router, tags=["users"])
    app.include_router(tasks_router, tags=["tasks"])
