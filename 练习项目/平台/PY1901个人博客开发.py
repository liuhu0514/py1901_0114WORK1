"""
博客项目
登录菜单
注册菜单
首页菜单
查看所有文章菜单
查看个人文章菜单
查看文章详情

登录
注册
退出系统
发表文章

定义一个用户字典
users = dict()
user={"admin":admin,"password":password,"usenamrname":usere}
定义一个临时在线用户
online = None
文章articles = dict('标题': a1)
        a1 = {'title': '标题', author: admin, content='内容', read_count: 0}
"""

import sys,time


# 定义函数
def show_login():
    # 登录菜单
    print("欢迎来到PY1901个人博客")
    print("")
    print("\t\t1.用户登录")
    print("\t\t2.用户注册")
    print("\t\t3.退出系统")

    # 提示用户选择
    choice = input("请选择选项：")

    # 判断用户选择 并跳转
    return login_menu_dict.get(choice)() if choice in login_menu_dict else show_login()


# 展示注册菜单
def show_register():
    # 展示注册菜单
    print("系统用户注册")
    print()
    print("\t\t欢迎来到PY1901个人博客平台")
    print()
    print("根据提示完成用户资料填写,完成注册")
    print("祝您体验愉快")

    time.sleep(1)

    # 用户开始注册
    return register()


# 展示首页菜单
def show_index():
    # 展示首页菜单
    print("欢迎{}来到PY1901个人博客平台".format(users.get(online.get("admin")).get("username")))
    print()
    print("\t\t1.查看全部文章")
    print("\t\t2.查看个人文章")
    print("\t\t3.发表文章")
    print("\t\t4.个人文章管理")
    print("\t\t5.查看回收站")
    print("\t\t6.维护个人资料")
    print("\t\t7.切换用户")
    print("\t\t8.返回登录界面")
    print("\t\t9.退出系统")

    # 用户选择
    choice = input("请选择选项：")

    # 判断用户选择并跳转
    return index_menu_dict.get(choice)() if choice in index_menu_dict else show_index()


# 回收站
def recycle_bin():
    # 展示回收站
    print("标题\t\t作者")
    for title_key in recycle_bin_dict.keys():
        if recycle_bin_dict.get(title_key).get("author") == online.get("username"):
            print(title_key, "\t", recycle_bin_dict.get(title_key).get("author"))
    print("1.清空回收站")
    print("2.返回上一级")
    print("3.删除文章")
    print("4.找回文章")
    print("根据提示完成操作")
    # 提示用户选择
    choice = input("请选择操作：")

    return recycle_manage_dict.get(choice)() if choice in recycle_manage_dict else recycle_bin()


# 清空回收站
def clear_bin():
    """清空回收站"""
    print("正在清空回收站...")
    recycle_bin_dict.clear()
    time.sleep(1)
    print("回收站已清空!")
    return show_index()


# 删除回收站文章
def delete_bin_wen():
    """删除回收站文章"""
    # 展示回收站自己的所有文章
    print("标题\t\t作者")
    for title_key in recycle_bin_dict.keys():
        if recycle_bin_dict.get(title_key).get("author") == online.get("username"):
            print(title_key, "\t", recycle_bin_dict.get(title_key).get("author"))

    title = input("请输入要删除的文章标题：（退出R）")
    if title == "R":
        return show_index()

    else:
        recycle_bin_dict.pop(title)
        print("正在删除中...")
        time.sleep(1)
        print("删除成功!")
        return show_index()


# 找回文章
def retrieve_wen():
    print("欢迎来到PY1901博客找回文章界面")
    # 展示回收站自己的所有文章
    print("标题\t\t作者")
    for title_key in recycle_bin_dict.keys():
        if recycle_bin_dict.get(title_key).get("author") == online.get("username"):
            print(title_key, "\t", recycle_bin_dict.get(title_key).get("author"))

    title = input("请输入您要找回文章的标题：（返回r）")
    if title == "R":
        return recycle_bin()

    else:
        if title in recycle_bin_dict:
            print("正在找回...")
            time.sleep(1)
            all_articles[title] = recycle_bin_dict[title]
            print("找回成功！")
            return recycle_bin()
        else:
            print("您要找回的文章不存在，请重新输入...")
            time.sleep(1)
            return retrieve_wen()


