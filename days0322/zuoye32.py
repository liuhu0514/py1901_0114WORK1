from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/qiku",
                       encoding="utf8", echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


