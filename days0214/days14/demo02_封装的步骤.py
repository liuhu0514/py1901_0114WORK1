'''
封装的步骤：
    1. 将全部属性私有化【使用两个下划线开头，描述该属性是私有的，外界不能直接访问】
    2. 给每个属性，提供set/get访问方法
    3. 在访问方法中，就可以添加访问限制，保护数据安全
'''
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if 18 <= age <= 40:
            self.__age = age
        else:
            print("输入年龄不合法")

    def get_age(self):
        return self.__age


# 创建用户对象
p = Person("tom", 10)
print(p.get_name(), p.get_age())

# 修改对象的属性数据
p.set_name("jerry")
p.set_age(100000)
print(p.get_name(), p.get_age())
