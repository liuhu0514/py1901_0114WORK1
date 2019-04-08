"""
关于封装属性的访问
"""


class Person:
    """人的类型"""

    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.__money = money

    def set_money(self, money):
        self.__money = money

    def get_money(self):
        return self.__money


# 初始化创建一个人
p = Person("老刘", 22, 1000)
print(p.name, p._age)
# 直接访问 破坏性访问
p.name = "老李"
p._age = 30
print(p.name, p._age)
# 直接访问



