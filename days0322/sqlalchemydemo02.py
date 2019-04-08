from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/newgoods",
                       encoding="utf8", echo=True)

# 2 ORM类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)
    userid = Column(Integer, ForeignKey("user.id"))


Base.metadata.create_all(engine)
