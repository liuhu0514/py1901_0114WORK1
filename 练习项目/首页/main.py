import os
smoke="香烟"
smoke_seria_number="0100"
smoke_price="5~100元"
smoke_kind=2
snadks="零食"
snadks_seria_number="0200"
snadks_price="1~20"
snadks_kind=4

os.system("cls")
# 展示首页
print("\t\t欢迎来到小虎无人售货中心")
print("~*"*20)
print()
print("本商店有以下商品：")
print("种类编号\t商品种类\t种类价格区间\t商品种类数量")
print("%s\t\t%s\t\t%s\t\t%s"%(smoke_seria_number,smoke,smoke_price,smoke_kind))
print("%s\t\t%s\t\t%s\t\t%s"%(snadks_seria_number,snadks,snadks_price,snadks_kind))
print()
print("~*"*20)

# 输入购买商品种类
purchase_seria_number=input("请输入您要购买商品种类的编号")

os.system("cls")
# 判断用户购买的商品种类
if purchase_seria_number==smoke_seria_number:
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

# 付款
payment=float(input("请付款"))    #payment:付款
print("你共付了%s元，共消费了%s元，应找%s元"%(payment,money,payment-money))
print("购物结束，请拿好小票，欢迎下次光临！")


