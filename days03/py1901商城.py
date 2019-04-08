import random
import os,time
while True:
    # 首页展示
    print("欢迎来到PY1901商城")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("")
    print()
    print("    1.登录界面")
    print("    2.注册界面")
    print("    3.退出系统")
    print()
    print()
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

    # 用户输入选择
    choice=input("请选择编号：")
    # 清屏
    os.system("cls")

    # 判断用户输入选择
    if choice=="1":
        while True:
            # 用户输入
            user_name=input("请输入用户名：")
            passworld=input("请输入密码：")
            os.system("cls")

            # 判断用户输入
            if user_name=="admin" and passworld == "123":
                print("欢迎%s来到PY1901商城首页"%user_name)
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                print("")
                print()
                print("    1.休闲小游戏")
                print("    2.购物中心")
                print("    3.退出当前界面，返回到登录界面")
                print()
                print()
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

                # 用户选择输入
                choice_user=input("请选择编号：")
                os.system("cls")

                while True:
                # 判断用户输入选择
                    if choice_user=="1":
                        print("欢迎来到休闲小游戏")
                        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                        print("    1.石头剪刀布")
                        print("    2.老虎棒子鸡")
                        print("    3.退出当前页面，返回到商城首页")
                        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                        choice=input("请选择游戏编号")

                        os.system("cls")
                        if choice=="1":
                            print("欢迎来到休闲小游戏石头剪刀布")
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                            print()
                            print("    系统会自动出招，用户请根据提示出招")
                            print("    系统会自动评判输赢")
                            print("    获胜会有小惊喜哦（该功能正在维护中...）")
                            print()
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                            print()

                            while True:

                                print("系统正在出招")
                                #产生随机数
                                num=random.randint(0,2)
                                print("系统出招完成")

                                user_Attacks=input("请您出招：石头、剪刀、布；输入其他退出返回上一级菜单")  #Attacks：出招

                                if (user_Attacks =="布" and num == 0) \
                                    or (user_Attacks =="石头" and num == 1) \
                                    or (user_Attacks =="剪刀" and num == 2):
                                    print("你太厉害了，竟然赢了电脑")
                                    continue

                                elif (user_Attacks =="剪刀" and num == 0) \
                                    or (user_Attacks =="布" and num == 1) \
                                    or (user_Attacks =="石头" and num == 2):
                                    print("你输了，虽然输了，但不要灰心，再接再厉，下次一定会赢的！")
                                    continue

                                elif (user_Attacks =="石头" and num == 0) \
                                    or (user_Attacks =="剪刀" and num == 1) \
                                    or (user_Attacks =="布" and num == 2):
                                    print("你和老板是亲戚吧，怎么总是平局...")
                                    continue

                                else:
                                    print("正在退出当前游戏，1秒后返回休闲小游戏界面...")
                                    break

                            

                        elif choice=="2":
                            print("欢迎来到休闲小游戏老虎棒子鸡")
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                            print()
                            print("    系统会自动出招，用户请根据提示出招")
                            print("    系统会自动评判输赢")
                            print("    获胜会有小惊喜哦（该功能正在维护中...）")
                            print()
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")                            
                            print()

                            while True:
                                # 系统出招
                                print("系统正在出招")
                                num=random.randint(0,3)   #产生随机数
                                print("系统出招完成")

                                user_Attacks=input("请出招：老虎、棒子、鸡、虫；输入其他退出返回上一级菜单")

                                if (user_Attacks =="老虎" and num == 2) \
                                    or (user_Attacks =="棒子" and num == 0) \
                                    or (user_Attacks =="鸡" and num == 3) \
                                    or (user_Attacks =="虫" and num == 1):
                                    print("你太厉害了，竟然赢了电脑")
                                    continue

                                elif (user_Attacks =="老虎" and num == 1) \
                                    or (user_Attacks =="棒子" and num == 3) \
                                    or (user_Attacks =="鸡" and num == 0) \
                                    or (user_Attacks =="虫" and num == 2):
                                    print("你输了，虽然输了，但不要灰心，再接再厉，下次一定会赢的！")
                                    continue

                                elif (user_Attacks =="老虎" and num == 0) \
                                    or (user_Attacks =="棒子" and num == 1) \
                                    or (user_Attacks =="鸡" and num == 2) \
                                    or (user_Attacks =="虫" and num == 3):
                                    print("你和老板是亲戚吧，怎么总是平局...")
                                    continue

                                else:
                                    print("正在退出当前游戏，1秒后返回休闲小游戏界面...")
                                    break
                            
                        elif choice=="3":
                                print("正在退出当前页面，返回到商城首页")


                        print("游戏结束...")
                        break
                    
                    elif choice_user == "2":
                        print("欢迎来到购物中心,正在维护中")

                        # 用户输入
                        choice=input("输入n返回登录页面")

                        if choice=="n":
                            print("正在返回上一级登录界面,1秒后退出...")
                            time.sleep(1)
                            break

                    elif choice_user=="3":
                        print("正在返回上一级登录界面,1秒后退出...")
                        time.sleep(1)
                        break

            else:
                print("您输入的用户名或密码不正确,请重新输入！")
                

    elif choice=="2":
        print("欢迎注册新用户！")
        print("此功能正在更新暂时不可用....")
        continue
        

    elif choice=="3":
        print("退出系统成功！")
        break
    
    else:
        print("您输入有误请重新输入！")
