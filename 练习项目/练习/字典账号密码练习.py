'''
    PY1901电商平台致力于河南奇酷学院py1901班学习开发，隶属于河南省奇酷集团py1901班所有，不用于任何商业运营，仿冒/盗用必究
                                 本平是一个集购物及娱乐的大型综合性商城
'''

import  random,sys,time

# 定义用户列表：账户/用户昵称/密码/余额/积分

users={}
while True:
    z=True
    is_ok=True
    a=True
    d=True

    # 展示开始界面
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
    choice=input("请选择您要的服务：")

    # 判断选择
    if choice=="1":

        # 展示登录界面
        while True:
            if d==False:
                break
            print()
            print("\t\t欢迎来到PY1901商城登录界面")
            print()


            # 提示用户输入账号信息
            user=input("请输入账号：(退出n)")
            if user=="n":
                print("正在退出，请稍等...")
                time.sleep(1)
                a=False
                break
            # 提示用户输入密码
            password=input("请输入密码:(退出n)")
            if password=="n":
                print("正在退出，请稍等...")
                time.sleep(1)
                a=False
                break

            for i,j in users.items():
                if user==i and password == j[1]:
                    print("登录成功！正在跳转请稍等...")
                    time.sleep(1)
                    d=False
                    break

                else:
                    print("您的账号或密码错误，请重新登录")
                    time.sleep(1)
                    break

        while True:
            if a==False:
                break

            # 展示首页
            print("欢迎%s来到PY1901商城")
            print()
            print("\t1.休闲小游戏")
            print("\t2.购物超市")
            print("\t3.修改密码")
            print("\t4.退出登录")
            print()

            # 提示用户选择服务
            choice=input("请选择服务:")

            if choice=="1":
                pass

            elif choice=="2":
                pass

            elif choice=="3":

                while True:
                    # 展示修改界面
                    print("欢迎%s来到修改密码界面")
                    print("根据提示完成操作")

                    que_password=input("请输入原密码：(退出n)")
                    if que_password=="n":
                        print("正在退出修改密码界面，请稍等...")
                        time.sleep(1)
                        break

                    elif que_password== password == j[1]:
                        xin_password=input("请输入新密码：")
                        if xin_password==password:
                            print("与原密码相同，请重新输入")
                            time.sleep(1)
                            continue

                        else:
                            j[1]=xin_password
                            print("修改成功，请重新登录！")
                            time.sleep(1)
                            a=False
                            break

                    else:
                        print("密码错误请重新输入！")
                        time.sleep(1)
                        continue

            elif choice=="4":
                print("正在退出登录，请稍等...")
                time.sleep(2)
                break

            else:
                print("您选择的服务暂时未开通，请重新选择")
                time.sleep(1)
                continue

    elif choice=="2":


        # 展示注册界面
        print("\t\t欢迎来到PY1901商城用户注册界面")
        print("根据下面提示进行操作")

        while True:
            if is_ok==False:
                break
            # 输入账号
            user=input("请输入您要注册的账号,退出n")
            if user=="n":
                print("正在退出注册界面...")
                time.sleep(1)
                z=False
                break

            for admin in users.keys():

                # 判断用户是否存在
                if admin==user:
                    is_cz=input("您注册的账号已经存在，任意键重新注册，退出n")
                    if is_cz=="n":
                        print("正在退出注册，请稍等...")
                        time.sleep(2)
                        is_ok=False
                        break

                    else:
                        print("请重新注册...")
                        time.sleep(1)
                        break

            else:
                break

        while True:
            if z==False or is_ok==False:
                break

            # 设置密码
            password=input("请输入密码:")
            # 确认密码
            password1=input("请确认密码：")

            # 判断密码是否正确
            if password1==password:
                name=input("请输入昵称：")

                users[user]=[name,password,0,10]
                input("注册成功！您注册的账号为%s,请牢记账号和密码.任意键结束"%user)
                time.sleep(1)
                break

            else:
                is_ok=input("您输入的密码不一致，任意键重新设置!退出n")
                if is_ok=="n":
                    print("正在退出注册...")
                    is_ok = False
                    break

                else:
                    time.sleep(1)
                    continue

    elif choice=="3":
        print("系统正在退出，请稍等...")
        time.sleep(3)
        break

print("系统退出成功，欢迎下次光临！请慢走...")