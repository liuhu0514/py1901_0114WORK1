"""
简单认识函数，函数的简单调用
"""

import time
import sys
users = dict()
z_h = list()


# 声明登录菜单
def show_dl():
    # 展示登录注册界面
    print()
    print("欢迎来到博客登录注册界面")
    print()
    print("\t\t1.用户登录")
    print("\t\t2.用户注册")
    print("\t\t3.退出系统")
    print()

    # 用户选择
    choice = input("请选择服务：")

    if choice == "1":
        show_denglu()

    elif choice == "2":
        show_zhuc()

    elif choice == "3":
        print("系统正在退出请稍等...")
        time.sleep(2)
        sys.exit(1)

    else:
        input("您的输入有误，任意键请重新选择")
        show_dl()


# 注册界面
def show_zhuc():
    # 展示注册界面
    print("欢迎来到注册界面")
    print()

    # 提示用户注册
    admin = input("请输入注册账号：（退出n）")
    if admin == "n":
        time.sleep(1)
        show_dl()

    elif admin in users:
        print("您注册的账号已经有了，请重新注册")
        time.sleep(1)
        show_zhuc()

    username = input("请输入昵称：（退出n）")
    if username == "n":
        time.sleep(1)
        show_dl()

    password = input("请设置密码：(退出n)")
    if password == "n":
        time.sleep(1)
        show_dl()

    password1 = input("请确认密码：")
    if password == password1:
        user = {"admin": admin, "password": password, "username": username}
        users[admin] = user
        print("注册成功！")
        show_dl()

    else:
        input("密码不一致，任意键重新注册")
        time.sleep(1)
        show_zhuc()


# 登录页面
def show_denglu():
    global z_h
    # 展示登录界面
    print("欢迎登陆PY1901博客")
    print()

    # 提示输入账号密码
    z_h = input("请输入账号：(退出n)")
    if z_h == "n":
        time.sleep(1)
        show_dl()

    password = input("请输入密码：(退出n)")
    if password == "n":
        time.sleep(1)
        show_dl()

    if z_h in users and password == users[z_h]["password"]:
        print("登录成功！正在跳转")
        time.sleep(1)
        show_main()

    else:
        print("你输入的账户或密码错误！请重新输入")
        time.sleep(1)
        show_denglu()


# 首页菜单界面
def show_main():
    print("欢迎%s来到PY901博客")
    print("\t\t1.个人资料维护")
    print("\t\t2.文章数据维护")
    print("\t\t3.返回上一级")
    print("\t\t4.退出系统")

    # 提示用户选择
    choice = input("请选择您想要的服务")

    # 判断用户的选择
    if choice == "1":
        time.sleep(1)
        show_geren()

    elif choice == "2":
        time.sleep(1)
        show_wenz()

    elif choice == "3":
        time.sleep(1)
        show_dl()

    elif choice == "4":
        print("正在退出系统...")
        time.sleep(3)
        sys.exit(1)

    else:
        input("你的选择有误，请重新选择")
        time.sleep(1)
        show_main()


# 个人资料界面
def show_geren():
    # 展示个人资料界面
    print("欢迎来到个人资料界面")
    print()
    print("\t\t1.修改登录密码")
    print("\t\t2.完善个人资料")
    print("\t\t3.返回上一级")

    choice = input("请选择服务")

    if choice == "1":
        print("正在跳转...")
        time.sleep(1)
        xiu_gai_password()

    elif choice == "2":
        print("正在跳转...")
        time.sleep(1)
        wan_zi_liao()

    elif choice == "3":
        print("正在跳转...")
        time.sleep(1)
        show_main()

    else:
        input("您的输入有误，任意键重新输入")
        time.sleep(1)
        show_geren()


# 修改密码
def xiu_gai_password():
    print("欢迎来到PY901修改密码界面（暂时没有此服务）")
    print()
    print("\t\t1.返回上一级")
    print("\t\t2.退出系统")
    print("\t\t3.修改密码")
    print()
    print("   个人文章")
    choice = input("请选择服务：")

    # 判断用户选择
    if choice == "1":
        show_geren()

    elif choice == "2":
        sys.exit(1)

    elif choice == "3":
        print("修改密码")
        password = input("请输入原密码：")

        if password == users[z_h]["password"]:
            password1 = input("请输入新密码：")
            password2 = input("请确认新密码")

            if password2 == password1:
                users[z_h]["password"] = password1
                print("修改成功！请重新登录...")
                time.sleep(1)
                show_dl()

            else:
                print("密码不一致,请重新修改...")
                time.sleep(1)
                xiu_gai_password()

        else:
            print("密码错误，请重新输入")
            xiu_gai_password()

    else:
        print("您的选择有误，请重新选择")
        time.sleep(1)
        ge_ren_wen()


def wan_zi_liao():
    print("欢迎来到PY901完善个人资料（暂时没有此服务）")
    print()
    print("\t\t1.返回上一级")
    print("\t\t2.退出系统")
    print()
    print("   个人文章")
    choice = input("请选择服务：")

    # 判断用户选择
    if choice == "1":
        show_geren()

    elif choice == "2":
        sys.exit(1)

    else:
        print("您的选择有误，请重新选择")
        time.sleep(1)
        ge_ren_wen()


# 文章数据维护
def show_wenz():
    print("欢迎来到PY901文章数据维护界面")
    print()
    print("\t\t1.发表文章")
    print("\t\t2.查看所有文章")
    print("\t\t3.查看个人文章")
    print("\t\t4.返回上一级")
    print()

    choice = input("请选择您要的项目：")

    # 判断用户选择
    if choice == "1":
        fa_biao()

    elif choice == "2":
        time.sleep(1)
        cha_kan()

    elif choice == "3":
        time.sleep(1)
        ge_ren_wen()

    elif choice == "4":
        print("正在跳转...")
        time.sleep(1)
        show_main()

    else:
        print("您的选择有误，请重新选择")
        time.sleep(1)
        show_wenz()


# 发表文章界面
def fa_biao():
    print("欢迎来到PY901发表文章界面")
    print()
    print("\t\t1.返回上一级")
    print("\t\t2.退出系统")
    print()

    choice = input("请开始写文章：")

    # 判断用户选择
    if choice == "1":
        show_wenz()

    elif choice == "2":
        sys.exit(1)

    else:
        input("您的文章已经写完，是否发表？本功能暂未完善...任意键继续")
        time.sleep(1)
        show_wenz()


def cha_kan():
    print("欢迎来到PY901查看所有文章界面")
    print()
    print("\t\t1.返回上一级")
    print("\t\t2.退出系统")
    print()
    print("   所有文章")
    choice = input("请选择服务：")

    # 判断用户选择
    if choice == "1":
        show_wenz()

    elif choice == "2":
        sys.exit(1)

    else:
        print("您的选择有误，请重新选择")
        time.sleep(1)
        cha_kan()


def ge_ren_wen():
    print("欢迎来到PY901查看个人文章界面")
    print()
    print("\t\t1.返回上一级")
    print("\t\t2.退出系统")
    print()
    print("   个人文章")
    choice = input("请选择服务：")

    # 判断用户选择
    if choice == "1":
        show_wenz()

    elif choice == "2":
        sys.exit(1)

    else:
        print("您的选择有误，请重新选择")
        time.sleep(1)
        ge_ren_wen()


# 启动程序，调用函数展示登录菜单
show_dl()
