"""
各种界面函数
"""
import models
import data
import time
import os
core = models.core
super1 = models.super1


def show_login():
    """登录菜单"""
    print("欢迎来到个人博客平台")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("1.用户登录")
    print("2.管理员登录")
    print("3.超级管理员登录")
    print("4.用户注册")
    print("5.账号申请解锁")
    print("6.退出系统")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")

    # 提示用户选择
    choice = input("请选择：")
    # 判断用户选择
    if choice == "1" or choice == "2" or choice == "3":
        return show_user_login(choice)

    elif choice == "4":
        return show_register()

    elif choice == "5":
        """账号申请解锁"""
        return show_sq_open()

    elif choice == "6":
        return core.sign_out()

    else:
        input("您的选择有误，任意键继续")
        return show_login()


def show_user_login(choice):
    """登录界面"""
    print(f"欢迎来到{data.data_login.get(choice)}登录界面")
    admin = input(f"请输入{data.data_login.get(choice)}账号：(r退出)")
    if admin == "r":
        return quit_show_login()

    password = input(f"请输{data.data_login.get(choice)}密码：(r退出)")
    if password == "r":
        return quit_show_login()

    res = core.login(choice, admin, password)

    if res == choice:
        if res == "1":
            return show_index()
        else:
            return show_manager_index()

    elif res == "suo_ding":
        input("您的账号已经被锁定，请赶快去申请解锁,任意键继续..")
        return show_login()

    else:

        res = input("您输入的账号或密码不正确，任意键继续:(r退出)")
        if res.lower() == "r":
            return quit_show_login()
        return show_user_login(choice)


def show_register():
    """用户注册界面"""
    print("根据提示输入信息，完成用户注册")
    res = core.user_register()
    if res == "quit":
        return quit_show_login()

    elif res == "ok":
        print("注册成功！")
        core.dump_data()
        return quit_show_login()

    else:
        return show_register()


def show_add_manager():
    """添加管理员界面"""
    print("欢迎来到添加管理员界面,根据提示完成管理员添加")
    res = super1.add_manager()
    if res == "ok":
        core.dump_data()
        print("添加成功！")
        time.sleep(1)
        return show_manager_index()

    elif res == "quit":
        print("正在退出...")
        time.sleep(1)
        return show_manager_index()

    else:
        print("您要添加的管理员已经存在，请添加其他账号...")
        time.sleep(1)
        return show_add_manager()


def show_index():
    """个人首页界面"""
    print(f"欢迎{core.get_online().get_username()}来到个人博客个人首页")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("1.修改密码")
    print("2.完善资料")
    print("3.退出登录")
    print("4.退出系统")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    # 提示用户输入
    choice = input("请选择：")

    if choice == "1":
        """修改密码"""
        print("欢迎来到修改密码界面")
        return show_change_password()

    elif choice == "2":
        """完善个人资料"""
        return show_user_information()

    elif choice == "3":
        return quit_show_login()

    elif choice == "4":
        return core.sign_out()

    else:
        input("您的选择有误，任意键继续")
        return show_index()


def show_manager_index():
    """管理员首页界面"""
    print(f"欢迎管理员{core.get_online().get_username()}来到个人博客管理员首页")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("1.修改密码")
    print("2.管理用户")
    print("3.管理管理员")
    print("4.退出登录")
    print("5.退出系统")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")

    # 提示用户选择
    choice = input("请选择：")
    # 判断用户输入
    if choice == "1":
        if core.get_online().get_power() is True:
            input("您是超级管理员，不能修改密码，任意键继续。。。")
            return show_manager_index()
        return show_change_password()

    elif choice == "2":
        """管理用户"""
        return show_user_manage()

    elif choice == "3":
        """管理管理员"""
        if core.get_online().get_power() is True:
            return show_manager_manager()

        else:
            input("您没有该权限，任意键继续。。。")
            return show_manager_index()

    elif choice == "4":
        """退出登录"""
        return quit_show_login()

    elif choice == "5":
        """退出系统"""
        return core.sign_out()

    else:
        input("您的选择有误，任意键继续")
        return show_manager_index()


def show_user_information():
    """展示个人资料"""
    print("以下是您的个人资料")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("账号：", core.get_online().get_admin())
    print("昵称：", core.get_online().get_username())
    print("性别：", core.get_online().get_gender())
    print("年龄：", core.get_online().get_age())
    print("邮箱：", core.get_online().get_email())
    print("手机号：", core.get_online().get_phone())
    print("备注：", core.get_online().get_remark())
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    # 提示用户是否修改资料
    res = input("是否修改资料：修改y,任意键退出")
    if res.lower() == "y":
        res = core.get_online().change_information()
        if res == "ok":
            print("修改成功！")
            core.dump_data()
            return show_user_information()
        else:
            print("修改失败！")
            return show_user_information()

    else:
        return show_index()


def quit_show_login():
    """退出到登录菜单"""
    print("正在退出...")
    time.sleep(1)
    return show_login()


def show_change_password():
    """修改密码界面"""
    res = core.get_online().change_password()
    if res == "ok":
        # 修改成功
        core.dump_data()
        print("修改成功！请重新登录")
        return show_login()

    elif res == "error":
        # 密码输入错误
        return show_change_password()

    else:
        if isinstance(core.get_online(), models.Manager):
            return show_manager_index()

        return show_index()


