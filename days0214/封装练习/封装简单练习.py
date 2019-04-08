"""
面向对象封装练习
"""


class Person:
    """人的类型"""
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
        else:
            print("您的年龄不到18，请到18以后再来")


# 创建一个对象
p = Person("小花", 17)
print(p.get_name(), p.get_age())
# 修改姓名
p.set_age(20)
print(p.get_name(),p.get_age())