# 个人文章管理
def wen_manage():
    """管理个人文章"""
    # 展示管理界面
    print("欢迎来到个人文章管理")
    print()
    print("你所有文章如下")
    print("标题\t\t作者")
    for title_key in all_articles.keys():
        if all_articles.get(title_key).get("author") == online.get("username"):
            print(title_key, "\t", all_articles.get(title_key).get("author"))

    title = input("请输入您要管理的文章：(返回R)")
    if title.upper() == "R":
        return show_index()

    else:
        # 判断用户输入的标题是否存在，并展示文章
        if title in all_articles:
            return change_wen(title)

        else:
            print("没有该文章,请重新查看.")
            time.sleep(1)
            return wen_manage()


# 展示要修改文章的详情
def change_wen(title):
    """展示要修改的文章"""
    print("欢迎来到个人文章管理")
    # 获取文章详情
    article = all_articles.get(title)
    # 展示文章详情
    print("文章标题：{}".format(article.get("title")))
    print("作者：{}".format(article.get("author")))
    print("阅读次数：{}".format(article.get("read_count")))
    print("文章内容如下：\n\t{}".format(article.get("content")))
    print()
    print("1.修改")
    print("2.删除")
    print("3.退出管理")
    # 选择操作模式
    choice = input("请输入选项：")
    # 判断用户选择
    return manage_wen.get(choice)(title, choice) if choice in manage_wen else change_wen(title)


# 修改文章
def xiu_gai(title, choice):
    if choice == "3":
        return show_index()
    xin_wen = input("请输入修改后的文章内容:(退出R)")
    if xin_wen == "R":
        return show_index()
    all_articles[title]["content"] = xin_wen
    print("修改成功1")
    time.sleep(1)
    return show_index()


# 删除文章
def delete_wen(title, choice):
    if choice == "3":
        return show_index()
    """删除文章功能"""
    x = all_articles.pop(title)
    recycle_bin_dict[title] = x
    print("删除成功！")
    time.sleep(1)
    show_index()


# 查看所有文章
def look_articles():
    # 查看所有文章
    # 循环查询所有文章标题
    print("\t\t标题\t\t作者")
    for title_key in all_articles.keys():
        print(title_key, "\t\t", all_articles.get(title_key).get("author"))

    title = input("请输入您要查看的文章标题：返回R")
    if title.lower() == "r":
        time.sleep(1)
        return show_index()

    else:
        # 判断文章是否存在
        if title in all_articles:
            return look_article_detail(title)

        else:
            print("您要查看的文章不存在，请重新查看...")
            time.sleep(1)
            return look_articles()


# 查看自己的文章
def look_articles_self():
    # 查看自己的文章
    print("标题\t\t作者")
    for title_key in all_articles.keys():
        if all_articles.get(title_key).get("author") == online.get("username"):
            print(title_key, "\t", all_articles.get(title_key).get("author"))

    title = input("请输入您要查看的文章:(返回R)")
    if title.upper() == "R":
        return show_index()

    else:
        # 判断用户输入的标题是否存在，并展示文章
        if title in all_articles:
            return look_article_detail(title)

        else:
            print("没有该文章,请重新查看.")
            time.sleep(1)
            return look_articles_self()


