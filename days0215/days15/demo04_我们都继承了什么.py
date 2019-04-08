"""
既然出现了继承，python中的所有对象都是直接或者间接继承object
    1. 我们都继承了什么？
 构造方法
    __new__  创建对象的方法   一般不使用~直接通过父类创建对象即可。
    __init__ 初始化数据的方法  一般会重写该方法，用来初始化对象数据

    __slots__ 封装时，限制属性的

    __str__ 对象字符打印方式；默认情况打印内存中16进制表示的位置
    __repr__ 交互模式中，字符打印方式

    __hash__ 获取对象的hash数据，用于判断的依据
    __ne__ 不等于：not equals；两个对象使用!=判断的
    __ge__ 大于等于：grant or equals  判断 >=
    __gt__ 大于： grant than判断 >
    __le__ 小于等于：less or equals 判断 <=
    __lt__ 小于 less than 判断 <
    __eq__ 判断等于 equals 判断 ==

    __dict__ 将对象转换成字典
    __doc__ 说明文档
    __class__ 类型，类似于type

    __format__
    __getattribute__
    __delattr__
    __sizeof__
    __reduce__
    __reduce_ex__
    __dir__
    ____init_subclass__
    __module__

    __setattr__  给属性设置数据-一般不重写
    2. 这些继承的东西有什么作用？

"""
class Person:
    """人的类型"""
    def __init__(self, name, age):
        """
        人的类型初始化函数
        :param name: 初始化的姓名
        :param age: 初始化的年龄
        """
        self.name = name
        self.age = age

    def __str__(self):
        return f"人：[name:{self.name}, age:{self.age}]"

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        # 判断两个对象~是否相等，按照业务逻辑 姓名和年龄一样，表示是同一个人
        if self.name == other.name and self.age == other.age:
            return True
        return False

    def __gt__(self, other):
        # 判断两人的大小：业务判断~按照年龄判断
        if self.age > other.age:
            return True
        return False

    def __ge__(self, other):
        if self.age >= other.age:
            return True
        return False

    def sleep(self, area):
        """
        睡觉了
        :param area 这是一个方法的参数说明
        """


# 创建对象
p1 = Person("tom", 18)
# 打印对象 0x000001E265E7ADA0~ 内存中的地址 16进制字符表示方式
print(p1) # <__main__.Person object at 0x000001E265E7ADA0>

p2 = Person("tom", 18)

print(p1.__hash__())

print(p1 == p2)
print(p1 > p2)
print(p1 >= p2)

print(p1.__dict__)

print(p1.__doc__)
print(p1.sleep.__doc__)
