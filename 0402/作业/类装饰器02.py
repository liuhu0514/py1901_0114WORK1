import time


class Ly(object):
    def __init__(self, fun):
        print('this is the first step')
        time.sleep(1)
        self.fun = fun

    def __call__(self, *args):
        print('this is the second step')
        time.sleep(1)
        self.fun(*args)
        print('this is the fourth step')
        time.sleep(1)


@Ly
def show(a1, a2, a3, a4):
    print('this is the thirty step', a1, a2, a3, a4)
    time.sleep(1)


show('parm', '1', '1', '1')
print('After first part call')
time.sleep(1)
show('parm', '2', '2', '2')
print('After second part call')



