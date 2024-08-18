from sqlalchemy.orm import Session
from sqlalchemy import select
from database import engine
import asyncio

from models import User


async def get_all_users():
    with Session(engine) as session:
        exp = select(User)
        return session.execute(exp).all()


async def get_user_by_id(id: int):
    with Session(engine) as session:
        exp = select(User).where(User.id == id)
        return session.execute(exp).first()


if __name__ == "__main__":
    print(asyncio.run(get_all_users()))
