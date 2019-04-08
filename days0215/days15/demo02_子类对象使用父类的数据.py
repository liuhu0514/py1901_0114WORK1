'''
子类对象使用父类数据
'''
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.__gender = gender

    def say(self):
        print(self.name, "滚去学习")

    def _play(self):
        print(self.name, "滚去玩")

    def __sleep(self):
        print(self.name, "嗨什么嗨，滚去睡觉")

    def get_sleep(self):
        self.__sleep()


class Child(Person):
    # def ge_sleep(self):
    #     super.__sleep()
    pass


c = Child("jerry", 18, "男")
print(c.name)# 对象访问父类中的属性
print(c._age)# 对象访问父类中的属性
# print(c.__gender)# 对象访问父类中的私有属性：ERROR
c.say()# 对象访问父类中的方法
c._play()# 对象访问父类中的方法
# c.__sleep()# 对象访问父类中的私有方法：ERROR
c.get_sleep()
