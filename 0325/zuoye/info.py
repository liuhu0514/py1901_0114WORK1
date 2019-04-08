from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String
# 创建连接实例
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/info",
                       encoding="utf8", echo=True)
from sqlalchemy.ext.declarative import declarative_base
# 创建父类
Base = declarative_base()


class Hotcitys(Base):
    __tablename__ = 'hotcitys'
    cid = Column(String(20), primary_key=True, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)


# Base.metadata.create_all(engine)
import requests
import json

res = requests.post("https://search.heweather.net/top?", data={
    'group': 'world',
    'key': '053d2b04d8a9433c957afe8309bfecd6',
    'number': 30
})

a = res.text
b = json.loads(a)
c = b['HeWeather6'][0]['basic']

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
for i in c:
    u = Hotcitys(cid=i['cid'], lat=i['lat'], lon=i['lon'])
    session.add(u)

session.commit()
