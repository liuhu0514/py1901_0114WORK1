"""
个人博客各种类
    用户类:User
    系统类:Core
    管理员类:Manager
    超级管理员类：Super_manager
"""
import time, shelve, sys


class User:
    """
    用户类
    """

    def __init__(self, admin, username, password):
        """
        初始化用户属性
        :param admin: 用户账号
        :param username: 用户昵称
        :param password: 用户密码
        """
        self.__admin = admin
        self.__username = username
        self.__password = password
        self.__suo = False

        # 用户性别
        self.__gender = None
        # 年龄
        self.__age = None
        # 邮箱
        self.__email = None
        # 手机号
        self.__phone = None
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

    def set_remark(self, remark):
        self.__remark = remark

    def get_remark(self):
        return self.__remark

    def get_suo(self):
        return self.__suo

    def set_suo(self, suo):
        self.__suo = suo

    def jie_suo(self):
        """解锁"""
        self.__suo = True

    def suo_zhu(self):
        """锁定"""
        self.__suo = False

    def change_password(self):
        """修改密码"""
        old_password = input("请输入旧密码：")
        if old_password != core.get_online().get_password():
            print("您输入的密码不对，请重新输入")
            time.sleep(1)
            return "error"

        new_password = input("请输入新密码：")
        confirm_password = input("请确认密码：")
        if new_password == confirm_password:
            self.set_password(new_password)
            return "ok"
        else:
            print("密码输入不一致，修改失败")
            time.sleep(1)
            return "fail"

    def change_information(self):
        """修改资料"""
        self.set_username(input(f"将旧昵称{self.get_username()}改为："))
        self.set_gender(input(f"将旧性别{self.get_gender()}改为："))
        self.set_age(input(f"将旧年龄{self.get_age()}改为："))
        self.set_email(input(f"将旧邮箱{self.get_email()}改为："))
        self.set_phone(input(f"将旧手机号{self.get_phone()}改为："))
        self.set_remark(input(f"将旧备注{self.get_remark()}改为："))
        return "ok"


class Core:
    """系统类"""
    def __init__(self):
        self.__users = dict()
        self.__online = dict()
        self.__managers = dict()
        self.__sq_user = list()

    def del_sq_user(self, admin):
        """删除申请解锁的用户"""
        self.__sq_user.remove(admin)

    def set_sq_user(self, sq_user):
        self.__sq_user = sq_user

    def get_sq_user(self):
        """查看申请解锁的所有用户"""
        return self.__sq_user

    def add_sq_user(self, sq_user):
        """添加申请解锁的用户"""
        self.__sq_user.append(sq_user)

    def set_users(self, users):
        self.__users = users

    def get_users(self):
        return self.__users

    def add_user(self, user):
        """添加用户"""
        self.__users[user.get_admin()] = user

    def find_user(self, admin):
        """查看用户"""
        return self.get_users().get(admin)

    def set_online(self, online):
        self.__online = online

    def get_online(self):
        return self.__online

    def set_managers(self, managers):
        self.__managers = managers

    def get_managers(self):
        return self.__managers

    def add_manager(self, manager):
        """添加管理员"""
        self.__managers[manager.get_admin()] = manager

    def delete_user(self, admin):
        """删除用户"""
        self.__users.pop(admin)

    def delete_manager(self, admin):
        """删除管理员"""
        self.__managers.pop(admin)
        return "ok"

    def user_register(self):
        admin = input("请输入要注册的用户账号:(r退出注册)")
        # 判断用户是否存在
        if admin in core.get_users():
            res = input("您输入的用户账号已经存在，请使用其他账号注册，任意键继续(r退出注册)")
            if res.lower() == "r":
                return "quit"
            else:
                return "error"
        elif admin.lower() == "r":
            return "quit"
        username = input("请输入昵称：(r退出注册)")
        if username.lower() == "r":
            return "quit"
        password = input("请输入密码：(r退出注册)")
        if password.lower() == "r":
            return "quit"
        user = User(admin, username, password)
        self.add_user(user)
        return "ok"

    def login(self, choice, admin, password):

        # 判断是什么用户登录
        if choice == "1":
            # 普通用户登录
            if admin in core.get_users() and password == core.get_users().get(admin).get_password():
                if core.get_users().get(admin).get_suo() is True:
                    user = self.get_users().get(admin)
                    # 存储登录用户
                    self.set_online(user)
                    return choice
                else:
                    return "suo_ding"
            else:
                return "error"
        elif choice == "2":
            # 管理员登录
            if admin in core.get_managers() and password == core.get_managers().get(admin).get_password():
                # 存储登录用户
                self.set_online(self.get_managers().get(admin))
                return choice
            else:
                return "error"
        else:
            # 超级管理员登录
            if admin == super1.get_admin() and password == super1.get_password():
                # 存储登录用户
                self.set_online(super1)
                return choice

            else:
                return "error"

    def sign_out(self):
        """退出系统"""
        self.dump_data()
        i = 3
        while i >= 1:
            print(f"系统将在{i}秒后退出...")
            time.sleep(1)
            i -= 1
        print("退出系统成功！")
        sys.exit(1)

    def dump_data(self):
        """保存数据"""
        file = shelve.open("./1.dat")
        file["users"] = self.get_users()
        file["managers"] = self.get_managers()
        file["sq_user"] = self.get_sq_user()

    def load_data(self):
        """读取数据"""
        file = shelve.open("./1.dat")
        self.set_users(file["users"])
        self.set_managers(file["managers"])
        self.set_sq_user(file["sq_user"])


