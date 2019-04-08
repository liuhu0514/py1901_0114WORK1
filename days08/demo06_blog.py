'''
个人博客项目开发
'''
import os, sys, time

# 定义存储所有用户数据的字典
users = dict()
# 存储当前登录在线的用户
online = None


def show_login():
    '''展示登录菜单'''
    print("\t\t博客用户登录")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 用户登录")
    print("\t\t2. 用户注册")
    print("\t\t3. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")


def show_register():
    '''展示注册菜单'''
    print("\t\t博客用户注册")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t根据提示信息，完成用户资料的录入")
    print("\t创建自己的账号，享受系统带来的乐趣吧.....")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")


def show_index():
    '''展示首页'''
    print("\t\t博客用户首页")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 查看所有文章")
    print("\t\t2. 查看个人文章")
    print("\t\t3. 发表文章")
    print("\t\t4. 个人资料维护")
    print("\t\t5. 返回登录菜单")
    print("\t\t6. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")


def login():
    '''用户登录：验证账号+密码是否正确，记录登录用户'''
    username = input("请输入账号：")
    password = input("请输入密码：")

    # 验证账号密码是否正确
    if username in users and password == users.get(username).get('password'):
        # 记录登录用户
        online = users.get(username)
        return True
    else:
        res = input("账号或者密码有误，按任意键重新输入(R返回)")
        if res == "R":
            return False
        else:
            return login()


def register():
    '''用户注册'''
    username = input("请输入账号：")
    if username in users:
        print("账号已经存在，请使用其他账号注册")
        return register()

    password = input("请输入密码：")
    confirm = input("请确认密码：")
    if password != confirm:
        print("两次密码输入不一致，请重新注册")
        return register()

    # 创建用户资料
    user = {'username': username, 'password': password, 'nickname': '待完善'}
    # 添加到系统中
    users[username] = user
    return True


def engine():
    '''流程控制引擎'''
    # 展示登录菜单
    show_login()

    # 用户输入选项
    choice = input("请输入选项：")

    if choice == "1":
        # 用户登录
        res = login()
        if res:
            # 展示首页菜单
            return show_index()
        else:
            # 重新展示登录菜单->重新开始流程
            return engine()

    elif choice == "2":
        # 用户注册：展示注册菜单
        show_register()
        # 用户注册流程
        res = register()
        if res:
            # 重新展示登录菜单:重新启动流程
            return engine()

    elif choice == "3":
        # 退出系统
        input("系统即将退出")
        sys.exit(1)

    else:
        input("没有这个选项")
        return engine()

# 程序启动
engine()
