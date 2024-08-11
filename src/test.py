from sqlalchemy.orm import Session
from database import engine
# from tasks.model import Task
from tasks.model import Status


with Session(engine) as session:
    # task1 = Task(title="testTask")
    print("hello")
