'''
个人博客开发
    登录菜单
    注册菜单
    首页菜单
    查看所有文章
    查看个人文章
    查看文章详情

    注册
    登录
    发表文章

    用户users = dict()
        u1 = {'username': 'admin', 'password': '123', 'nickname': '小刘'}
    文章articles = dict('标题': a1)
        a1 = {'title': '标题', author: u1, content='内容', readed_count: 0}
'''
# 引入依赖的模块
import os, sys, time, shelve


# 定义函数
def show_login():
    '''展示登录菜单'''
    print("\t\t个人博客项目用户登录")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 用户登录")
    print("\t\t2. 用户注册")
    print("\t\t3. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")

    # 用户输入选项
    choice = input("请输入选项：")
    # 跳转执行对应的函数
    # if choice in login_menu_dict:
    #     # 获取选项对应的函数
    #     func = login_menu_dict.get(choice)
    #     # 执行函数
    #     return func()
    # else:
    #     # 没有这个选项，重新展示登录菜单
    #     return show_login()
    return login_menu_dict.get(choice)() if choice in login_menu_dict else show_login()


def show_register():
    '''展示注册菜单'''
    print("\t\t系统用户注册")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t 欢迎来到PY1901个人博客系统")
    print("\t 请按照提示信息，录入个人资料，完成注册")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    time.sleep(1)

    # 用户开始注册
    return register()


def show_index():
    '''展示首页菜单'''
    print("\t\t个人博客首页")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 查看所有文章")
    print("\t\t2. 查看个人文章")
    print("\t\t3. 发表文章")
    print("\t\t4. 个人信息维护")
    print("\t\t5. 返回上一级")
    print("\t\t6. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")

    # 用户输入选项
    choice = input("请输入选项：")

    return index_menu_dict.get(choice)() if choice in index_menu_dict else show_index()


def look_articles():
    '''查看所有文章'''
    # 循环查看所有文章的标题即可
    print("标题\t\t作者")
    for title_key in articles.keys():
        print(title_key, "\t\t", articles.get(title_key).get('author').get('username'))

    title = input("请输入要查看的文章标题(R键返回首页)：")
    if title.upper() == "R":
        return show_index()
    else:
        # 判断用户输入的标题是否存在，并展示文章
        if title in articles:
            look_article_detail(title)
        else:
            print("没有这篇文章")
            time.sleep(1)
            return look_articles()


def look_articles_self():
    '''查看自己的所有文章'''
    print("标题\t\t作者")
    for title_key in articles.keys():
        if articles.get(title_key).get('author').get('username') == online.get('username'):
            print(title_key, "\t\t", articles.get(title_key).get('author').get('username'))

    title = input("请输入要查看的文章标题(R键返回首页)：")
    if title.upper() == "R":
        return show_index()
    else:
        # 判断用户输入的标题是否存在，并展示文章
        if title in articles:
            look_article_detail(title)
        else:
            print("没有这篇文章")
            time.sleep(1)
            return look_articles()


def look_article_detail(title):
    '''查看文章详情'''
    # 获取文章
    article = articles.get(title)
    # 更改阅读次数
    rc = article.get('readed_count')
    rc += 1
    article['readed_count'] = rc
    # 展示文章
    print("文章标题：{}".format(article.get('title')))
    print("文章作者：{}".format(article.get('author').get('username')))
    print("阅读次数：{}".format(article.get('readed_count')))
    print("文章内容：{}".format(article.get('content')))

    input("按任意键返回首页")
    return show_index()


def login():
    '''登录函数'''
    username = input("请输入账号：")
    password = input("请输入密码：")
    # 验证账号密码是否正确
    if username in users and password == users.get(username).get('password'):
        # 登录成功，记录登录用户并跳转到首页
        global online
        online = users.get(username)
        return show_index()
    else:
        print("账号或者密码有误，请重新输入")
        time.sleep(1)
        return login()


def register():
    '''注册函数'''
    # 用户输入注册信息
    username = input("请输入注册账号:")
    if username in users:
        print("账号已经存在，请使用其他账号注册")
        time.sleep(1)
        return register()

    password = input("请输入密码：")
    confirm = input("请确认密码：")
    if password != confirm:
        print("两次密码输入不一致，请重新注册")
        time.sleep(1)
        return register()

    # 创建用户信息，注册
    user = {'username': username, 'password': password, 'nickname': '待完善'}
    # 注册，录入到系统全局变量中
    users[username] = user
    # 展示登录菜单
    save_data()
    return show_login()


def article_publish():
    '''发表文章函数'''
    # 用户输入发表文章的标题、内容
    title = input("请输入文章标题：")
    if title in articles:
        print("标题已经存在，请使用其他标题")
        time.sleep(1)
        return article_publish()

    # 用户输入内容
    content = input("请输入文章内容：")

    # 创建文章
    article = {'title': title, 'content': content, 'author': online, 'readed_count': 0}
    # 将文章添加到系统中
    articles[title] = article

    print("文章发表中.....")
    time.sleep(1)
    print("文章发表成功.")
    # 跳转到首页
    return show_index()


def userinfo_perfect():
    '''个人信息维护'''
    pass


def exit_system():
    '''退出系统'''
    # 存储数据
    save_data()
    for i in range(0, 3):
        print("系统将在{}秒后退出....".format(3 - i))
        time.sleep(1)
    sys.exit(1)


def save_data():
    '''将数据存储到文件中'''
    file = shelve.open('data/blog.dat')
    file['users'] = users
    file['articles'] = articles


def get_data():
    '''从文件中读取数据'''
    global users, articles
    file = shelve.open('data/blog.dat')
    users = file['users']
    articles = file['articles']


# 用户数据
users = dict()
# 文章数据
articles = dict()
# 创建一个变量，记录在线登录的用户
online = None

# 定义选项和函数的对应关系
login_menu_dict = {
    '1': login,
    '2': show_register,
    '3': exit_system
}
# 定义首页选项和函数的对应关系
index_menu_dict = {
    '1': look_articles,
    '2': look_articles_self,
    '3': article_publish,
    '4': userinfo_perfect,
    '5': show_login,
    '6': exit_system
}


def engine():
    # 初始化数据
    get_data()
    # 初始化引擎：展示登录菜单
    show_login()


engine()
