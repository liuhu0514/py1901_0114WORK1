'''
    PY1901电商平台致力于河南奇酷学院py1901班学习开发，隶属于河南省奇酷集团py1901班所有，不用于任何商业运营，仿冒/盗用必究
                            本平是一个集购物及娱乐的大型综合性商城
'''

# 引入函数:清屏cls\退出系统\随机函数\时间
import sys,random,time
# 账户储存
user_list=list()
while True:
    a=True
    z=True
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

            print("欢迎%s来到PY1901商城"%user_name)
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()
            print()
            print("    1.休闲小游戏")
            print("    2.购物中心")
            print("    3.修改密码")
            print("    4.返回到商城首页")
            print()
            print()
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print()

            choice =input("请选择服务：")

            # 判断用户选择
            if choice=="4":
                print("系统即将退出...")
                time.sleep(1)
                break
            
            elif choice=="1":
                
                while True:
                    

                    # 展示小游戏界面
                    print()
                    print("      欢迎%s来到PY1901休闲小游戏"%user_name)
                    print()
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    print()
                    print("        1.石头剪刀布")
                    print("        2.老虎棒子鸡")
                    print("        3.猜数字")
                    print("        4.退出界面，返回商城")
                    print("        5.退出登录")
                    print()
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    print()

                    # 用户输入选择
                    choice = input("请选择：")

                    # 判断用户输入
                    if choice=="1":
                        
                        while True:

                            # 展示石头剪刀布界面
                            print("##########################################")
                            print()
                            print("     欢迎来到石头剪刀布休闲小游戏")
                            print()
                            print("       根据提示出招，祝您玩的愉快")
                            print()
                            print("##########################################")
                            print()

                            # 系统出招
                            print("系统正在出招...")
                            time.sleep(3)
                            num=random.randint(0,2)
                            print("系统出招完毕，请您出招")

                            # 提示用户出招
                            user_choice=input("请出招：石头、剪刀、布;退出n")

                            # 判断输赢
                            if (user_choice=="石头" and num==1) \
                                or (user_choice=="剪刀" and num==2) \
                                or (user_choice=="布" and num==0):

                                # 提示用户是否继续
                                choice=input("恭喜您，您赢了！  是否退出：退出y,任意键继续！")
                                if choice=="y":
                                    print("正在退出，请稍等...")
                                    time.sleep(2)
                                    break

                                else:
                                    continue

                            elif (user_choice=="石头" and num==2) \
                                or (user_choice=="剪刀" and num==0) \
                                or (user_choice=="布" and num==1):

                                # 提示用户是否继续
                                choice=input("你是不是和老板有亲戚，总是平局。  是否退出：退出y,任意键继续！")
                                if choice=="y":
                                    print("正在退出，请稍等...")
                                    time.sleep(2)
                                    break

                                else:
                                    continue

                            elif (user_choice=="石头" and num==0) \
                                or (user_choice=="剪刀" and num==1) \
                                or (user_choice=="布" and num==2):

                                # 提示用户是否继续
                                choice=input("很遗憾你输了  是否退出：退出y,任意键继续！")
                                if choice=="y":
                                    print("正在退出，请稍等...")
                                    time.sleep(2)
                                    break

                                else:
                                    continue

                            elif user_choice=="n":
                                print("正在退出，请稍等...")
                                time.sleep(2)
                                break
                            
                            else:
                                print("您的输入有误，请稍后输入")
                                time.sleep(2)
                                continue

                    elif choice=="2":
                        pass
                        while True:

                            # 展示老虎棒子鸡小游戏
                            print("欢迎来到休闲小游戏老虎棒子鸡")
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                            print()
                            print("    系统会自动出招，用户请根据提示出招")
                            print("    系统会自动评判输赢")
                            print("    获胜会有小惊喜哦（该功能正在维护中...）")
                            print()
                            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")                            
                            print()

                            # 系统出招
                            print("系统正在出招...")
                            time.sleep(3)
                            num=random.randint(0,3)   #产生随机数
                            print("系统出招完成")

                            # 用户出招
                            choice=input("请出招：老虎棒子鸡虫；退出n")

                            if (choice=="老虎" and num==2) \
                                or (choice=="棒子" and num==0) \
                                or (choice=="鸡" and num==3) \
                                or (choice=="虫" and num==1):
                                choice=input("您太厉害了，竟然赢了电脑，任意键继续，结束n")

                                # 判断
                                if choice=="n":
                                    print("正在退出,一秒后退出")
                                    time.sleep(1)
                                    break

                                else:
                                    print("请稍等，一秒后重新开始...")
                                    continue

                            elif (choice=="老虎" and num==1) \
                                or (choice=="棒子" and num==3) \
                                or (choice=="鸡" and num==0) \
                                or (choice=="虫" and num==2):
                                choice=input("您输了，再接再厉，下次一定能赢，任意键继续，结束n")

                                # 判断
                                if choice=="n":
                                    print("正在退出,一秒后退出")
                                    time.sleep(1)
                                    break

                                else:
                                    print("请稍等，一秒后重新开始...")
                                    continue

                            elif (choice=="老虎" and num==0) \
                                or (choice=="棒子" and num==1) \
                                or (choice=="鸡" and num==2) \
                                or (choice=="虫" and num==3):
                                choice=input("平局，你和老板有亲戚吧，总是平局，任意键继续，结束n")

                                # 判断
                                if choice=="n":
                                    print("正在退出,一秒后退出")
                                    time.sleep(1)
                                    break

                                else:
                                    print("请稍等，一秒后重新开始...")
                                    time.sleep(1)
                                    continue

                            elif choice=="n":
                                print("正在退出,一秒后退出")
                                time.sleep(1)
                                break

                            else:
                                print("您的输入有误，请重新输入...")
                                time.sleep(2)
                                continue
                    
                    elif choice=="3":

                        while True:

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
                                
                                elif cai_num < no:
                                    input("你输入的数字过小，按任意键继续....")

                                else:
                                    print("恭喜您猜对了，共猜了",ci_shu,"次")
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
                while True:
                    smoke="香烟"
                    smoke_seria_number="1"
                    smoke_price="5~100元"
                    smoke_kind=2
                    snadks="零食"
                    snadks_seria_number="2"
                    snadks_price="1~20"
                    snadks_kind=2

                    # 展示购物超市页面
                    print("\t\t欢迎来到无人PY1901售货中心")
                    print("~*"*20)
                    print()
                    print("本商店有以下商品：")
                    print("种类编号\t商品种类\t种类价格区间\t商品种类数量")
                    print("%s\t\t%s\t\t%s\t\t%s"%(smoke_seria_number,smoke,smoke_price,smoke_kind))
                    print("%s\t\t%s\t\t%s\t\t%s"%(snadks_seria_number,snadks,snadks_price,snadks_kind))
                    print()
                    print("3.退出界面，返回商城")
                    print("4.退出登录")
                    print("~*"*20)

                    # 输入购买商品种类
                    purchase_seria_number=input("请输入您要选择的服务：")
                    
                    # 判断用户的选择
                    if purchase_seria_number=="3":
                        print("正在跳转...")
                        time.sleep(2)
                        break
                    
                    elif purchase_seria_number=="4":
                        print("正在退出登录")
                        time.sleep(2)
                        a=False
                        break

                    # 判断用户购买的商品种类
                    elif purchase_seria_number==smoke_seria_number:
                        huang_jy="黄金叶"   #香烟名称：黄金叶
                        huang_jy_seria="0101"     #黄金叶编号
                        huang_jy_price=int(10)     #黄金叶价格
                        huang_jy_kind=int(20)      #黄金叶库存
                        huang_hl="黄鹤楼"
                        huang_hl_seria="0102"
                        huang_hl_price=int(18)
                        huang_hl_kind=int(15)

                        # 展示详细商品
                        print("欢迎来到%s购买中心"%smoke)
                        print("~*"*20)
                        print()
                        print("商品编号\t商品名称\t商品价格\t商品库存")
                        print("%s\t\t%s\t\t%s\t\t%s"%(huang_jy_seria,huang_jy,huang_jy_price,huang_jy_kind))
                        print("%s\t\t%s\t\t%s\t\t%s"%(huang_hl_seria,huang_hl,huang_hl_price,huang_hl_kind))
                        print()
                        print("~*"*20)

                        while True:

                            # 用户选择购买的商品
                            purchase_smoke_seria_number=input("请输入您要购买商品的%s的编号："%smoke)

                            if purchase_smoke_seria_number == "0101" \
                            or purchase_smoke_seria_number == "0102":
                                break

                            else:
                                print("你输入的信息有误，请重新选择！")


                        while True:

                            # 用户选择购买数量
                            choice_num=int(input("请输入购买数量："))   #quantity  数量

                            # 判断购买的详细商品
                            if purchase_smoke_seria_number==huang_jy_seria:
                                buy=huang_jy        
                                
                                # 判断黄金叶是否充足
                                if huang_jy_kind-choice_num==0:
                                    money=choice_num*huang_jy_price  #price  价格
                                    huang_jy_kind-=choice_num
                                    huang_jy_kind=="此商品已售罄，暂时无货"
                                    break

                                elif huang_jy_kind-choice_num<0:
                                    print("此商品剩余不足请重新选择购买数量")
                                    continue
                                    
                                elif huang_jy_kind-choice_num>0:
                                    money=choice_num*huang_jy_price
                                    huang_jy_kind-=choice_num
                                    break

                            elif purchase_smoke_seria_number==huang_hl_seria: 
                                buy=huang_hl       
                                
                                # 判断黄鹤楼库存是否充足
                                if huang_hl_kind-choice_num==0:
                                    money=choice_num*huang_hl_price  #price  价格
                                    huang_hl_kind-=choice_num
                                    huang_hl_kind=="此商品已售罄，暂时无货"
                                    break
                                elif huang_hl_kind-choice_num<0:
                                    print("此商品剩余不足请重新选择购买数量")
                                    continue
                                elif huang_hl_kind-choice_num>0:
                                    money=choice_num*huang_hl_price
                                    huang_hl_kind-=choice_num
                                    break  

                    elif purchase_seria_number==snadks_seria_number:
                        wei_l="卫龙辣条"   #零食名称：卫龙辣条
                        wei_l_seria="0201"     #卫龙辣条编号
                        wei_l_price=int(2)     #卫龙辣条价格
                        wei_l_kind=int(100)      #卫龙辣条库存
                        shuang_h="双汇火腿肠"       #双汇火腿
                        shuang_h_seria="0202"
                        shuang_h_price=int(3)
                        shuang_h_kind=int(50)

                        print("欢迎来到%s购买中心"%snadks)
                        print("~*"*20)
                        print()
                        print("我们的零食有以下几种")
                        print("商品编号\t商品名称\t商品价格\t商品库存")
                        print("%s\t\t%s\t\t%s\t\t%s"%(wei_l_seria,wei_l,wei_l_price,wei_l_kind))
                        print("%s\t\t%s\t\t%s\t\t%s"%(shuang_h_seria,shuang_h,shuang_h_price,shuang_h_kind))

                        while True:
                            
                            #选择零食编号
                            choice=input("请输入您要购买商品的%s的编号：")    #choice：选择

                            if choice==wei_l_seria:
                                print("你选择的零食是%s"%(wei_l))
                                break

                            elif choice==shuang_h_seria:
                                print("您选择的零食是%s"%(shuang_h))
                                break

                            else:
                                print("您输入的编号有误，请重新选择")
                        
                        while True:
                        # 输入购买数量
                            choice_num=int(input("请输入购买数量"))

                            # 判断购买的详细商品
                            if choice==wei_l_seria:
                                buy=wei_l
                                    
                                # 判断辣条商品是否充足
                                if wei_l_kind>choice_num:
                                    money=choice_num*wei_l_price
                                    wei_l_kind-=choice_num
                                    break

                                elif wei_l_kind<choice_num:
                                    print("此商品剩余不足请重新选择购买数量")

                                elif wei_l_kind==choice_num:
                                    money=choice_num*wei_l_price
                                    wei_l_kind-=choice_num
                                    wei_l_kind="此商品已售罄"
                                    break
                            

                            elif choice==shuang_h_seria:
                                buy=shuang_h
                                    
                                    # 判断火腿肠是否充足
                                if shuang_h_kind>choice_num:
                                    money=choice_num*shuang_h_price
                                    shuang_h_kind-=choice_num
                                    break

                                elif shuang_h_kind<choice_num:
                                    print("此商品剩余不足请重新选择购买数量")

                                elif shuang_h_kind==choice_num:
                                    money=shuang_h_price*choice_num
                                    shuang_h_kind-=choice_num
                                    shuang_h_kind="此商品已售罄"
                                    break

                    print("你购买了%s，共%s件，总价%s元"%(buy,choice_num,money))
                    chioce=input("是否继续购买：是y,任意键结束")

                    # 询问顾客是否继续购买
                    if chioce=="y":
                        continue

                    # 付款
                    payment=float(input("请付款"))    #payment:付款
                    print("你共付了%s元，共消费了%s元，应找%s元"%(payment,money,payment-money))
                    print("购物结束，请拿好小票，欢迎下次光临！")

                    break

            # 修改密码
            elif choice=="3":
                while True:

                    print()
                    print("欢迎%s来到修改密码界面"%(admin[0]))
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
            admin=[user_name,password]
            # 注册用户：将用户列表，添加到系统用户变量中
            user_list.append(admin)

            print("注册成功,1秒后退出...")
            time.sleep(1)
            break

    elif choice=="3":
        print("系统将在1秒后退出...")
        time.sleep(1)
        break

    else:
        print("您的输入有误，请重新输入...")
        time.sleep(2)

print("退出系统成功！欢迎下次光临")
    


