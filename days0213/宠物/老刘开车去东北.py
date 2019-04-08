"""
类和对象的基本练习
    老刘开车去东北
"""


class Person:
    """
    定义一个人的类型
    """

    def __init__(self, name, age):
        """
        定义人类型的属性
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def jia_shi(self, vehicle, place):
        """
        人驾驶车的行为
        :return:
        """
        print(self.name, "驾驶")
        vehicle.travel(place)


class Vehicle:
    """
    交通工具类型
    """

    def __init__(self, name):
        self.name = name

    def travel(self, place):
        print("开着", self.name, "行驶去", place.name)


class Place:
    """
    目的地类型
    """

    def __init__(self, name):
        self.name = name


# 创建一个人
p1 = Person("老张", 20)
# 创建一个交通工具
car = Vehicle("奔驰")
# 创建一个目的地
pla = Place("东北")

# 调用人的驾驶行为
p1.jia_shi(car, pla)

