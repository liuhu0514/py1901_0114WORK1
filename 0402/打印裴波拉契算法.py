def fib(times):
    n = 0
    a, b = 0, 1
    yield a
    yield b
    while n < times:
        a, b = b, b+a
        yield b
        n += 1
    yield 'finish'


r = fib(10)
print(r)
while True:
    try:
        x = next(r)
        print(x)
    except StopIteration as e:
        print(e.value)
        break
