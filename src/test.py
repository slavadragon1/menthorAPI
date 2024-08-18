from sqlalchemy.orm import Session
from database import engine, Base
from models import User


with Session(engine) as session:
    Base.metadata.create_all(engine)
    # user = User(name="gena", password_hash="13341k")
    # session.add(user)
    # session.commit()
    # session.close()
