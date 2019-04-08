# import sqlalchemy
# print(sqlalchemy.__version__)

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/school",
                                    encoding='utf8', echo=True)
result = engine.execute("show tables")

print(result.fetchall())
