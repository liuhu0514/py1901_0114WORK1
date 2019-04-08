import time,os
a=True
# 商品定义
h_jy=["1","黄金叶",10,20]
h_hl=["2","黄鹤楼",18,15]
smoke=[h_jy,h_hl]
while True:
    if a==False:
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
    print()
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

    # 选择商品
    choice=input("请选择服务：")

    for i in smoke:
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
                    print("您付款%s元，一共消费了%s元，找零%s元"%(fu_k,money,zhao_l))
                    is_ok=input("是否继续购买：继续y，任意键结束")
                    if is_ok=="y":
                        print("请稍等...")

                        break
                    else:
                        print("正在退出...")
                        a=False
                        time.sleep(2)
                        break


                else:
                    print("您的付款不足，请重新付款.")
                    time.sleep(1)

                    continue




        else:
            print("你要的服务暂时没有，稍后请重新选择...")
            time.sleep(2)
            continue

    

    break

print("欢迎下次光临，祝您生活愉快，请慢走...")