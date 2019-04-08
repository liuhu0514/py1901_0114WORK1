import copy
list1 = [1,2,3,[4,5]]
print(list1)
list2 = copy.deepcopy(list1)
print(list2)
list1.append(8)
print(list1, list2)
list1[3].append(6)
print(list1, list2)
