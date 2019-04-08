'''
程序中的数据，存储到文件中
'''
# 基本数据类型、组合数据类型
# 1. 将程序中的字典数据，转换成字符串存储到文件中
# users = {'admin': {'username': 'admin', 'password': '123', 'nickname': '老刘'}}
#
# # 类型能否直接转换字符串?
# users_str = str(users)
#
# # 存储到文件中
# with open('./data/2.1.text', 'w') as file:
#     file.write(users_str)


# 2. 将文件中的字符串数据，读取到程序中
with open('./data/2.1.text', 'r') as file:
    users = file.read()
    print(users, type(users))
    # 将字符串数据，转换成字典：该字符串的格式~和python中的字典的表达式一致
    users = eval(users)
    print(users, type(users))
    print(users.get('admin'))

'''
问题：每个文件只能存储一个指定的数据
项目中：用户字典、文章字典、菜单映射字典
        users   artciles   login_menu_dict/index_menu_dict
'''