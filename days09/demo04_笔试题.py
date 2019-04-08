'''
笔试题：
请分析下面代码是否出现问题？
    简要说明问题出现的原因
'''
'''
name = "tom"

def test():
    print("访问数据：", name)
    
    name = "jerry"
    
    print("访问数据：", name)

test()

1. 结论：有问题
2. 结果：第10行代码会出现错误
3. 原因：因为函数中没有global引入不可变类型name，所以12行声明的name是一个局部变量
    函数中访问name都是访问局部变量name，第10行代码在name局部变量声明之前进行了访问，这是语法错误

Inspection info: This inspection detects names that should resolve but don't. 
Due to dynamic dispatch and duck typing, this is possible in a limited but useful number of cases.
 Top-level and class-level items are supported better than instance items.
'''
name = "tom"


def test():
    print("访问数据：", name)

    name = "jerry"

    print("访问数据：", name)


test()