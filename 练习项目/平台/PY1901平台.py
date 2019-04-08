'''
    PY1901电商平台致力于河南奇酷学院py1901班学习开发，隶属于河南省奇酷集团py1901班所有，不用于任何商业运营，仿冒/盗用必究
                                 本平是一个集购物及娱乐的大型综合性商城
'''

# 引入函数:清屏cls\退出系统\随机函数\时间
import os,sys,random,time
# 账户储存
ji_f=10
user_list=list()
while True:
    os.system("cls")
    a=True
    z=True
    2
    b=True
    c=True
    # 展示界面
    print("欢迎来到PY1901电商平台")
    print()
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print()
    print()
    print("    1.登录界面")
    print("    2.注册界面")
    print("    3.退出系统")
    print()
    print()
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print()

    # 用户输入选择
    choice=input("请选择：")

    # 判断用户选择
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

            for admin in user_list:
                
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
            if is_ok==False or a==False or z==False:
                break
            

            # 展示电商平台首页
            print()
            os.system("cls")
            print("欢迎%s来到PY1901商城"%user_name)
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()
            print()
            print("    1.休闲小游戏")
            print("    2.购物中心")
            print("    3.查看积分")
            print("    4.修改密码")
            print("    5.返回到商城首页")
            print("    6.充值积分")
            print()
            print("   新号系统会赠送10积分，购物也可赠送积分")
            print()
            x=user_list.index(admin)
            print("您剩余积分:%s"%user_list[x][2])
            print()
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()

            choice =input("请选择服务：")

            # 判断用户选择
            if choice=="5":
                print("即将退出...")
                time.sleep(1)
                break
            
            elif choice=="6":

                while True:
                    os.system("cls")
                
                    # 充值积分界面
                    print()
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    print()
                    print("          欢迎来到PY1901积分充值中心")
                    print()
                    print("     1元钱10积分")
                    print("")
                    print("   1.充值")
                    print("   2.退出")
                    x=user_list.index(admin)
                    print("您剩余积分:%s"%user_list[x][2])
                    print()
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    print()

                    choice=input("请选择服务：")

                    if choice=="1":
                        chong_z=int(input("请充值："))

                        x=user_list.index(admin)
                        user_list[x][2]+=chong_z*10
                        print("充值成功！")
                        time.sleep(1)
                        continue

                    elif choice=="2":
                        print("正在退出...")
                        time.sleep(1)
                        break
                    
                    else:
                        print("您的输入有误请重新输入")
                        time.sleep(1)
                        continue

            # 查看积分
            elif choice=="3":
                print("正在计算机的积分，请稍等...")
                time.sleep(1)
                x=user_list.index(admin)
                input("你的积分剩余：%s分;按任意键退出查看。"%user_list[x][2])
                time.sleep(1)
                continue
            
            elif choice=="1":
                
                while True:

                    t=True
                    l=True
                    
                    os.system("cls")
                    # 展示小游戏界面
                    print()
                    print("      欢迎%s来到PY1901休闲小游戏"%user_name)
                    print()
                    print("玩游戏赢积分，赢到店家破产")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    print()
                    print("        1.石头剪刀布")
                    print("        2.老虎棒子鸡")
                    print("        3.猜数字")
                    print("        4.退出界面，返回商城")
                    print("        5.退出登录")
                    print()
                    print()
                    x=user_list.index(admin)
                    print("您剩余积分:%s"%user_list[x][2])
                    print()
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    print()

                    # 用户输入选择
                    choice = input("请选择：")

                    # 判断用户输入
                    if choice=="1":
                        
                        while True:

                            if t==False:
                                break
                            os.system("cls")
                            # 展示石头剪刀布界面
                            print("##########################################")
                            print()
                            print("     欢迎%s来到石头剪刀布休闲小游戏"%user_name)
                            print()
                            print("       根据提示出招，祝您玩的愉快")
                            print()
                            print("积分规则：赢了奖励2分，输了扣2分")
                            print()
                            x=user_list.index(admin)
                            print("您剩余积分:%s"%user_list[x][2])
                            print()
                            print("##########################################")
                            print()
                            

                            # 系统出招
                            print("系统正在出招...")
                            time.sleep(3)
                            num=random.randint(0,2)
                            print("系统出招完毕，请您出招")

                            while True:
                                # 提示用户出招
                                user_choice=input("请出招：石头、剪刀、布;退出n")


                                # 判断输赢
                                if (user_choice=="石头" and num==1) \
                                    or (user_choice=="剪刀" and num==2) \
                                    or (user_choice=="布" and num==0):

                                    # 提示用户是否继续
                                    choice=input("恭喜您，您赢了！  是否退出：退出y,任意键继续！")
                                    user_list[x][2]+=2
                                    if choice=="y":
                                        print("正在退出，请稍等...")
                                        time.sleep(2)
                                        t=False
                                        break

                                    else:
                                        break

                                elif (user_choice=="石头" and num==2) \
                                    or (user_choice=="剪刀" and num==0) \
                                    or (user_choice=="布" and num==1):

                                    # 提示用户是否继续
                                    choice=input("你是不是和老板有亲戚，总是平局。  是否退出：退出y,任意键继续！")
                                    if choice=="y":
                                        print("正在退出，请稍等...")
                                        time.sleep(2)
                                        t=False
                                        break

                                    else:
                                        break

                                elif (user_choice=="石头" and num==0) \
                                    or (user_choice=="剪刀" and num==1) \
                                    or (user_choice=="布" and num==2):

                                    # 提示用户是否继续
                                    choice=input("很遗憾你输了  是否退出：退出y,任意键继续！")
                                    user_list[x][2]-=2
                                    if choice=="y":
                                        print("正在退出，请稍等...")
                                        time.sleep(2)
                                        t=False
                                        break

                                    else:
                                        break

                                elif user_choice=="n":
                                    print("正在退出，请稍等...")
                                    time.sleep(2)
                                    t=False
                                    break

                                else:
                                    print("您的输入有误，请稍后输入")
                                    time.sleep(2)
                                    continue

                    elif choice=="2":
                        pass
                        while True:
                            if l==False:
                                break

                            os.system("cls")
                            # 展示老虎棒子鸡小游戏
                            print("欢迎来到休闲小游戏老虎棒子鸡")
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                            print()
                            print("    系统会自动出招，用户请根据提示出招")
                            print("    系统会自动评判输赢")
                            print("    获胜会有小惊喜哦（该功能正在维护中...）")
                            print()
                            print("积分规则：赢了奖励2分，输了扣2分")
                            print()
                            x=user_list.index(admin)
                            print("您剩余积分:%s"%user_list[x][2])
                            print()
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")                            
                            print()

                            # 系统出招
                            print("系统正在出招...")
                            time.sleep(3)
                            num=random.randint(0,3)   #产生随机数
                            print("系统出招完成")

                            while True:

                                # 用户出招
                                choice=input("请出招：老虎棒子鸡虫；退出n")

                                # 判断用户输入
                                if (choice == "老虎" and num == 2) \
                                    or (choice == "棒子" and num == 0) \
                                    or (choice == "鸡" and num == 3) \
                                    or (choice == "虫" and num == 1):
                                    choice = input("您太厉害了，竟然赢了电脑，任意键继续，结束n")
                                    user_list[x][2] += 2

                                    # 判断
                                    if choice=="n":
                                        print("正在退出,一秒后退出")
                                        time.sleep(1)
                                        l=False
                                        break

                                    else:
                                        print("请稍等，一秒后重新开始...")
                                        break


                                elif (choice=="老虎" and num==1) \
                                    or (choice == "棒子" and num==3) \
                                    or (choice=="鸡" and num==0) \
                                    or (choice=="虫" and num==2):
                                    choice=input("您输了，再接再厉，下次一定能赢，任意键继续，结束n")
                                    user_list[x][2]-=2

                                    # 判断
                                    if choice=="n":
                                        print("正在退出,一秒后退出")
                                        time.sleep(1)
                                        l = False
                                        break

                                    else:
                                        print("请稍等，一秒后重新开始...")
                                        break

                                elif (choice=="老虎" and num==0) \
                                    or (choice=="棒子" and num==1) \
                                    or (choice == "鸡" and num==2) \
                                    or (choice=="虫" and num==3):
                                    choice=input("平局，你和老板有亲戚吧，总是平局，任意键继续，结束n")

                                    # 判断
                                    if choice=="n":
                                        print("正在退出,一秒后退出")
                                        time.sleep(1)
                                        l = False
                                        break

                                    else:
                                        print("请稍等，一秒后重新开始...")
                                        time.sleep(1)
                                        break

                                elif choice=="n":
                                    print("正在退出,一秒后退出")
                                    time.sleep(1)
                                    l = False
                                    break

                                else:
                                    print("您的输入有误，请重新输入...")
                                    time.sleep(2)
                                    continue
                    
                    elif choice=="3":

                        while True:
                            os.system("cls")
                            ci_shu=0
                            # 展示猜字游戏界面
                            print()
                            print("欢迎来到猜数字游戏！")
                            print()
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                            print()
                            print("  游戏规则：系统会随机产生一个数字(1~100)")
                            print("            用户根据提示进行猜测")
                            print("            猜对会有积分奖励哦！")
                            print()
                            print("积分规则：猜对奖励4分，猜错扣1分")
                            print()
                            x=user_list.index(admin)
                            print("您剩余积分:%s"%user_list[x][2])
                            print()
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                            print()

                            # 提示系统正在随机产生一个数字
                            print("系统正在产生数字，请稍等...")
                            time.sleep(3)
                            # 产生随机数
                            no = random.randint(1,100)
                            # 提示随机数已产生
                            print("系统随机数已经产生，请输入您的猜测")

                            while True:
                                # 记录次数变化
                                ci_shu+=1
                                # 用户输入
                                cai_num = input("请输入您的数字：(1~100)")
                                # 转整
                                cai_num = int(cai_num)

                                # 判断输入的数字大小
                                if cai_num > no:
                                    input("你输入的数字过大，按任意键继续...")
                                    user_list[x][2]-=1
                                
                                elif cai_num < no:
                                    input("你输入的数字过小，按任意键继续....")
                                    user_list[x][2]-=1

                                else:
                                    print("恭喜您猜对了，共猜了",ci_shu,"次")
                                    user_list[x][2]+=4
                                    break
                            
                            # 提示用户是否继续玩
                            is_player=input("是否继续：继续y,结束按任意键退出游戏")

                            # 判断用户输入
                            if is_player == "y":
                                continue
                            
                            else:
                                print("游戏结束！")
                                break


                    elif choice=="4":
                        print("正在返回上一个界面，请稍等...")
                        time.sleep(2)
                        break

                    elif choice=="5":
                        print("正在退出登录...")
                        time.sleep(3)
                        a=False
                        break

                    else:
                        print("您的输入有误，3秒后请重新选择...")
                        time.sleep(2)
                        continue


            # 购物超市
            elif choice=="2":
                # 商品定义
                h_jy=["1","黄金叶",10,20]
                h_hl=["2","黄鹤楼",18,15]
                smoke=[h_jy,h_hl]
                while True:
                    if b==False:
                        break

                    os.system("cls")

                    # 展示商品
                    print("")
                    print("                                        欢迎来到PY1901无人售货超市")
                    print()
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    print()
                    print("\t\t商品编号\t\t商品名称\t\t商品价格\t\t商品库存")
                    print()
                    print("\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s"%(h_jy[0],h_jy[1],h_jy[2],h_jy[3]))
                    print("\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s"%(h_hl[0],h_hl[1],h_hl[2],h_hl[3]))
                    print()
                    print("\t\t3.退出")
                    print()
                    print("在本商城消费赠送积分，积分可以去休闲游戏里玩游戏，每消费1元赠送1积分可积累")
                    print()
                    x=user_list.index(admin)
                    print("您剩余积分:%s"%user_list[x][2])
                    print()

                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

                    # 选择商品
                    choice=input("请选择服务：")

                    for i in smoke:
                        # if c==False:
                        #     break
                        if choice==i[0]:
                            # 确认选择
                            choice=input("您选择的是%s,任意键确定，重新选择n"%i[1])
                            if choice=="n":
                                break
                            
                            while True:
                                    
                                shu_l=int(input("请输入购买数量："))

                                if shu_l<i[3]:
                                    is_ok=input("您购买的数量为%s,任意键确定，重新选择n"%shu_l)
                                    if is_ok=="n":
                                        continue
                                    
                                    else:
                                        break

                                elif shu_l==i[3]:
                                    is_ok=input("您购买的数量为%s,任意键确定，重新选择n"%shu_l)
                                    if is_ok=="n":
                                        continue
                                    else:
                                        break

                                else:
                                    input("库存不足，请重新选择数量,任意键继续")
                                    continue
                            money=shu_l*i[2]
                            print("您购买了%s个%s,共%s元"%(shu_l,i[1],money))
                            is_ok=input("是否放弃购买，放弃n，任意键付款")
                            if is_ok=="n":
                                print("正在放弃...")
                                time.sleep(1)
                                break

                            # # 提示是否继续购买
                            # is_ok=input("是否继续购买其他商品？任意键结束，继续y")
                            
                            # # 判断
                            # if is_ok=="y":
                            #     print("请稍后继续...")
                            #     time.sleep(1)
                            #     break

                            # else:
                            while True:

                                # 提示付款
                                fu_k=float(input("请付款"))
                                if fu_k>=money:
                                    print("正在找零，请稍等...")
                                    time.sleep(1)
                                    zhao_l=fu_k-money
                                    x=user_list.index(admin)
                                    user_list[x][2]+=money
                                    print("您付款%s元，一共消费了%s元，找零%s元"%(fu_k,money,zhao_l))
                                    print("本次购物共增加了%s分，您总共剩余%s分"%(money,user_list[x][2]))
                                    
                                    is_ok=input("是否继续购买：继续y，任意键结束")
                                    if is_ok=="y":
                                        print("请稍等...")
                                        c=False
                                        break
                                    else:
                                        print("正在退出...")
                                        b=False
                                        time.sleep(2)
                                        break

                                else:
                                    print("您的付款不足，请重新付款.")
                                    time.sleep(1)

                                    continue

                        elif choice=="3":
                            b=False
                            time.sleep(1)
                            break

                        else:
                            print("你要的服务暂时没有，稍后请重新选择...")
                            time.sleep(2)
                            break

                print("欢迎下次光临，祝您生活愉快，请慢走...")

            # 修改密码
            elif choice=="4":
                while True:

                    os.system("cls")
                    print()
                    print("\t\t欢迎%s来到修改密码界面"%(admin[0]))
                    print()

                    # 输入原密码
                    a=input("请输入原密码，退出n")
                    
                    # 判断密码是否正确
                    if a==admin[1]:
                        xin_password=input("请输入新密码：")
                        x=user_list.index(admin)
                        user_list[x][1]=xin_password
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
                
            # 退出当前页面
            elif choice=="4":
                print("正在退出，请稍等...")
                time.sleep(2)
                break

            # 输入不正确提示
            else:
                print("您的输入有误，请重新输入...")
                time.sleep(2)
                continue

    elif choice=="2":
        
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
            user_name=input("请输入需要注册的用户名：（退出n）")
            if user_name=="n":
                print("正在退出...")
                time.sleep(2)
                break

            is_ok=True
            for admin in user_list:
                if user_name==admin[0]:
                    print("您输入的账户已存在，请使用其他账户注册")
                    is_ok=False
            
            if is_ok==False:
                continue

            password=input("请输入密码：")

            # 注册用户：将用户输入的账户、密码、保存成一个列表
            admin=[user_name,password,ji_f]
            # 注册用户：将用户列表，添加到系统用户变量中
            user_list.append(admin)

            print("注册成功,1秒后退出...")
            time.sleep(1)
            break

    elif choice == "3":
        print("系统将在1秒后退出...")
        time.sleep(1)
        break

    else:
        print("您的输入有误，请重新输入...")
        time.sleep(2)


print("退出系统成功！欢迎下次光临")
    


