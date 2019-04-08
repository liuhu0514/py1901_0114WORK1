from sqlalchemy import create_engine
from sqlalchemy import Column, Float, String
import requests
import json
import pymongo

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


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
seddion = Session()

a = seddion.query(Hotcitys.cid)
for i in a:
    res = requests.post("https://free-api.heweather.net/s6/weather/forecast?", data={
        "location": i[0],
        "key": '053d2b04d8a9433c957afe8309bfecd6'
    })
    b = res.text
    c = json.loads(b)
    d = c['HeWeather6'][0]['daily_forecast']
    pymongo.MongoClient()['info']['day1'].insert_one({'cid': i[0], 'tmp_max': d[0]['tmp_max'], 'tmp_min': d[0]['tmp_min']})
    pymongo.MongoClient()['info']['day2'].insert_one({'cid': i[0], 'tmp_max': d[1]['tmp_max'], 'tmp_min': d[1]['tmp_min']})
    pymongo.MongoClient()['info']['day3'].insert_one({'cid': i[0], 'tmp_max': d[2]['tmp_max'], 'tmp_min': d[2]['tmp_min']})


