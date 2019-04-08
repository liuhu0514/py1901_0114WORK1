"""
关于封装的属性访问
"""
class Person:
    """人的类型"""
    def __init__(self, name, _age, __money):
        self.name = name
        self._age = _age
        self.__money = __money

    def set_money(self, money):
        """给属性设置值的方法"""
        self.__money = money

    def get_money(self):
        """获取属性值的方法"""
        return self.__money


# 创建对象的同时初始化数据
p = Person("jerry", 18, 1000)
print(p.name, p._age)
# 1. 直接 - 操作对象的属性 - 对于对象的属性，破坏性访问
p.name = "xiao_jie"
print(p.name)
# 2. 约定 - 约定如果一个属性的名称是一个下划线开头的，表示它是私有数据，不让直接操作
p._age = 80
print(p._age)
# Access to a protected member _age of class
# 警告：这里访问了类型中一个收到保护的成员属性_age

# 3. 私有化 - 类型中的属性，通过添加两个开头的下划线，将属性更改为私有属性，外界不能直接访问
# 提供访问该私有属性的 方法【获取数据的方法，设置数据的方法】
# print(p.__money)
print(p.get_money())
p.set_money(1200)
print(p.get_money())
# Unresolved attribute reference __money for class Person
# 在Person类型中，查询不到属性__money




