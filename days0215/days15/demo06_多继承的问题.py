'''
问题：如果不同的父类出现了相同名称的属性或者方法
    子类会继承谁的属性或者方法？

    python3中都是新式类：广度优先，从父类中查询对应的方法，查询到第一个满足的方法之后就直接返回
                    object
                    |
                    A(object)
                    |
        A_1(A) --> A_2(A)
        |
        Test(A_1, A_2)

    python2中的经典类：深度优先
                A
                |
        A  --> A_2(A)
        |
        A_1(A)
        |
        Test(A_1, A_2)
'''
class A:

    def test(self):
        print("aaaaaaaaaaaaaaaaa")


class A_1(A):

    def test1(self):
        print("1111111111111111111")


class A_2:

    def test(self):
        print("2222222222222222222")


class Test(A_1, A_2):
    pass


t = Test()
t.test() # 1111111111111111111
# [<class '__main__.Test'>, <class '__main__.A_1'>, <class '__main__.A_2'>, <class '__main__.A'>, <class 'object'>]
print(Test.mro())