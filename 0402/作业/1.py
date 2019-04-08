list1 = (x for x in range(10))

try:
    while True:
        a = next(list1)
        print(a)

except StopIteration as e:
    print(e)

list2 = (x for x in range(10))
for i in list2:
    print(i)


def fun(num):
    a, b = 0, 1
    yield a
    yield b
    n = 0
    while n < num:
        a, b = b, a+b
        yield b
        n += 1
    return 'finish'


f = fun(5)
print(f)

while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print(e)
        break

