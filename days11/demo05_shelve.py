'''
python存取多个数据到文件中

    如果按照常规方式~open/write/read方式，每个独立的数据都的单独存储 一个文件
        1. str()数据:字符串:文件存储->文件读取:eval():数据
        2. 数据:json.dump():文件存储->json.load():数据
    如果要存储多个数据到一个文件中
        3. 多个数据:总数量:marshal.dump()->marshal.load(fp):总数量:循环->marshal.load(fp)依次读取

    多个数据，也可以按照比较友好的like dict的方式，将数据存储到文件中
        可以将数据在文件中，通过key值直接获取对应的数据
'''
# 数据准备
users = {'admin': {'username': 'admin', 'password': '123', 'nickname': '大牧'}}
articles = {'标题': {'title': '标题', 'content': '文章内容', 'author': users.get('admin')}}

import shelve

file = shelve.open('./data/5.1')

# 1. 将多个数据按照key:value的形式存储到文件中
file['users'] = users
file['articles'] = articles

# 2. 从文件中根据key读取数据
print(file['users'], type(file['users']))


