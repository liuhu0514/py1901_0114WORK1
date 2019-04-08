"""
面向对象封装简单案例练习
    上网：18岁以后才能上网
"""


class Person:
    """创建一个人的类型"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if self.__age >= 18:
            self.__age = age

    def computer(self):
        if self.__age >= 18:
            print(self.__name, "可以去网吧上网")

        else:
            print(self.__name, "您的年龄太小，不能上网")


p = Person("tom", 17)
p.set_age(20)

p1 = Person("jirey", 20)
p1.set_age(30)
print(p.get_age())
p.computer()
p1.computer()
