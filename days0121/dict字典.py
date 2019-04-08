"""
为了方便数据在组合数据类型中的管理，python 还提供了一种特殊存储数据的组合数据类型：字典。
通过key-value键值对的形式来存储数据，可以很方便的通过key来对value进行增删改查的操作
字典：dict
"""


a={"b":"j","2":"k"}
print(type(a))

# 通过键（key）查找值（value）
print(a["b"])              # 通过方括号形式查
print(a.get("2"))         # 通过get()函数方法查询

# 修改字典中指定的数据，通过给指定的key直接赋值就可以修改
a["b"] = "h"
print(a.get("b"))


# 删除字典中的数据，通过删除指定的key对应的数据即可删除
a.pop("2")
print(a)


list1=["黄鹤楼",18,20]
list2=["黄金叶",10,30]
dict1={'1':list1,"2":list2}
x=True
while True:
    if x==False:
        break
    # print(dict1[1][0])
    # print(dict1[2])
    #
    # print(dict1)

    choice=input('请选择：')

    for i in dict1.keys():

        if choice==i:
            print("您购买的是%s，单价%s元/盒，库存剩余%s盒"%(dict1[i][0],dict1[i][1],dict1[i][2]))
            x=False
            break
