import requests
import re
response = requests.get('http://quote.stockstar.com/stock/ranklist_a_3_1_1.html')
# print(response.text)
res = response.text
result = re.search(r'<tbody class="tbody_right" id="datalist">(.*?)</tbody>', res, re.S)
# print(result)
# for r in result:
#     print(r.group(1))
#     # print(r.group(2))

result = re.findall(r'<tr>(.*?)</tr>', result.group(1))
# print(result[0])
# for r in result:
#     r1 = re.findall(r'<td.*?>(.*?)</td>', r)
#     # print(r1[0])
#     id = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">\1</a>', r1[0])
#     # print(id.group(1))
#     name = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', r1[1])
#     # print(name.group(2))
#     price = re.search(r'<span class="red">(.*?)</span>', r1[2])
#     print(price.group(1))

with open('data.txt','w',encoding='utf8') as fl:
    for r in result:
        r1 = re.findall(r'<td.*?>(.*?)</td>', r)
        # print(r1[0])
        id = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">\1</a>', r1[0])
        # print(id.group(1))
        name = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', r1[1])
        # print(name.group(2))
        price = re.search(r'<span class="red">(.*?)</span>', r1[2])
        # print(price.group(1))
        fl.write('股票代码:'+str(id.group(1))+"   股票名："+str(name.group(2))+"     最新价格："+str(price.group(1)))
        fl.write('\n')
