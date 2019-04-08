'''
函数的定义：
    四种不同的操作方式
'''


# 需求：开窗通风
def open_window():
    '''开窗口通风的函数'''
    print("中午下课时")
    print("打开两个大窗户，打开门")
    print("通风一个小时，不容易生病")


# 调用执行
# open_window()


# 需求：收快递
def receive_thing():
    '''收取快递的行为'''
    # 函数中的执行过程
    print("帮我收一个快递")
    print("门口快递架")
    print("防辐射丝袜")
    # 返回结果
    return "防辐射丝袜"


# 调用执行
# thing = receive_thing()
# print("收到的快递：", thing)


# 需求：购买年会表演服
def buy_clothe(format, money):
    '''购买年会衣服函数'''
    print("购买的衣服款式：", format)
    print("购买衣服的资金：", money)
    print("购买完成，等待年会开始.....")


# 调用执行函数  提供执行函数需要的数据
# buy_clothe("燕尾服", 1888)
# buy_clothe("丝袜", 500)


# 需求(需要的功能，要求的限制)：买烟的行为
def buy_smoke(name, money):
    if 10 < money < 13:
        print("可以购买万宝路")
        res = "万宝路"
    elif money < 10:
        print("买个棒棒糖戒烟吧.....")
        res = "棒棒糖"
    else:
        print("可以购买黄金叶....")
        res = "黄金叶"
    print("老刘需要购买的是：", name)
    return res


# 调用执行：需要提供数据、需要接收返回数据
smoke = buy_smoke("中华", 9)
print("购买结果：", smoke)

smoke2 = buy_smoke("利群", 20)
print("购买结果：", smoke2)
