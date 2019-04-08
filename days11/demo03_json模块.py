'''
python中提供一个特殊的模块，可以直接对python
    中的数据进行序列化操作
        序列化：按照指定的数据顺序定义数据格式【类似编码】
'''
import json

# 准备操作的数据
users = {'admin': {'username': 'admin', 'password': '123', 'nickname': '老刘'}}
# 1. 将程序中的数据，直接存储到文件中
# json模块的操作
with open('./data/3.1.json', 'w') as file:
    json.dump(users, file)

# 2. 将文件中的数据，读取到程序中
with open('./data/3.1.json', 'r') as file:
    print(file, type(file))
    users = json.load(file)
    print(users, type(users))
