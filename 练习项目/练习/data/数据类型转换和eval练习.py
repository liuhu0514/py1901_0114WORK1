'''

程序中的数据，存储到文件中
'''
# 基本数据类型、组合数据类型
# 1. 将程序中的字典数据，转换成字符串存储到文件中
# users = {'admin': {'username': 'admin', 'password': '123', 'nickname': '老刘'}}
# # 转换成字符串类型
# users = str(users)
# print(users, type(users))
# with open("./data/1.1.text", "w") as file:
#     file.write(users)

with open("./data/1.1.text", "r") as file:
    users = file.read()
    print(users, type(users))
    # 转换成字典
    users = eval(users)
    print(users, type(users))
    print(users.get("admin").get("username"))
