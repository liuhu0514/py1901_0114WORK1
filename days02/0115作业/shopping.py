print("\t\t\t\t欢迎来到小飞虎无人购物中心")
print("本购物中心有以下商品")
print("商品编号\t商品名称\t商品价格\t库存")
print("01\t\t黄金叶\t\t10\t\t20")
print("02\t\t黄鹤楼\t\t18\t\t15")
print("03\t\t玉溪\t\t25\t\t16")
mai_bh=input("请输入购买商品编号")
mai_count=int(input("请输入都买数量"))

if mai_bh=="01":
    money=int(mai_count*10)
    mai_bh="黄金叶"
    print("您选择买的是：黄金叶\n购买了%s件\n总价格为：%s"%(mai_count,money))
elif mai_bh=="02":
    mai_bh="黄鹤楼"
    money=int(mai_count*18)
    print("您选择买的是：黄鹤楼\n购买了%s件\n总价格为：%s"%(mai_count,money))
elif mai_bh=="03":
    mai_bh="玉溪"
    money=int(mai_count*25)
    print("您选择买的是：玉溪\n购买了%s件\n总价格为：%s"%(mai_count,money))

s_money=float(input("请付款"))

while True :
    if s_money<money:
        print("您的付款不足，请重新付款")
    else:
        z_money=s_money-money
        break
print("您选择买的是：%s\n购买了%s件\n总价格为：%s\n您共付了%s\n找零%s\n"%(mai_bh,mai_count,money,s_money,z_money))
print("打印小票，请拿好小票！")
    