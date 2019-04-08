"""
异常处理语法
"""
"""
1. 异常处理步骤
    1.1 程序运行出现异常
        ValueError: invalid literal for int() with base 10: 'a'
    1.2 捕捉出现的异常
        python中提供了一种步骤异常的语法
        ----------------------------
        try:  尝试执行
            可能出现异常的代码
        except 要捕捉的异常类型:
            处理异常的代码
        ----------------------------
    1.3 处理捕捉到的异常
    
    1.4 处理捕捉到的多个异常
    
    1.5 那么多异常，我怎么一个一个去处理？
        全部异常捕捉
        
    1.6 不论是否出现异常，我都想执行一些代码
        我不管你系统中有木有异常，最终我都要关闭一个文件：回收资源的代码
        python中的异常语法体系中，提供了一个关键字:final
            不论try中是否出现异常，final中的代码必须最后执行
            
    1.7 else关键字
        异常模块中，代码执行如果不出现异常，才会执行的代码
        
    1.8 自定义异常---异常转换
        问题：系统出现的异常，好难理解~
            多人协同开发，出现异常抛出异常给别人，不好处理
            
软件开发过程中的两个专业术语：
    容错：
        程序运行过程中，包容用户在操作时出现的失误
        这样的失误产生的错误不会导致程序崩溃
    
    容灾：
        灾难性错误！
"""
# 1. 第一个步骤，出现异常
# choice = int(input("请输入选项："))
# print(f"用户输入了一个选项：{choice}")

# 2. 捕捉异常
# choice = None
# try:
#     choice = int(input("请输入选项："))
# except ValueError as e:
#     pass
#
# print(f"用户输入了一个选项：{choice}")


# 3. 处理一个异常
# def input_choice():
#     choice = None
#     try:
#         # 用户输入选项
#         choice = int(input("请输入选项："))
#     except ValueError as e:
#         # 用户输入了非法选项
#         print("用户输入了非法选项")
#         return input_choice()
#     return choice
#
#
# print(f"用户输入了一个选项：{input_choice()}")

# 4. 处理多个异常
# def input_choice():
#     choice = None
#     try:
#         # 用户输入选项
#         choice = int(input("请输入选项："))
#         if choice == 1:
#             # 打开C盘的一个文件
#             file = open("c:/test.txt", "r")
#         elif choice == 2:
#             # 打开D盘的一个文件
#             file = open("d:/test.txt", "r")
#     except (ValueError,FileNotFoundError) as e:
#         # 用户输入了非法选项
#         print("系统出现错误【系统功能正在升级中...】")
#         return input_choice()
#     return choice
#
#
# print(f"用户输入了一个选项：{input_choice()}")

# 5. 处理所有异常
# def input_choice():
#     choice = None
#     try:
#         # 用户输入选项
#         choice = int(input("请输入选项："))
#         if choice == 1:
#             # 打开C盘的一个文件
#             file = open("c:/test.txt", "r")
#         elif choice == 2:
#             # 打开D盘的一个文件
#             file = open("d:/test.txt", "r")
#     # except:
#     except Exception as e:
#         # 用户输入了非法选项
#         print("系统出现错误【系统功能正在升级中...】")
#         return input_choice()
#     return choice
#
#
# print(f"用户输入了一个选项：{input_choice()}")

# 6.  final关键字
try:
    choice = int(input("请输入选项："))
except:
    print("出现异常")
finally:
    # 通过语法明确的告诉所有人：这是异常处理中的代码，用来回收数据资源
    print("异常处理完成，必须执行的代码....")

# 异常外面的代码，它可能都不属于异常这个部分
print("正常代码")

# 7. else关键字
# try:
#     choice = int(input("请输入选项："))
# except:
#     print("出现异常")
# else:
#     print("程序中没有出现异常")
# finally:
#     # 通过语法明确的告诉所有人：这是异常处理中的代码，用来回收数据资源
#     print("异常处理完成，必须执行的代码....")
#
# # 异常外面的代码，它可能都不属于异常这个部分
# print("正常代码")


# 8. 抛出异常
# 将系统中比较难懂的异常，转换成和业务相关的异常，抛出给调用者处理，有利于业务的健壮性

# 自定义异常
# class Shuru_Exception(Exception):
#
#     def __init__(self, info):
#         super().__init__(info)
#
#
# # 开发人员A
# def input_choice():
#     try:
#         choice = int(input("请输入选项："))
#     except:
#         # 抛出一个让调用的人必须处理的异常
#         # raise Exception("输入了非法选项.")
#         raise Shuru_Exception("输入了非法选项.")
#     return choice
#
# # 开发人员B
# c = input_choice()
# print(f"用户输入了选项：{c}")
#ValueError: invalid literal for int() with base 10: 'A'
