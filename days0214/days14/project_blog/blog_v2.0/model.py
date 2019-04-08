"""
定义项目中需要的各种class类型
"""


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
        pass

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
        """用户退出"""
        pass