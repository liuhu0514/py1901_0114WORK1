"""
个人博客面向对象简单开发
    OOA:
        对象：用户，系统
        展示菜单【登录界面，注册界面，首页菜单，修改密码界面，个人资料管理】
    OOD：
        类型
        用户 User
        系统 Core
        行为
        用户：【修改密码，个人资料管理】
        系统：【登录，注册，退出系统】
"""
import shelve, os, time


class User:
    """
    定义用户类型
    """
    def __init__(self, admin, username, password):
        """
        初始化用户属性
        :param admin: 用户账号
        :param username: 用户名
        :param password: 用户密码
        """
        self.admin = admin
        self.username = username
        self.password = password

    def change_password(self):
        """
        修改密码的行为
        :return: 返回登录界面
        """
        # TODO
        pass

    def data_maintenance(self):
        """
        个人资料维护
        :return: 返回上一页
        """
        pass


class Core:
    """
    定义系统类型
    """
    def register(self):
        """
        注册功能
        :return:
        """
        global users
        admin = input("请输入账号：")
        username = input("请输入用户名：")
        password = input("请输入密码：")
        u = User(admin, username, password)
        # user = dict()
        # user[admin] = u
        users.append(u)
        print("注册成功！")
        self.save_data()
        show_login()

    def save_data(self):
        """
        将程序中的数据保存到文件中
        :return:
        """
        global users
        file = shelve.open("./data/1.dat")
        file["users"] = users

    def get_data(self):
        """
        读取文件数据到程序中
        :return:
        """
        global users
        file = shelve.open("./data/1.dat")
        users = file["users"]

    def exit_system(self):
        """
        退出系统行为
        :return: 退出程序
        """
        # 引入与系统交互的函数
        import sys, time
        print("系统正在退出请稍等...")
        self.save_data()
        time.sleep(3)
        sys.exit(1)

    def login(self):
        """
        登录功能
        :return:
        """
        admin = input("请输入账号：")
        password = input("请输入密码：")
        for u in users:
            if u.admin == admin:
                if password == u.password:
                    print("登录成功！")
                    time.sleep(1)
                    return show_main()

        else:
            print("您输入的账号或密码有误，请重新输入...")
            self.login()


def show_login():
    """
    展示登录界面
    :return:无
    """
    print("欢迎来到个人博客平台")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("1.用户登录")
    print("2.用户注册")
    print("3.退出系统")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")

    # 提示用户输入
    choice = input("请输入选项：")

    # 判断用户输入
    if choice == "1":
        # 进入登录
        return show_login_jiemian()

    elif choice == "2":
        # 进入注册界面
        return show_register()

    elif choice == "3":
        # 退出系统
        c = Core()
        c.exit_system()

    else:
        input("您的输入有误，任意键继续...")
        return show_login()


def show_register():
    """
    展示注册界面
    :return:
    """
    print("欢迎来到个人博客注册界面")
    print("根据提示输入信息！")
    c = Core()
    c.register()
    show_login()


def show_main():
    """
    展示个人首页界面
    :return:
    """
    print("欢迎%s来到个人博客平台")
    print("1.资料维护")
    print("2.修改密码")
    print("3.退出登录")
    print("4.退出系统")

    # 提示用户选择
    choice = input("请选择服务：")

    # 判断用户输入
    if choice == "1":
        pass

    elif choice == "2":
        pass

    elif choice == "3":
        return show_login()

    elif choice == "4":
        Core().exit_system()

    else:
        input("您的输入有误，任意键继续...")
        return show_main()


def show_data_maintenance():
    """
    展示个人资料维护界面
    :return:
    """
    pass


def show_login_jiemian():
    print("欢迎登录个人博客")
    print("根据提示填写信息，进行登录")
    c = Core()
    c.login()


users = list()


def qi_dong():
    n = os.path.exists("./data/1.dat.bak")
    if not n:
        Core().save_data()

    c = Core()
    c.get_data()
    return show_login()


qi_dong()
