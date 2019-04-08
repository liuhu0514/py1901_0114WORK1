'''
继承基本语法
    体现的是，某个小类型，属于某个大类型的
        如：男人 是 人 的一种类型

    生活中：约定

    代码中：约定  Man类型就是Person类型  非强制

    代码中：强制约束：通过继承关系，体现某个类型属于另一个类型

关于继承：
    python中的所有类型，都是直接或者间接继承自object类型的
        object:对象 万物皆对象

    python3中类型声明语法：
        class 类型名称:   # 隐式继承object类型
            pass

        class 类型名称(object): # 显式继承object类型
            pass

    python2中类型的声明语法：
        class 类型名称:   # 经典类
            pass

        class 类型名称(object): # 新式类
            pass

继承的语法：
    class 类型名称(要继承的类型):
        pass

继承的特性：
    代码中出现了继承，类型就出现了新的名称：
        被继承的类型：父类
        当前类型：子类
        体现的是：子类继承父类

    子类中就可以继承父类中的属性和方法【公共】
        子类中可以直接使用父类的属性和方法

'''
class Person:
    """人的类型"""

    def __init__(self, name):
        self.name = name


class Man(Person):
    """男人"""
    pass


tianqi = Man("jerry")
mingxin = Man("jerry")
da_sheng = tianqi
print(type(tianqi))
# 运算符：类型判断运算符 isinstance
print(isinstance(tianqi, Man))
print(isinstance(tianqi, Person))

# 运算符：对象判断运算符 is
print(tianqi is Man)
print(tianqi is Person)
print(tianqi is mingxin)

print(tianqi is da_sheng)
print(tianqi == da_sheng)


