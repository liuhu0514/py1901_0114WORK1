'''
    调用函数  四种类型
'''


# 有条件 不返回结果
def buy(leixing, money):
    print("给你钱", money)
    print("物品类型", leixing)


buy("裙子",100)


# 有条件需要返回结果
def buy_smoke(smoke, money):
    if 1 <= money < 10:
        print("买什么烟啊")
        res = "棒棒糖"

    elif money == 10:
        print("只能买个黄金叶")
        res = "黄金叶"

    else:
        print("买个黄鹤楼")
        res = "黄鹤楼"
    print("要求购买的烟是：", smoke)
    return res


thing = buy_smoke("中华", 10)
print("买的是：", thing)


# 无条件不需要结果
def open_window():
    # 打开窗户 开窗通风
    print("去吧窗户打开")
    print("下课打开窗户")
    print("开窗通风身体好")
