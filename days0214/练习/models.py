"""
个人博客平台开发
    程序中的各种类型
"""
import sys, os, time,random, shelve


class User:
    """
    创建用户类
    """

    def __init__(self, admin, username, password):
        """
        用户属性
        :param admin: 账号
        :param username: 用户名
        :param password: 密码
        """
        self.admin = admin
        self.username = username
        self.password = password
        # 用户性别
        self.gender = None
        # 年龄
        self.age = None
        # 邮箱
        self.email = None
        # 手机号
        self.phone = None
        # 用户是否激活
        self.is_active = True
        # 用户备注
        self.remark = None

    def user_change_password(self):
        """
        修改密码
        :return:
        """
        # TODO 待完善
        old_password = input("请输入旧密码：")
        if old_password != self.password:
            return self.user_change_password()

        new_password = input("请输入新密码：")
        confirm_password = input("请确认密码：")
        if new_password == confirm_password:
            self.password = new_password
            return "ok"

        else:
            return "error"

    def user_perfect_information(self):
        """
        完善个人资料
        :return:
        """
        # TODO 待完善
        username = input("请输入新昵称：（r退出修改）")
        if username.lower() == "r":
            return "error"
        self.username = username
        self.gender = input("请输入性别：")
        self.age = input("请输入年龄：")
        self.email = input("请输入邮箱：")
        self.phone = input("请输入手机号：")
        self.remark = input("请输入备注：")



class Core:
    """
    系统类
    """

    def __init__(self):
        # 用户数据
        self.users = dict()
        # 文章数据
        self.articles = dict()
        # 记录在线用户
        self.online = None

    def user_register(self):
        """
        用户注册
        :return: "ok"
        """
        admin = input("请输入账号")
        if admin in self.users:
            print("您要注册的账号已经存在，重新注册")
            return self.user_register()

        username = input("请输入昵称：")
        password = input("请输入密码：")
        sure_password = input("请确认密码：")
        if password != sure_password:
            input("你输入的两次密码不一致，任意键重新注册...")
            return self.user_register()

        user = User(admin, username, password)
        self.users[admin] = user
        self.dump_data()
        return "ok"

    def login(self):
        """
        用户登录
        :return: "ok" 或者 "error"
        """
        admin = input("请输入账号：")
        password = input("请输入密码：")
        if admin in self.users and password == self.users.get(admin).password:
            self.online = self.users[admin]
            return "ok"
        else:
            return "error"

    def logout(self):
        """
        退出系统
        :return: 无
        """
        i = 3
        while i >= 1:
            print(f"系统将在{i}秒后退出系统..")
            time.sleep(1)
            i -= 1
        sys.exit(1)

    def dump_data(self):
        """
        保存数据
        :return: 无
        """
        file = shelve.open("./1.dat")
        file["users"] = self.users
        file["articles"] = self.articles

    def load_data(self):
        """
        读取数据
        :return: 无
        """
        file = shelve.open("./1.dat")
        self.users = file["users"]
        self.articles = file["articles"]


core = Core()
