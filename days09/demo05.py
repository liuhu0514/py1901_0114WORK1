"""
全局变量：访问并修改全局变量
"""
user = "hu"


def name():
    # print("访问全局变量：",user)
    global user
    print("访问原始全局变量：", user)
    user = "liu"
    print("修改全局变量", user)


name()
print("修改之后的变量", user)
