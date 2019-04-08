import os
from multiprocessing import Process
import time


# 创建p1进程入口
def p1process():
    while True:
        time.sleep(1)
        print('p1process进程 ', os.getpid())


def p2process():
    while True:
        time.sleep(1)
        print('p2 process 执行了', os.getpid(), 'p2父进程ID', os.getppid())


def main():
    p1 = Process(target=p1process, name='p1进程')
    p1.start()
    # p1.terminate()
    p2 = Process(target=p2process)
    p2.start()
    # p1.terminate()
    print('main process ', os.getpid())


if __name__ == "__main__":
    print('pycharm process ', os.getppid())
    print('进程 process ', os.getpid())
    main()
