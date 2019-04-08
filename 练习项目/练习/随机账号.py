import random,time

users=dict()
while True:


    # 展示开始界面
    print()
    print("欢迎来到PY1901电商平台")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print()
    print("    1.登录界面")
    print("    2.注册界面")
    print("    3.退出系统")
    print()
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print()
    print(users)

    # 用户输入选择
    choice = input("请选择您要的服务：")

    if choice == "2":
        ni_cheng = input("请输入昵称：(退出n)")
        if ni_cheng=="n":
            continue

        while True:

            # 设置密码
            password = input("请输入密码:")
            # 确认密码
            password1 = input("请确认密码：")

            # 判断密码是否正确
            if password1 == password:

                while True:
                    account_number=list()
                    # 产生随机账号
                    for i in range(6):
                        account_number.append(str(random.randint(0,9)))

                    account_number = "".join(account_number)
                    if account_number in users:
                        continue

                    else:
                        print("正在生成账号...")
                        time.sleep(1)
                        break

                print(account_number)
                user={"admin":account_number,"password":password,"username":ni_cheng,"yu_e":0,"ji_f":10}
                users={account_number:user}
                input("注册成功！您注册的账号为%s,请牢记账号和密码.任意键结束"%account_number)
                time.sleep(1)
                break

            else:
                is_ok = input("您输入的密码不一致，任意键重新设置!退出n")
                if is_ok == "n":
                    print("正在退出注册...")
                    break

                else:
                    time.sleep(1)
                    continue

    elif choice=="1":

        while True:
            # 展示登录界面
            print("欢迎登录博客")

            account_number=input("请输入账号：（退出n）")
            if account_number=="n":
                print("正在退出，请稍等...")
                time.sleep(1)
                break
            password = input("请输入密码：（退出n）")
            if password == "n":
                print("正在退出，请稍等...")
                time.sleep(1)
                break

            # 判断用户输入是否正确
            if account_number in users and password==users[account_number]["password"]:
                print("登录成功！")
                break

            else:
                print("你的账户或者密码不正确，请重新登录...")
                time.sleep(1)
                continue

        while True:

            # 展示首页
            print()
            print("欢迎%s来到商城"%users[account_number]["username"])
            print()
            print("\t\t1.小游戏")

            choice=input("请选择服务:")





    elif choice=="3":
        print("正在退出...")
        time.sleep(1)
        break

    else:
        print("您的输入有误，请重新输入.")
        time.sleep(1)
        continue


