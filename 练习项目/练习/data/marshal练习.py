'''
python程序将多个数据存储到文件中
'''
import marshal
a = "字符串"
b = ["sf",1]
c = 3
d = 3.1415926
e = True
f = {1:"你好","sff": 1}

x = [a, b, c, d, e, f]

# 1.多个数据存入文件
# with open("./data/1.sdf", "wb") as file:
#     # 第一次存储一个数量：有多少个数据存储到了文件中
#     marshal.dump(len(x), file)
#     # 将多个数据依次存入文件
#     for x1 in x:
#         marshal.dump(x1, file)


# 2.多个数据依次读出来
with open("./data/1.sdf", "rb") as file:
    n = marshal.load(file)
    print(n)
    # 将所有数据依次取出
    for x in range(n):
        print(marshal.load(file))
