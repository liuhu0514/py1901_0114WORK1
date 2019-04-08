import time


def fun(f):
    def fc():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, '消耗', end-start)
    return fc


@fun
def getformlist():
    list1 = [x for x in range(100000001)]
    a = list1.index(99999999)
    print(a)


@fun
def get():
    list1 = (x for x in range(100000001))
    index = 0
    while True:
        try:
            r = next(list1)
            if r == 99999999:
                print(r)
                break
            index += 1
        except StopIteration as e:
            print(e)


getformlist()
get()
