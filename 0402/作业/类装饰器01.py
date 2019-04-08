import time, datetime


class P:
    def __init__(self, fun):
        self.fun = fun
        print('this is the first step on' + str(datetime.datetime.now()))
        time.sleep(1)
        self.fun()

    def __call__(self):
        print('this is the thirty step on' + str(datetime.datetime.now()))


@P
def show():
    print('this is the second step on' + str(datetime.datetime.now()))
    time.sleep(1)


if __name__ == "__main__":
    show()
    print('this is the fourth step on' + str(datetime.datetime.now()))