# 查看文章详情
def look_article_detail(title):
    # 查看文章详情
    # 获取文章详情
    article = all_articles.get(title)
    # 更改阅读次数
    yue_shu = article.get("read_count")
    yue_shu += 1
    all_articles[title]["read_count"] = yue_shu
    # 展示文章
    print("文章标题：{}".format(article.get("title")))
    print("作者：{}".format(article.get("author")))
    print("阅读次数：{}".format(article.get("read_count")))
    print("文章内容如下：\n\t{}".format(article.get("content")))
    for i in all_articles[title]["comment"]:
        for a, b in i.items():
            print("评论详情：{}\t评论人{}".format(b, a))

    x = input("任意键返回或R评论")

    if x.upper() == "R":
        return comment_wen(title)

    else:
        return show_index()


# 评论文章
def comment_wen(title):
    # 判断这篇文章是否是自己的
    if all_articles[title]["author"] == online["username"]:
        input("这篇是您自己的文章，您不能评论自己的文章,任意键返回")
        time.sleep(1)
        return show_index()
    else:
        comment = input("请留下您的评论：（放弃评论R）")
        if comment == "R":
            return show_index()

        else:
            all_articles[title]["comment"].append({online.get("username"): comment})
            print("评论成功！")
            return look_article_detail(title)


# 发表文章
def article_publish():
    # 发表文章
    print("欢迎{}发表文章".format(online["username"]))
    print()

    # 输入文章标题
    title = input("请输入文章标题：")
    # 如果存在重新输入
    if title in all_articles:
        print("您输入的标题已经存在，重新输入...")
        time.sleep(1)
        return article_publish()
    # 提示输入文章
    content = input("请输入文章内容：")

    # 提示用户是否发表
    publish = input("是否发表,任意键继续：放弃r")
    if publish.upper() == "r":
        print("正在放弃请稍等...")
        time.sleep(2)
        print("放弃成功！")
        return show_index()

    # 创建文章
    article = {"title": title, "content": content, "author": online.get("username"), "read_count": 0, "comment": list()}
    # 将文章添加到文章字典里
    all_articles[title] = article
    print("正在发表中...")
    time.sleep(2)
    print("发表成功！")
    return show_index()


# 维护个人资料菜单
def wei_hu_zl():
    # 维护个人资料菜单
    print("欢迎来到PY901个人博客平台资料维护界面")
    print()
    print("\t1.修改密码")
    print("\t2.修改昵称")
    print("\t3.修改性别")
    print("\t4.修改年龄")
    print("\t5.联系电话")
    print("\t6.返回上一级")
    print("\t7.退出系统")
    # 用户选择
    choice = input("请选择服务：")
    # 判断用户输入
    return zi_menu_dict.get(choice)(choice) if choice in zi_menu_dict else wei_hu_zl()


# 修改密码
def change_password(choice):
    # 修改密码

    print("根据提示修改密码%s" % choice)
    password = input("请输入原密码：(退出r)")
    if password.lower() == "r":
        return wei_hu_zl()
    if password != online.get("password"):
        print("您输入的密码不正确请重新输入")
        time.sleep(1)
        return change_password(choice)

    else:
        # 输入新密码
        password1 = input("请输入新密码：")
        password2 = input("请确认密码：")
        # 判断两次密码输入是否一致
        if password1 == password2:
            users[online.get("admin")]["password"] = password1
            print("密码修改成功！")
            return login()

        else:
            print("您的密码输入不一致,请重新修改")
            time.sleep(1)
            return change_password(choice)


# 修改基本信息
def change(choice):
    """ 修改基本信息"""
    if choice == "6":
        return show_index()

    elif choice == "7":
        return exit_system()
    print("您的原{}为：{}".format(change_xx_dict[choice], online[change_dict[choice]]))
    user_name = input("请输入新{}：（退出R）".format(change_xx_dict[choice]))
    if user_name.upper() == "R":
        return wei_hu_zl()

    else:
        users[online.get("admin")][change_dict[choice]] = user_name
        print("修改成功！")
        time.sleep(1)
        return wei_hu_zl()


