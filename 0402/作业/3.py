"""
装饰器：
作用：在不改变原函数的情况下给函数增加功能！
"""
import time


# 创建函数装饰器
def funb(fun):
    def f():
        # 判断用户输入是否有权限
        # 如果有权限就执行函数
        if input('请输入用户名：') == "lh":
            fun()
        # 如果不能就返回提示
        else:
            print('您没有权限查看！')
    return f


# 创建装饰器连接
@funb
def select():
    print('查询到了')


# 调用启动查看函数
select()


def func(fun):
    def f():
        start = time.time()
        fun()
        end = time.time()
        print(fun.__name__, '消耗', end-start)
    return f


@func
def getfromlist():
    list1 = (x for x in range(100000))
    while True:
        try:
            next(list1)
        except StopIteration as e:
            print(e)
            break


getfromlist()
