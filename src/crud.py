# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import engine
import asyncio

from models import User


async def get_all_users():
    session = AsyncSession(engine)
    exp = select(User)
    result = await session.execute(exp)
    return result.all()


async def get_user_by_id(id: int):
    session = AsyncSession(engine)
    exp = select(User).where(User.id == id)
    result = await session.scalars(exp)
    return result.one_or_none()


if __name__ == "__main__":
    print(asyncio.run(get_user_by_id(12)))