# 注册功能
def register():
    # 注册功能
    admin = input("请输入注册账号：(退出R)")
    if admin.upper() == "R":
        return show_login()
    # 判断账号是否存在
    elif admin in users:
        print("你注册的账号已经存在，请重新注册")
        return register()

    username = input("请输入注册昵称：")
    return email(admin, username)


# 邮箱注册
def email(admin, username):
    # 判断邮箱是否存在
    e_mail = input("请输入邮箱号：(必须使用qq邮箱)")
    e_mail = e_mail.strip()
    for value in users.values():
        if e_mail == value.get("email"):
            a = input("您输入的邮箱已经被注册，任意键重新输入（或R退出）")
            if a.upper() == "R":
                return show_login()

            else:
                return email(admin, username)

    # 判断邮箱格式是否正确
    if e_mail.endswith("@qq.com"):
        password = input("请输入密码：(退出R)")
        if admin.upper() == "R":
            return show_login()

        password1 = input("请确认密码：(退出R)")
        if admin.upper() == "R":
            return show_login()

        # 判断密码是否一致
        if password != password1:
            print("您输入的密码不一致，请重新注册...")
            time.sleep(1)
            return register()

        # 创建一个用户
        user = {"admin": admin, "password": password, "username": username,
                "email": e_mail, "sex": None, "age": None, "ph": None}
        users[admin] = user
        print("注册成功！")
        time.sleep(1)
        return show_login()

    else:
        print("您输入的邮箱有误，请重新输入...")
        return email(admin, username)


# 登录功能
def login():
    global online
    # 登录功能
    admin = input("请输入账号或邮箱号：")

    password = input("请输入密码：")
    # 判断账户登录
    if admin in users and password == users.get(admin).get("password"):
        # 登录成功
        print("登录成功！")

        online = users[admin]
        time.sleep(1)
        return show_index()

    # 判断邮箱登录
    for value in users.values():
        if admin == value.get("email") and password == value.get("password"):

            online = value
            print("登录成功！")
            time.sleep(1)
            return show_index()

    else:
        a = input("您输入的账号或邮箱号或密码不正确，任意键重新输入（退出r）")
        if a.upper() == "R":
            return show_login()

        else:
            time.sleep(1)
            return login()


# 退出系统
def exit_system():
    # 退出系统
    for i in range(0, 3):
        print("系统将在{}秒后退出".format(3-i))
        time.sleep(1)
    sys.exit(1)


# 定义登录界面的选项和函数的关系
login_menu_dict = {
    "1": login,
    "2": show_register,
    "3": exit_system
}
# 定义首页选项与函数的关系
index_menu_dict = {
    "1": look_articles,
    "2": look_articles_self,
    "3": article_publish,
    "4": wen_manage,
    "5": recycle_bin,
    "6": wei_hu_zl,
    "7": login,
    "8": show_login,
    "9": exit_system
}
# 定义资料维护与函数的关系
zi_menu_dict = {
    "1": change_password,
    "2": change,
    "3": change,
    "4": change,
    "5": change,
    "6": change,
    "7": change
}
# 定义修改函数与修改内容的关系
change_dict = {
    "2": "username",
    "3": "sex",
    "4": "age",
    "5": "ph"
}
# 定义修改各项资料和函数的关系
change_xx_dict = {
    "2": "昵称",
    "3": "性别",
    "4": "年龄",
    "5": "联系方式"
}

# 创建文章字典
all_articles = dict()
# 文章管理与函数关系
manage_wen = {
    "1": xiu_gai,
    "2": delete_wen,
    "3": delete_wen
}
# 回收站字典
recycle_bin_dict = dict()
# 回收站与操作函数的关系
recycle_manage_dict = {
    "1": clear_bin,
    "2": show_index,
    "3": delete_bin_wen,
    "4": retrieve_wen
}

# 系统用户字典
users = dict()
# 在线用户存储
online = None


def engine():
    # 启动程序
    show_login()


engine()
