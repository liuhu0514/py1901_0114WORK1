'''
python程序将多个数据存储到文件中
'''
# 数据准备
s = "字符串"
i = 19
f = 3.1415
b = True
c = 12 + 5j
l = [1,2,3]
d = {'username': 'admin', 'password': '123'}

x = [s, i, f, b, c, l, d]
# 存储多个数据的模块：marshal
import marshal

# 1. 存储多个数据到文件中
# with open('./data/4.1.dat', 'wb') as file:
#     # 第一次存储一个数量：有多少个数据存储到了文件中
#     marshal.dump(len(x), file)
#     # 存储每个数据
#     for x1 in x:
#         marshal.dump(x1, file)

# 2. 将多个数据从文件中依次取出
with open('./data/4.1.dat', 'rb') as file:
    n = marshal.load(file)

    # 将所有数据依次取出
    for x in range(n):
        print(marshal.load(file))



