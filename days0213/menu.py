"""
定义各种界面
"""
import models, data


# 注册界面函数
def zhu_ce():
    print("根据提示注册")

    # 提示用户输入用户名
    new_user = input("请输入用户名：")
    age = input("请输入年龄：")
    gender = input("请输入性别：")
    p1 = models.Person(new_user, age, gender)
    p[new_user] = p1
    show_long()
# 首页界面函数
def show_long():
    """
    展示登录界面
    """
    print("欢迎来到PY1901个人信息平台")
    print()
    print("~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~")
    print("1.吃饭")
    print("2.睡觉")
    print("3.运动")
    print("~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~")

    # 提示用户输入
    choice = input("请选择服务：")
    if choice == "1":
        pass


p =dict()

