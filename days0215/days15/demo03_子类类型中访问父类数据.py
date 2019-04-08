'''
子类类型使用父类数据

    1. 子类中访问父类的方法
        super().方法名称()
        注意：访问属性时~可能会出错。扩展~为什么会出错？

    2. 子类的__init__()方法
        如果子类中不写__init__()方法，直接使用父类的__init__()方法初始化数据
        怎么访问：如果子类中写了自己的__init__()方法，一定要调用执行父类的__init__()方法

        什么时候访问：什么时候子类写自己的__init__()方法，子类中出现独立属性时！
        为什么要访问：？

    3. 子类中可以重新定义从父类中继承的方法【方法名称和方法参数一致】：方法重写
        方法重写：子类中重写父类中已经存在的方法
            在执行过程中~如果子类中重写了方法，执行子类的方法，如果没有重写则执行父类中的方法【运行过程中的多种状态切换：运行时多态】

    在继承关系中，python中有两种事物的存在：
        数据类型-> 所有的类型，都是直接继承自type类型的
        对象-> 所有对象都是直接或者间接继承自object对象的

        python中所有的数据，都是直接或者间接继承自type类型的。

        重点：区分类型和对象的区别
'''
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say(self):
        print(self.name, "滚去学习")

    def play(self):
        print(self.name, "出门打麻将")

    def sleep(self):
        print(self.name, "嗨什么嗨，滚去睡觉")


class Child(Person):

    def __init__(self, name, age, gender, email, phone):
        super().__init__(name, age, gender)
        self.email = email
        self.phone = phone

    def speek(self):
        """子类的方法"""
        # 访问父类的属性和方法
        # print("子类speek中访问父类的属性：", super().name)
        super().say()
        print("子类的speek方法执行中......")

    def play(self):
        print(self.name, "搭积木.........")



c = Child("tom", 18, "男", "damu@163.com", "15682808270")
c.speek()
print(c.email)
c.play()

p = Person("jerry", 20, "女")
p.play()
# print(p.email)