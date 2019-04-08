users=list()
import os,time

while True:
    z=True
    os.system("cls")
    print("修改密码")
    print()
    print()

    print("1.登录")
    print("2.注册")

    print()
    choice=input("请选择")

    if choice=="1":
        while True:
            os.system("cls")
            is_ok=True
            # 展示登录界面
            print()
            print("##########################################")
            print()
            print("        欢迎登陆PY901综合性电商平台")
            print()
            print("##########################################")
            print()

            # 用户登录
            user_name=input("请输入账号：n")
            if user_name=="n":
                is_ok=False
                break       
            password=input("请输入密码：")

            for admin in users:
                
                # 判断输入是否正确
                if user_name==admin[0] and password==admin[1]:
                    print("登录成功！1秒后进入首页...")
                    time.sleep(1)
                    break
            else:
                print("你的账号或者密码不正确，请重新登录...")
                time.sleep(1)
                continue

            break

        while True:
            if z==False:
                break

            os.system("cls")
            # 展示电商平台首页
            print()
            print("欢迎%s来到PY1901商城"%user_name)
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()
            print()
            print("    1.休闲小游戏")
            print("    2.购物中心")
            print("    3.修改密码")
            print("    4.退出登录")
            print()
            print()
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()

            choice =input("请选择服务：")

            # 判断用户选择
            # 
            if choice=="3":

                while True:

                    os.system("cls")
                    a=input("请输入原密码，退出n")

                    if a==admin[1]:

                        xin_password=input("请输入新密码：")

                        x=users.index(admin)
                        users[x][1]=xin_password
                        input("修改成功！任意键返回,重新登录")
                        time.sleep(1)
                        z=False
                        break
                
                    
                    elif a=="n":
                        break

                    else:
                        print("您的输入的密码不正确请重新输入")
                        time.sleep(3)
                        continue

                if z==False:
                    continue
            
            # 退出登录
            elif choice=="4":
                print("正在退出，请稍等...")
                time.sleep(2)
                break

            # 休闲小游戏
            elif choice=="1":
                
                while True:

                    os.system("cls")




            # 购物超市
            elif choice=="2":
                pass

            # 提醒输入有误,没有这个选项
            else:
                print("您的的输入有误，稍后请重新输入...")
                time.sleep(2)
                continue
            
        


    else:
        while True:
            os.system("cls")
            # 展示注册界面
            print("欢迎注册PY1901电商平台账号")
            print()
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()
            print("根据提示填写注册信息!")
            print()
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()

        
            
            # 提示用户进行输入
            user_name=input("请输入需要注册的用户名：")
            is_ok=True
            for admin in users:
                if user_name==admin[0]:
                    print("您输入的账户已存在，请使用其他账户注册")
                    is_ok=False
            
            if is_ok==False:
                continue

            password=input("请输入密码：")

            # 注册用户：将用户输入的账户、密码、保存成一个列表
            admin=[user_name,password]
            # 注册用户：将用户列表，添加到系统用户变量中
            users.append(admin)

            print("注册成功,1秒后退出...")
            time.sleep(1)
            break


