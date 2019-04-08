from sys import getrefcount
while True:
    # print(getrefcount([1, 2, 3]))
    list1 = [1, 2, 3]
    # print(getrefcount(list1))
    list2 = [4, 5, 6]
    # print(getrefcount(list2))
    list1.append(list2)
    list2.append(list1)
    print(getrefcount(list1), getrefcount(list2))
    del list1
    del list2
