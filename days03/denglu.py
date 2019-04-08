import random
import os
print("欢迎来到休闲小游戏")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
print("    1.石头剪刀布")
print("    2.老虎棒子鸡")
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

    print("系统正在出招")
    num=random.randint(0,2)   #产生随机数
    print("系统出招完成")

    user_Attacks=input("请您出招：石头、剪刀、布")  #Attacks：出招

    if (user_Attacks =="布" and num == 0) \
        or (user_Attacks =="石头" and num == 1) \
        or (user_Attacks =="剪刀" and num == 2):
        print("你太厉害了，竟然赢了电脑")

    elif (user_Attacks =="剪刀" and num == 0) \
        or (user_Attacks =="布" and num == 1) \
        or (user_Attacks =="石头" and num == 2):
        print("你输了，虽然输了，但不要灰心，再接再厉，下次一定会赢的！")

    elif (user_Attacks =="石头" and num == 0) \
        or (user_Attacks =="剪刀" and num == 1) \
        or (user_Attacks =="布" and num == 2):
        print("你和老板是亲戚吧，怎么总是平局...")
    

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

    print("系统正在出招")
    num=random.randint(0,3)   #产生随机数
    print("系统出招完成")

    user_Attacks=input("请出招：老虎、棒子、鸡、虫")

    if (user_Attacks =="老虎" and num == 2) \
        or (user_Attacks =="棒子" and num == 0) \
        or (user_Attacks =="鸡" and num == 3) \
        or (user_Attacks =="虫" and num == 1):
        print("你太厉害了，竟然赢了电脑")

    elif (user_Attacks =="老虎" and num == 1) \
        or (user_Attacks =="棒子" and num == 3) \
        or (user_Attacks =="鸡" and num == 0) \
        or (user_Attacks =="虫" and num == 2):
        print("你输了，虽然输了，但不要灰心，再接再厉，下次一定会赢的！")

    else:
        print("你和老板是亲戚吧，怎么总是平局...")
print("游戏结束...")
