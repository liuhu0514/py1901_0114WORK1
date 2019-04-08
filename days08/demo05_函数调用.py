'''
函数的调用
    函数间的调用
    函数自己调用自己
'''
# 函数之间的互相调用
# def func_a():
#     print("func_a函数执行了")
#     # 调用执行其他函数
#     func_b()
#
#
# def func_b():
#     print("func_b函数执行了")
#
#
# # 程序启动，调用执行了func_a()函数
# func_a()


# 函数自己调用自己：函数递归调用
def func_c():
    r = input("按任意键继续，按R键结束")
    if r == "R":
        return
    # 调用当前函数自己
    return func_c()

    # 执行一句话
    # print("*********************")


func_c()