class Manager(User):
    """管理员类"""
    def __init__(self, admin, username, password):
        super().__init__(admin, username, password)
        self.__power = False

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power


class Super_manager():
    """超级管理员"""
    def __init__(self):
        self.__admin = "123"
        self.__username = "大神"
        self.__password = "123"
        self.__power = True

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

    def set_power(self):
        self.__power = True

    def get_power(self):
        return self.__power

    def add_manager(self):
        """添加管理员"""
        admin = input("请输入要添加的管理员账号:(r退出)")
        if admin.lower() == "r":
            return "quit"
        elif admin in core.get_managers():
            return "error"
        username = input("请输入昵称：")
        password = input("请输入密码：")
        manager = Manager(admin, username, password)
        core.add_manager(manager)
        return "ok"

    def delete_manager(self):
        """删除管理员"""
        admin = input("请输入要删除的管理员的账号：(r退出)")
        if admin.lower() == "r":
            return "quit"
        elif admin in core.get_managers():
            res = core.delete_manager(admin)
            if res == "ok":
                return "ok"
            else:
                return "error"

        else:
            return "error"

    def jie_suo(self):
        admin = input("请输入要解锁的用户账号：")
        if admin in core.get_users():
            core.get_users().get(admin).jie_suo()
            if admin in core.get_sq_user():
                core.del_sq_user(admin)
                return "ok"
            else:
                return "ok"
        else:
            return "error"

    def suo_zhu(self):
        admin = input("请输入要锁定的账号：")
        if admin in core.get_users():
            core.get_users().get(admin).suo_zhu()
            return "ok"

        else:
            return "error"

    def find_user_information(self):
        admin = input("请输入您要查看的用户的账号：(退出r)")
        if admin.lower() == "r":
            return "quit"

        elif admin in core.get_users():
            print("账号：", core.find_user(admin).get_admin())
            print("昵称：", core.find_user(admin).get_username())
            print("性别：", core.find_user(admin).get_gender())
            print("年龄：", core.find_user(admin).get_age())
            print("邮箱：", core.find_user(admin).get_email())
            print("手机号：", core.find_user(admin).get_phone())
            print("用户状态：", core.find_user(admin).get_suo())
            print("备注：", core.find_user(admin).get_remark())
            return "ok"
        else:
            return "error"


core = Core()
super1 = Super_manager()
