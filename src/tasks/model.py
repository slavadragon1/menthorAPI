from sqlalchemy import String, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from database import Base
from users.model import User
from typing import List


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text())
    status_id: Mapped[int] = mapped_column(ForeignKey("status.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    status: Mapped["Status"] = relationship(back_populates="tasks")
    user: Mapped["User"] = relationship(back_populates="tasks")


class Status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

    tasks: Mapped[List["Task"]] = relationship(back_populates="status")
