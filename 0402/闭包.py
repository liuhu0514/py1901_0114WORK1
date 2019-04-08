"""
闭包：
"""


def fun1(a):
    def fun2(b):
        nonlocal a
        a += 1
        return a+b
    return fun2


f = fun1(20)
print(f)
print(f(10))
