'''
函数的参数处理
'''
# 1. 位置参数
# def party(area, person, wine):
#     '''聚会的函数'''
#     print("今晚消毒，放假")
#     print("晚上聚会")
#     print("地点：", area)
#     print("参与人员：", person)
#     print("有了酒，就有了故事.....", wine)


# 函数的调用过程
# party('天上人间', ['老刘', '花花'], '二锅头')

# 2. 默认值参数
# def party(person, wine='二锅头', area='天上人间'):
#     '''聚会的函数'''
#     print("今晚消毒，放假")
#     print("晚上聚会")
#     print("地点：", area)
#     print("参与人员：", person)
#     print("有了酒，就有了故事.....", wine)


# party('老刘', '二锅头', '皇家一号')
# party('老刘', '82年的拉菲')
# party('老刘')

# 3. 可变参数：可以接受0~n个数据
# def party(name, *things):
#     print("参与人员：", name)
#     print("使用资源：", things)
#
# party('老刘')
# party('老刘', '蜡烛')
# party('老刘', '蜡烛', '拉菲')
# party('老刘', '花花', '蜡烛', '拉菲', '披萨', '菲力牛排')

# 4. 关键字参数：可以接受0~n个键值对数据
# def party(name, **things):
#     print("参与人员：", name)
#     print("使用资源：", things)
#
# party('老刘')
# party('老刘', wine='二锅头')
# party('老刘', wine='拉菲/82', girl='花花')

# 5. (号称)万能参数
# def party(*args, **kwargs):
#     print(args)  # args: arguments 参数
#     print(kwargs)# kwargs: key word arguments 关键字参
#
# party()
# party('老刘')
# party('老刘', girl='花花')
# party('老刘', '花花', wine='拉菲', food='牛排')
# party('老刘', '花花', jiu='拉菲', shi_wu='牛排')

# 6. 强制关键字参数~ 不是可变参数
def party(name, *, wine, food):
    print(name)
    print(wine)
    print(food)


# party('老刘', wine='二锅头', food='牛排')
# party('老刘', food='牛排', wine='二锅头')
# party('老刘', jiu='二锅头', shi_wu='牛排') # ERROR
