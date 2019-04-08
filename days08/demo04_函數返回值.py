'''
函数返回值
'''
# def calculations(num1, num2, opra):
#     '''计算器函数'''
#     res = ""
#     if opra == "+":
#         res = num1 + num2
#     elif opra == "-":
#         res = num1 - num2
#     elif opra == "*":
#         res = num1 * num2
#     elif opra == "/":
#         res = num1 / num2
#
#     return res
#
#
# r = calculations(12, 10, '*')
# print(r)


def calculations(num1, num2, opra):
    '''计算器函数'''
    res = ""
    if opra == "+":
        res = num1 + num2
    elif opra == "-":
        res = num1 - num2
    elif opra == "*":
        res = num1 * num2
    elif opra == "/":
        res = num1 / num2

    return num1, num2, opra, res


n1, n2, o, r = calculations(12, 10, '*')
print("运算数据：", n1, "--", n2, "运算符号：", o, "运算结果：", r)