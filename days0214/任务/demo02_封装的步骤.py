"""
封装的操作步骤
"""


class Person:
    """人的类型"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


p = Person("老刘", 30)
print(p.get_age())
