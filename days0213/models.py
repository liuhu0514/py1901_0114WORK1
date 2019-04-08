"""
创建程序中需要的各种类
"""


class Person:
    """
    创建一个人的类型
    """

    def __init__(self, name, age, gender):
        """
        定义人的属性
        :param name: 对象名称
        :param age: 对象年龄
        :param gender: 对象性别
        """
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        """
        定义人吃的行为
        :return:
        """
        print(self.name, "该吃饭了，吃米饭...")

    def sleep(self):
        """
        定义人睡的行为
        :return: 无
        """

        print(self.name, "睡觉了！")
