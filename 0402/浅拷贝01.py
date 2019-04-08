list1 = [1,2,[3,4]]
print(list1)
list2 = list1
print(list2)
list1.append(5)
print(list1,list2)
list1[2].append(3.5)
print(list1,list2)
