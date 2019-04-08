'''
全局变量的操作
'''
# 定义了两个全局变量
name = "tom"
fav = ['lol']


# 1. 修改全局变量的数据：全局变量是一个字符串
def test_str():
    '''修改字符串数据'''
    # 如果要修改全局变量的数据：声明可以修改
    global name
    # 查看全局变量的数据
    print(name)
    # 修改全局变量的数据
    name = 'jerry'

    print("name:", name)
# '''
# 全局变量
#     在普通函数中，可以访问数据
#         但是一般不允许直接修改数据
#         可以通过global关键字引入之后进行修改
# '''
#
print("test_str执行之前", name)
test_str()
print("test_str执行之后", name)
#
# def test():
#     print("test中访问全局变量name:", name)
#
# # 只要在test_str()函数中，对全局变量global之后进行了修改，在之后的访问中，变量就是修改后的数据
# test()


# # 2.修改全局变量的数据，全局变量是一个列表
# def test_list():
#     print("全局变量的数据fav:", fav)
#     # 修改list数据
#     fav.append("CCTV")
#     print("全局变量的数据fav:", fav)
#
# test_list()
# print("普通代码中全局变量fav:", fav)
#
#
# '''
# 再说数据类型：
#     python中数据类型
#         不可变类型：数据一旦赋值~该数据是固定的不能变化的
#             如：字符串 name = "tom"
#                 重新赋值：name = "jerry" 修改~创建了一个新字符串，替代了旧字符串
#         可变类型：复杂数据一旦赋值给变量~复杂数据中包含的具体数据可以修改
#             如：列表 l = list()  -> l = []
#                 l.append('world') -> l = ['world']
#
#
# '''
