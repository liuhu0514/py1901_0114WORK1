'''
列表的语法结构：通过一堆方括号包含起来的数据序列，可以存放重复数据
列表：list
可以嵌套
'''

list1=[1,"o",3,["a:","b"]]    # 可以嵌套

# 列表数据的查看，可以通过索引/下标进行查看
print(list1[0])
print(list1[3][1])

# 列表中追加数据：append()
list1.append(["l","hu"])
print(list1)


# 列表中指定位置追加数据：insert()
list1.insert(1,["a","m"])
print(list1)


# 删除列表末尾的元素：pop()
list1.pop()
print(list1)


# 删除列表中指定位置的元素：pop(index
list1.pop(2)
print(list1)


# 将列表中指定位置的数据进行替换，直接给对应的索引赋值
list1[0]=[1,2]
print(list1)
