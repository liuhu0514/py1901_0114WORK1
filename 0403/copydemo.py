import copy
"""
= 赋值：内外层都拷贝的是引用
"""
# list1 = [1, 2, 3, [4, 5]]
# list2 = list1
# print(list1 is list2)
# print(list1, list2)
# print(id(list1))
# print(id(list2))
# list1.insert(3, 3.5)
# list1[4].insert(1, 4.5)
# print(list1, list2)
"""
    copy:浅拷贝  copy.copy
    外层复制值， 内层引用
"""

# list1 = [1, 2, 3, [4, 5]]
# list2 = copy.copy(list1)
# print(list1 is list2)
# print(list1, list2)
# print(id(list1), id(list2))
# print(id(list1[3]), id(list2[3]))
# list1.insert(3, 3.5)
# print(list1 is list2)
# print(list1, list2)
# print(id(list1), id(list2))
# list1[3].insert(1, 4.5)
# print(list1 is list2)
# print(list1, list2)
# print(id(list1), id(list2))
# print(id(list1[3]), id(list2[3]))


"""
深复制：copy.deepcopy
    内外层都是复制值
"""
list1 = [1, 2, 3, [4, 5]]
list2 = copy.deepcopy(list1)
print(list1 is list2)
print(list1, list2)
print(id(list1), id(list2))
print(id(list1[3]), id(list2[3]))
# list1.insert(3, 3.5)
# print(list1 is list2)
# print(list1, list2)
# print(id(list1), id(list2))
list1[3].insert(1, 4.5)
print(list1 is list2)
print(list1, list2)
print(id(list1), id(list2))
print(id(list1[3]), id(list2[3]))
