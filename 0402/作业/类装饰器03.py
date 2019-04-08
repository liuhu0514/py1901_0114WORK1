import time


class Ly:
    def __init__(self, one_parm, two_parm, three_parm):
        self.one_parm = one_parm
        self.two_parm = two_parm
        self.three_parm = three_parm

    def __call__(self, fun):
        print('性别' + self.one_parm + '的' + self.two_parm + '岁的' + self.three_parm)
        time.sleep(1)

        def info(*args):
            fun(*args)

        return info


@Ly('男', '22', 'ly')
def show(name, age, sex):
    print('性别' + sex + '的' + age + '岁的' + name)


show('蓝月', '20', '男')
