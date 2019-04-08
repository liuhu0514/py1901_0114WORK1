'''
函数参数基本语法练习
'''

#
# # 位置参数:实际参数按照前后顺序依次赋值给形式参数。
# def eat(area,name,wine):
#     print("聚会地点：",area)
#     print("聚会成员：",name)
#     print("酒水类型",wine)
#
#
# eat("皇家一号", ["老刘","花花"], "一担粮二锅头")


# # 默认参数:函数声明定义时，可以给某个参数设置默认数据，在调用执行时~有默认数据的参数可以不传递实际数据
# def party(area, name, wine="拉菲"):
#     print("聚会地点：", area)
#     print("聚会人员", name)
#     print("酒水类型：", wine)
#
#
# party("天上人间", ["老刘", "发发"])
# party("天上人间", ["老刘", "发发"], "二锅头")


# 可变参数:定义在函数声明后括号中的特殊参数，可以接受0~n个实际参数
# def party(area, wine, *name):
#     print("地点：", area)
#     print("参会人员：", name)
#     print("酒水类型：", wine)
#
#
# party("皇家一号","五粮液","老刘","花花")


# 关键字参数:定义在函数声明后括号中的特殊参数，可以接受0~n个键值对数据
# def party(area, **args):
#     print("地点：", area)
#     print("人员", args)
#
#
# party("皇家一号",name="老刘",wine="茅台")


# 万能参数:定义在函数后面的括号中的特殊参数序列，可以让这个函数接受任何形式的参数数据。
# def party(*thing,**args):
#     print("聚会详情",thing)
#     print("人员，酒水",args)


# party("皇家一号","天上人间",name="老刘",wine="二锅头")
# party("皇家一号","天上人间",ming_zi="老刘",liu_shui="二锅头")

def party(area, *, name, wine):
    print("聚会地点", area)
    print("参会人员：", name)
    print("酒水类型：", wine)


party("皇家一号", name=["fa发","老刘"], wine="郎酒")
party("皇家一号", wine="郎酒", name=["fa发", "老刘"])

