"""

本平台采用函数基础，面向过程开发
"""
import time,sys
# 声明一个用户字典
users = dict()
# 定义一个在线用户
temp = None


def show_login():
    """展示登录界面"""
    print("\t\t个人博客登录")
    print()
    print("\t1.用户登录")
    print("\t2.用户注册")
    print("\t3.退出系统")
    print()
    # 提示用户输入
    choice = input("请选择服务：")
    choice = choice.strip()
    # 判断用户的选择
    return login_menu_dict.get(choice)() if choice in login_menu_dict else show_login()


def show_register():
    """"展示注册菜单"""
    print("\t\t欢迎来到个人博客注册界面")
    print()
    print("根据提示完成用户信息资料填写")
    print("创建个人博客账户，享受大千世界的精彩吧。")
    print()
    # 引入注册函数
    return register()


def login():
    """登录功能"""
    admin = input("请输入账号：(退出R)")
    if admin.upper() == "R":
        return show_login()

    password = input("请输入密码：(退出R)")

    if password.upper() == "R":
        return show_login()

    if admin in users and password == users.get(admin).get("password"):
        # 记录登录用户
        global temp
        temp = users.get(admin)
        print("登录成功！")
        return show_index()

    else:
        res = input("您输入的账户或密码不正确，任意键重新输入(退出R)")
        if res.upper() == "R":
            return show_login()

        else:
            return login()


def show_index():
    """"展示首页菜单"""
    print("欢迎%s来到个人博客首页" % users.get(temp).get("username"))
    print()
    print("\t\t1.个人资料维护")
    print("\t\t2.查看所有文章")
    print("\t\t3.查看个人文章")
    print("\t\t4.写文章")
    print("\t\t5.退出登录")
    print("\t6.退出系统")
    print()


def register():
    """注册功能"""
    admin = input("请输入注册账号：")

    if admin in users:
        res = input("您注册的用户已经存在,退出R，任意键继续")
        if res == "R":
            return show_login()

        else:
            return register()

    password = input("请输入密码：")
    password1 = input("请确认密码：")
    if password == password1:
        # 添加一个用户
        user = {"admin": admin, "password": password}
        # 将用户添加到用户字典里
        users[admin] = user
        print("用户添加成功!")
        time.sleep(1)
        return show_login()

    else:
        print("密码不一致请重新注册！")
        return register()


def sys_system():
    x = 3
    for i in range(1, 4):
        time.sleep(1)
        print("系统", x, "秒后退出...")
        x -= 1
        if x == 0:
            print("退出成功！")
            break
    sys.exit()


login_menu_dict = {
    "1": login,
    "2": show_register,
    "3": sys_system
}


def engine():
    """流程控制"""
    show_login()


engine()
