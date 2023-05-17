from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy import Column, Integer, DateTime

class Base(DeclarativeBase):
    pass

class Wins(Base):
    __tablename__ = "history"

    id: Mapped[int] = mapped_column(primary_key=True)
    result = Column(String)
    game_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self) -> str:
        return f"Wins(id={self.id!r}, result={self.result!r}, game_date={self.game_date!r})"

from sqlalchemy import create_engine
engine = create_engine("sqlite:///gameDB.db", echo=True)

Base.metadata.create_all(engine)