from hashlib import sha1
import pymysqlhelper as sql
import time
# 累计登录次数
frequency = 0


def logon():
    """
    登录函数
    :return:
    """

    # 提示用户输入
    name = input("请输入账户：")
    pwd = input("请输入密码：")

    sha = sha1()
    pwd = pwd.encode("utf8")
    sha.update(pwd)
    pwd = sha.hexdigest()
    return testing(name, pwd)


def testing(name, pwd):
    """
    检测用户登录
    :return:
    """
    global frequency
    sqll = "select pwd from user where name=%s"
    uname = [name]
    sqlhelper = sql.MySqlHelper("zuoye").queryone(sqll, uname)
    # 判断用户输入
    if sqlhelper is None:
        if frequency >= 2:
            print("超出最大次数")
            time.sleep(1)
            exit(1)
        print("密码或用户名有误，请重新登录！")
        time.sleep(1)
        frequency += 1
        return logon()
    if sqlhelper[0] == pwd:
        print("登录成功！")
        time.sleep(1)
        exit(1)
    else:
        if frequency >= 3:
            print("超出最大次数")
            time.sleep(1)
            exit(1)
        print("密码或用户名有误，请重新登录！")
        time.sleep(1)
        frequency += 1
        return logon()


if __name__ == "__main__":
    logon()

