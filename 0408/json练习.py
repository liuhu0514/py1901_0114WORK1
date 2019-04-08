import json
name = input('请输入商品名')
price = input('请输入价格')


class Good:
    name = None
    price = None


g = Good()
g.name = name
g.price = price
g_str = json.dumps(g.__dict__)
with open('data.txt', 'w', encoding='utf-8') as fl:
    fl.write(g_str)


with open('data.txt', 'r') as f:
    print(f.read())
