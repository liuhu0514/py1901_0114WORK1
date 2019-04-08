"""
装饰器作用：在不改变原函数的情况下给函数增加功能

"""


def func(fun):
    def fun1():
        if input('请输入用户名：') == 'lh':
            fun()
        else:
            print('您的权限不够')

    return fun1


def show_list():
    for i in range(10):
        print(i)


show_list = func(show_list)
show_list()
