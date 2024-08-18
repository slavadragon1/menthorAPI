from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from database import Base
from typing import List


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    email: Mapped[str | None] = mapped_column(String(30))
    password_hash: Mapped[str] = mapped_column(String(), nullable=False)

    tasks: Mapped[List["Task"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"id: {self.id} name: {self.name}"


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(String(), nullable=True)
    status_id: Mapped[int] = mapped_column(ForeignKey("status.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    status: Mapped["Status"] = relationship(back_populates="tasks")
    user: Mapped["User"] = relationship(back_populates="tasks")


class Status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

    tasks: Mapped[List["Task"]] = relationship(back_populates="status")
