import asyncio
from typing import Annotated

from sqlalchemy import String, create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings

engine = create_engine(url=settings, echo=False)

with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res.first()}")
 
session_factory = sessionmaker(engine)


str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }

    repr_cols_num = 3
    repr_cols = tuple()
    
    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"
    
