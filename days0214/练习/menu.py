"""
个人博客平台开发
    各种界面函数
"""
import models, time, os


def show_login():
    """登录菜单"""
    print("欢迎来到个人博客平台")
    print("~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~")
    print("1.用户登录")
    print("2.用户注册")
    print("3.退出系统")
    print("~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~")

    # 提示用户选择
    choice = input("请选择：")
    # 判断用户的选择
    if choice == "1":
        res = core.login()
        if res == "ok":
            """登录成功"""
            print("登录成功，正在跳转")
            time.sleep(1)
            return show_index()

        else:
            """登录失败"""
            input("您输入的账号或密码不正确，任意键重新登录")
            return show_login()

    elif choice == "2":
        """注册界面"""
        return show_register()

    elif choice == "3":
        """退出系统"""
        return core.logout()

    else:
        input("您的选择有误，任意键重新选择")
        return show_login()


def show_register():
    """注册界面"""
    print("根据提示完成注册")
    res = core.user_register()
    if res == "ok":
        # 注册成功
        input("注册成功！任意键继续")
        return show_login()
    else:
        # 注册失败
        print("注册失败...")
        return show_register()


def show_index():
    """
    首页菜单
    :return:
    """
    print(f"欢迎{core.online.username}来到个人博客首页")
    print("~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~")
    print("1.修改密码")
    print("2.维护个人资料")
    print("3.文章管理")
    print("4.退出登录")
    print("5.退出系统")
    print("~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~！~*~")

    # 提示用户选择
    choice = input("请选择服务：")

    if choice == "1":
        """修改密码"""
        res = core.online.user_change_password()
        if res == "ok":
            core.dump_data()
            print("修改成功！")
            return show_login()

        else:
            print("修改失败...")
            return show_index()

    elif choice == "2":
        """维护个人资料"""
        return show_user_information()

    elif choice == "3":
        """文章管理"""
        # TODO 待完善
        pass

    elif choice == "4":
        """退出登录"""
        print("正在退出...")
        time.sleep(1)
        return show_login()

    elif choice == "5":
        """退出系统"""
        core.logout()

    else:
        input("您的输入有误，任意键重新选择")
        return show_index()


def show_user_information():
    """展示个人资料"""
    print("昵称：", core.online.username)
    print("性别：", core.online.gender)
    print("年龄：", core.online.age)
    print("邮箱：", core.online.email)
    print("手机号：", core.online.phone)
    print("备注：", core.online.remark)
    res = core.online.user_perfect_information()
    if res == "error":
        print("退出资料维护")
        time.sleep(1)
        return show_index()
    core.dump_data()
    print("资料维护成功！")
    time.sleep(1)
    return show_index()


core = models.Core()


def engine():
    """程序引擎函数"""
    a = os.path.exists("./1.dat.bak")
    if not a:
        core.dump_data()
    core.load_data()
    show_login()
