def fun():
    print('!!')
    while True:
        yield 1
        print('***')


f = fun()
print(next(f))
print('---------')
print(next(f))
print('---------')
print(next(f))
