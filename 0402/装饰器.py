

def fun1(fun):
    def fun2():
        user = input('请输入用户名')
        if user == 'lh':
            fun()
        else:
            print('您无权限')
    return fun2


@fun1
def insert():
    print('添加成功！')


@fun1
def select():
    print('查询成功！')


if __name__ == '__main__':
    select()
