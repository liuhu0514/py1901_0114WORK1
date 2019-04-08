"""
封装：存在的一些操作误区和解决方案
"""
"""
1. 误区：什么样的属性应该封装？封装的话是不是一定要添加限制访问条件？
    (1) 为了让定义的数据类型，能使用不同的应用场景，一帮情况下我们
    要对当前类型的所有属性进行封装处理。
    (2) 封装属性之后，会提供访问属性数据的set/get方法，开发过程中方法中不需要添加
    任何限制条件，只是预留了可以添加限制条件的方法而已，后期根据项目需求进行限制
    条件的完善。
"""


class User:
    """用户类型"""

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


"""
2. 误区：私有属性，完全不能直接访问
    我们定义了私有属性，就是两个下划线开头的属性
    理论上外界不能直接访问，而是要通过我们提供的set/get方法间接访问
    
    功能开发过程中，代码和功能都可能会存在一些问题
        如果发现问题~一定要及时沟通，而不是私自修改。
"""


class Person:

    def __init__(self, name):
        self.__name = name


p = Person("tom")
# 私有属性破坏性访问方式：我们自己要知道，但是严禁使用
p._Person__name = "jerry"
print(p._Person__name)

"""
3. 误区：关于对象属性的扩展
"""


class Goods:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


car = Goods("奥拓", 18000)
print("car的价格:", car.get_price())

# 如果通过 对象的引用变量.属性 直接赋值，该属性又不是类型中定义的属性
# 这个属性就是 单独属于这个对象 的扩展属性。
car.__price = 20000
print("car的价格", car.__price, "---", car.get_price())

# 扩展属性，属于对象car
car.__color = "红色"
print(car.__color)

# car2 = Goods("奥迪", 300000)
# print(car2.__color)

"""
但是，这样的扩展方式，破坏了原有的封装语法，让代码的可读性出现了严重的下降

解决方案：在类型中，定义好~该对象可以出现的属性，其他任何扩展属性就不能添加了。
"""


class Pet:
    """宠物类型：限制该类型只能出现哪些属性"""
    # 限制该类型的对象，只能拥有下面列表中出现的属性
    __slots__ = ['__name', '__age', '__gender', 'color']

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

p = Pet("tomcat", 18, "公")
print(p.get_name(), p.get_age(), p.get_gender())
# 扩展属性
p.color = "灰色"
print(p.get_name(), p.get_age(), p.get_gender(), p.color)

p.email = "tomcat@cat.com"
print(p.email)