def show_user_manage():
    """用户管理界面"""
    print("欢迎来到个人博客用户管理界面")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("所有的用户如下：")
    for i in core.get_users().keys():
        print(i, end=",")
    print()
    print("1.删除用户")
    print("2.添加用户")
    print("3.查询用户信息")
    print(f"4.申请解锁的用户({len(core.get_sq_user())})")
    print("5.解锁用户")
    print("6.锁定用户")
    print("7.返回上一级")
    print()
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    # 提示用户选择
    choice = input("请选择：")
    if choice == "1":
        print()
        print("欢迎来到个人博客删除用户界面")
        print()
        admin = input("请输入要删除用户的账号：")
        if admin in core.get_users():
            core.delete_user(admin)
            input("删除成功！任意键继续")
            core.dump_data()
            return show_user_manage()
        else:
            print("删除失败")
            input("你要的账号不存在，任意键继续")
            return show_user_manage()

    elif choice == "2":
        """添加用户"""
        return show_add_user()

    elif choice == "3":
        return show_find_user()

    elif choice == "4":
        """申请解锁的用户"""
        return show_sq_user()

    elif choice == "7":
        print("正在返回上一级...")
        time.sleep(1)
        return show_manager_index()

    elif choice == "5":
        """解锁账号"""
        return show_jie_suo()

    elif choice == "6":
        """锁定账号"""
        res = super1.suo_zhu()
        if res == "ok":
            print("用户锁定成功！")
            core.dump_data()
            time.sleep(1)
            return show_user_manage()

        else:
            print("锁定失败，您要锁定的用户账号可能不存在...")
            time.sleep(1)
            return show_user_manage()

    else:
        input("您的输入有误，任意键继续")
        return show_user_manage()


def show_add_user():
    """添加用户界面"""
    print()
    print("欢迎来到个人博客添加用户界面")
    print()
    # 提示用户输入要添加的账号
    admin = input("请输入要添加的账号：")
    if admin in core.get_users():
        print("您输入的用户已经存在...")
        return show_user_manage()
    username = input("请输入昵称：")
    password = input("请输入密码：")
    user = models.User(admin, username, password)
    core.add_user(user)
    print("添加成功！")
    core.dump_data()
    time.sleep(1)
    return show_user_manage()


def show_manager_manager():
    """管理员管理界面"""
    print("欢迎来到管理管理员界面")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")
    print("以下是所有管理员")
    for i in core.get_managers().keys():
        print(i, ",", end="")
    print()
    print("1.添加管理员")
    print("2.删除管理员")
    print("3.返回上一级")
    print("~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~!~*~")

    choice = input("请选择:")

    # 判断用户输入
    if choice == "1":
        return show_add_manager()

    elif choice == "2":
        res = core.get_online().delete_manager()
        if res == "ok":
            print("删除成功！")
            core.dump_data()
            time.sleep(1)
            return show_manager_index()

        elif res == "error":
            print("正在退出...")
            time.sleep(1)
            return show_manager_index()

        else:
            input("删除失败，您要删除的用户可能不存在，任意键结束。。")
            return show_manager_manager()

    elif choice == "3":
        print("正在返回上一级...")
        time.sleep(1)
        return show_manager_index()

    else:
        print("您的输入有误，请重新输入")
        time.sleep(1)
        return show_manager_manager()


def show_sq_open():
    """用户申请解锁界面"""
    admin = input("请输入申请解锁的账号：")
    # TODO 申请解锁
    # 判断用户是否存在
    if admin in core.get_users() and core.get_users().get(admin).get_suo() is False:
        # 判断用户是否已经申请过解锁
        if admin in core.get_sq_user():
            input("该账号正在审核中，请耐心等待，任意键返回...")
            return show_login()
        else:
            core.add_sq_user(admin)
            core.dump_data()
            input("账号解锁申请已发送：等待管理员审核,任意键返回...")
            return show_login()

    elif admin in core.get_users() and core.get_users().get(admin).get_suo() is True:
        input("您的账号当前时解锁状态，请放心登录，任意键返回...")
        return show_login()

    else:
        input("申请失败，您输入的账号可能不存在，任意键返回...")
        return show_login()


def show_sq_user():
    """查看申请解锁界面"""
    print("以下是申请解锁的用户")
    for i in core.get_sq_user():
        print(i, "；", end="")
    print()
    return show_jie_suo()


def show_jie_suo():
    """解锁用户界面"""
    res = super1.jie_suo()
    if res == "ok":
        print("解锁成功！")
        core.dump_data()
        time.sleep(1)
        return show_user_manage()

    else:
        print("修改失败：您要解锁的账号不存在...")
        time.sleep(1)
        return show_user_manage()


def show_find_user():
    """查看用户信息"""
    res = super1.find_user_information()
    if res == "ok":
        input("任意键退出查看...")
        return show_user_manage()

    elif res == "quit":
        print("正在退出...")
        time.sleep(1)
        return show_user_manage()

    else:
        input("您要查看的账号可能不存在，任意键继续查看")
        return show_find_user()


def engine():
    a = os.path.exists("./1.dat.bak")
    if not a:
        core.dump_data()
    core.load_data()
    return show_login()
