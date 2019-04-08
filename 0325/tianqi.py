import requests
import json

res = requests.post("https://free-api.heweather.net/s6/weather/forecast?",data={
    "location": "zhengzhou",
    "key": '053d2b04d8a9433c957afe8309bfecd6'
})

a = res.text
print(a)
b = json.loads(a)
print(b)
c = b['HeWeather6'][0]
for i in c:
    print(i)
# for i, d in c.items():
#     print(i, d)

