import requests
import json

r = requests.post('https://search.heweather.net/find?', data={
    "location": "zhengzhou",
    'key': '053d2b04d8a9433c957afe8309bfecd6'

})
a = r.text
b = json.loads(a)
print(b)
c = b['HeWeather6'][0]['basic'][0]
for i, u in c.items():
    print(i, u)

