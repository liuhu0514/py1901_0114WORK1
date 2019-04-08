from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/newgoods",
                       encoding="utf8", echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime


class User(Base):
    __tablename__ = "jg"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)
    retime = Column(TIMESTAMP, default=DateTime.now())


Base.metadata.create_all(engine)

