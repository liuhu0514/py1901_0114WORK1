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
print(c)
for i in c:
    print(i)
