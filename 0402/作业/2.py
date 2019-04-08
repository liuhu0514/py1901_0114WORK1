from collections.abc import Iterable, Iterator

list1 = [1, 2]
tuple1 = (1, 2, 3)
dict1 = {"name": "laoliu"}
str1 = 'hello'
int1 = 5
print(isinstance(list1, Iterable))
print(isinstance(list1, Iterator))
print(isinstance(tuple1, Iterable))
print(isinstance(tuple1, Iterator))
print(isinstance(dict1, Iterable))
print(isinstance(dict1, Iterator))
print(isinstance(str1, Iterable))
print(isinstance(str1, Iterator))
print(isinstance(int1, Iterable))
print(isinstance(int1, Iterator))
# 没有迭代器
