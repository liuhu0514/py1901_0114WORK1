from collections.abc import Iterable, Iterator
list1 = [1, 2, 3]
print(isinstance(list1, Iterable))
print(isinstance(list1, Iterator))

print(isinstance((x for x in range(100)), Iterator))
print(isinstance((x for x in range(100)), Iterable))

print(isinstance(iter(list1), Iterator))
