from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from database import Base
from tasks.model import Task
from typing import List


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(30))
    password_hash: Mapped[str] = mapped_column(String(), nullable=False)

    tasks: Mapped[List["Task"]] = relationship(back_populates="user")
