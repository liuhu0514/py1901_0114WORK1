'''
python中，还提供了一种特殊的数据类型，集合Set，和列表类似，但是不能存储相同的数据；
注意：集合set中存放数据是不能重复的，并且是没有存放顺序的，也就是没有下标的。
'''

set={1,"s","d","a"}
# set.add("hu")     #  添加数据
print(set)


set.remove("s")         #删除数据
print(set)


for admin in set:
    print(admin)




