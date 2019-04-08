"""
个人博客平台开发
    程序中的各种类型
"""
import sys, time, shelve


class User:
    """
    创建用户类
    """
    # 限制用户的属性
    __slots__ = ["__admin", "__username", "__password", "__gender", "__age", "__email", "__phone",
                 "__is_active", "__remark"]

    # 声明类的属性
    def __init__(self, admin, username, password):
        """
        用户属性
        :param admin: 用户账号
        :param username: 用户昵称
        :param password: 用户账号密码
        """
        self.__admin = admin
        self.__username = username
        self.__password = password
        # 用户性别
        self.__gender = None
        # 年龄
        self.__age = None
        # 邮箱
        self.__email = None
        # 手机号
        self.__phone = None
        # 用户是否激活
        self.__is_active = True
        # 用户备注
        self.__remark = None

    def set_admin(self, admin):
        self.__admin = admin

    def get_admin(self):
        return self.__admin

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def set_is_active(self, is_active):
        self.__is_active = is_active

    def get_is_active(self):
        return self.__is_active

    def set_remark(self, remark):
        self.__remark = remark

    def get_remark(self):
        return self.__remark

    def user_change_password(self):
        """
        修改密码
        :return:
        """
        old_password = input("请输入旧密码：")
        if old_password != self.get_password():
            print("密码输入错误")
            return "error"

        new_password = input("请输入新密码：")
        confirm_password = input("请确认密码：")
        if new_password == confirm_password:
            self.set_password(new_password)
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
        self.set_username(username)
        self.set_gender(input("请输入性别："))
        self.set_age(input("请输入年龄："))
        self.set_email(input("请输入邮箱："))
        self.set_phone(input("请输入手机号："))
        self.set_remark(input("请输入备注："))


class Core:
    """
    系统类
    """

    def __init__(self):
        # 用户数据
        self.__users = dict()
        # 文章数据
        self.__articles = dict()
        # 记录在线用户
        self.__online = None

    def set_users(self, users):
        self.__users = users

    def get_users(self):
        return self.__users

    def set_articles(self, articles):
        self.__articles = articles

    def get_articles(self):
        return self.__articles

    def set_online(self, online):
        self.__online = online

    def get_online(self):
        return self.__online

    def add_user(self, user):
        """添加用户的方法"""
        self.__users[user.get_admin()] = user

    def user_register(self):
        """
        用户注册
        :return: "ok"
        """
        admin = input("请输入账号")
        if admin in self.get_users():
            print("您要注册的账号已经存在，重新注册")
            return self.user_register()

        username = input("请输入昵称：")
        password = input("请输入密码：")
        sure_password = input("请确认密码：")
        if password != sure_password:
            input("你输入的两次密码不一致，任意键重新注册...")
            return self.user_register()

        user = User(admin, username, password)
        self.add_user(user)
        self.dump_data()
        return "ok"

    def login(self):
        """
        用户登录
        :return: "ok" 或者 "error"
        """
        # 提示用户输入账号
        admin = input("请输入账号：")
        # 提示用户输入密码
        password = input("请输入密码：")

        # 判断用户输入的账号和密码是否正确
        if admin in self.get_users() and password == self.get_users().get(admin).get_password():
            self.set_online(self.get_users()[admin])
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
        file["users"] = self.get_users()
        file["articles"] = self.get_articles()

    def load_data(self):
        """
        读取数据
        :return: 无
        """
        file = shelve.open("./1.dat")
        self.set_users(file["users"])
        self.set_articles(file["articles"])


core = Core()
