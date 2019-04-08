def pbl(num):
    a, b = 1, 1
    yield a
    yield b
    n = 0
    while n < num:
        a, b = b, a+b
        yield b
        n += 1
    return '裴波拉契'


result = pbl(10)
for r in result:
    print(r)

res = pbl(10)
while True:
    try:
        x = next(res)
        print(x)
    except StopIteration as e:
        print(e)
        break
