"""
代码验证
=:复制   内层和外层都是拷贝的引用
"""
import copy
# list1 = [1, 2, 3, [4, 5, 6]]
# list2 = list1
# print(list1 is list2)
# print(id(list1))
# print(id(list2))
# list1.insert(3, 3.5)
# print(list1, list2)
# print(list1 is list2)
# list1[4].append(7)
# print(list1 is list2)
# print(id(list1))
# print(id(list2))
# print(list1, list2)

"""
浅拷贝：copy.copy
    外层赋值，内层拷贝的是引用
"""
# list1 = [1, 2, 3, [4, 5, 6]]
# list2 = copy.copy(list1)
# print(list1 is list2)
# print(list1[3] is list2[3])  # 内层拷贝引用
# # list1.insert(3, 3.5)
# print(list1)
# print(list2)
# list1[3].insert(1, 4.5)
# print(list1)
# print(list2)

"""
深拷贝：copy.deepcopy
    内层外层都只是赋值
"""
list1 = [1, 2, 3, [4, 5, 6]]
list2 = copy.deepcopy(list1)
print(list1 is list2)  # 外层是赋值
print(list1[3] is list2[3])  # 内层也是赋值
# list1.insert(3, 3.5)
print(list1)
print(list2)
list1[3].insert(1, 4.5)
print(list1)
print(list2)
