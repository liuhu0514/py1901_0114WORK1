from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, target):
        Process.__init__(self, target=target)

    def run(self):
        print('运行了')


def p1process():
    print('p1执行了')


def main():
    p1 = Process(target=p1process)
    p1.start()


if __name__ == '__main__':
    main()
