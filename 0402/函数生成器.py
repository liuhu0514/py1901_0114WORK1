# list1 = [x for x in range(100)]
# for i in list1:
#     print(i)


def fun():
    yield 1
    yield 2
    yield 3
    yield 4
    return '你好'


f = fun()
try:
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
except StopIteration as s:
    print(s)


for i in fun():
    print(i)
