'''
个人博客开发
    面向对象 + 面向过程
'''
# 引入项目中依赖的模块
import os, sys, time, random


class User:
    """
    用户类型
    """

    def __init__(self, username, password, nickname):
        """初始化用户属性数据"""
        self.username = username
        self.password = password
        self.nickname = nickname

        self.gender = "待完善"
        self.age = 0
        self.email = "待完善"
        self.phone = "待完善"
        self.is_active = True
        self.remark = "待完善"

    def user_change_password(self):
        """修改用户登录密码"""
        # 用户输入旧密码
        old_password = input("输入旧密码：")
        if old_password != self.password:
            print("输入旧密码有误..")
            return self.user_change_password()
        # 用户输入新密码
        # new_password = ...
        # 确认新密码
        # confirm_password = ....
        # if new_password == confirm_password ...
            # 修改当前用户属性数据
            # self.password = new_password
            # return "ok"
        # 返回结果
        #  return "error"



    def user_perfect_information(self):
        """完善用户资料"""
        pass


class Core:
    """系统核心类型"""

    def __init__(self):
        # 记录系统中所有的注册用户
        self.users = dict()
        # 记录系统中所有文章数据
        self.articles = dict()
        # 记录登录用户
        self.online = None

    def register(self):
        """用户注册"""
        # 提示用户输入注册信息
        username = input("请输入账号：")
        if username in self.users:
            print("账号已经存在...")
            return self.register()

        password = input("请输入密码：")
        nickname = input("请输入昵称：")

        # 创建并注册对象
        user = User(username, password, nickname)
        self.users[username] = user

        return "ok"

    def login(self):
        """用户登录"""
        # 提示用户输入账号+密码
        username = input("请输入账号：")
        password = input("请输入密码：")
        # 验证账号+密码是否正确
        if username in self.users and password == self.users.get(username).password:
            # 登录成功
            self.online = self.users.get(username)
            return "ok"
        else:
            res = input("账号或者密码有误.按R键返回登录菜单")
            if res.upper() == "R":
                return "error"
            # 重新输入账号密码进行登录
            return self.login()

    def logout(self):
        """退出系统"""
        i = 0
        while i <= 2:
            print(f"系统将在{3-i}秒后退出")
            i += 1
            time.sleep(1)
        sys.exit(1)


def show_login():
    """展示登录菜单"""
    # TODO 展示登录菜单，提示用户输入选项
    print("欢迎来到个人博客平台")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("1.用户登录")
    print("2.用户注册")
    print("3.退出系统")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    # 提示用户选择
    res = input("请选择服务：")

    if res == "1":
        # 如果用户选择登录
        res = core.login()
        if res == "ok":
            # 登录成功，展示首页
            return show_index()

        else:
            # 登录失败，返回登录菜单
            return show_login()
    elif res == "2":
        # 用户注册
        return show_register()

    elif res == "3":
        return core.logout()


def show_register():
    """展示注册菜单"""
    # TODO 展示注册提示信息
    print("注册菜单")

    # 用户注册：
    res = core.register()
    if res == "ok":
        # 注册成功
        return show_login()
    else:
        # 注册失败
        return show_register()


def show_index():
    """展示首页菜单"""
    # TODO 展示首页菜单，完成功能处理
    print("测试语句：尊敬的用户%s，欢迎访问本系统" % core.online.nickname)
    print("测试语句：尊敬的用户{}，欢迎访问本系统".format(core.online.nickname))
    input(f"测试语句：尊敬的用户{core.online.nickname}，欢迎访问本系统")


# 系统运行~全局数据，存储在系统类型中，创建系统对象
core = Core()


# 程序运行入口
def engine():
    # 展示登录菜单
    show_login()


# 启动程序
engine()