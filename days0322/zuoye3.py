from sqlalchemy import create_engine

# 创建连接实例
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/qiku",
                       encoding="utf8", echo=True)
from sqlalchemy.ext.declarative import declarative_base

# 创建父类
Base = declarative_base()
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Tea(Base):
    __tablename__ = "tea"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)


class Stu(Base):
    __tablename__ = "stu"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)
    teaid = Column(Integer, ForeignKey("tea.id"), nullable=False)
    tea = relationship("Tea", backref="t")


# Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()
# 查询对应的老师的学生
a = session.query(Tea).filter(Tea.name == "张").all()
for i in a:
    for x in i.t:
        print(x.name, x.id)

# # 添加
u1 = Tea(id=0, name="liuhu")
# session.add(u1)
# u2 = Tea(id=0, name="liuhu1")
# session.add(u2)

# # s1 = Stu(name="王二", teaid=1)
# session.add(s1)
# s2 = Stu(name="张三", teaid=2)
# session.add(s2)

# # 查询
# result = session.query(Tea.name).filter(Tea.id > 0).all()
# print(result)
# stus = session.query(Stu.name).filter(Stu.id > 0).first()
# print(stus)
#
# # 修改
# session.query(Tea).filter(Tea.id == 1).update({Tea.name: "张"})

# # 删除
session.query(Stu.name).filter(Stu.id == 5).delete()
session.commit()


