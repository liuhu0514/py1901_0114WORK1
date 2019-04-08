'''
    猜字游戏：系统自动产生一个数字，然后用户根据提示猜数字
             本游戏有项目积分
'''

import os,sys,random,time

chu_shi_fen=10
while True:
    # 定义一个变量记录用户猜测的次数
    ci_shu = 0

    # 清除
    os.system("cls")
    # 首页展示
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
            chu_shi_fen-=1
            input("你输入的数字过大，按任意键继续...您共剩余%s"%chu_shi_fen)
        
        elif cai_num < no:
            chu_shi_fen-=1
            input("你输入的数字过小，按任意键继续....您共剩余%s"%chu_shi_fen)

        else:
            chu_shi_fen-=1
            chu_shi_fen+=5
            print("恭喜您猜对了，共猜了",ci_shu,"次","您共剩余",chu_shi_fen,"分")
            break
    
    # 提示用户是否继续玩
    is_player=input("是否继续：继续y,结束按任意键退出游戏")

    # 判断用户输入
    if is_player == "y":
        continue
    
    else:
        print("游戏结束！")
        sys.exit(1)


