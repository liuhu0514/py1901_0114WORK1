'''
个人博客开发
    面向对象 + 面向过程
'''
# 引入项目中依赖的模块
import os, sys, time, random

# 从当前文件夹中的model.py中，导入一个Core类型
# from .model import Core

# 从当前文件夹中导入一个model.py文件
import model


def show_login():
    """展示登录菜单"""
    # TODO 展示登录菜单，提示用户输入选项
    res = input("登录菜单 1 登录  2 注册")

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
core = model.Core()


# 程序运行入口
def engine():
    # 展示登录菜单
    show_login()


# 启动程序
engine()