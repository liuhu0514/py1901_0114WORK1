# t=10
# while t > 0:
#     t-=1

#     # 显示票数详情
#     print("已经卖出了",10-t,"张票")
#     print("还剩",t,"张票")

#     # 确认是否有突发状况
#     shu_ru=input("是否出现突发状况，如果有：y,没有：任意键继续")

#     if shu_ru == "y":
#         print("遇到紧急状况，结束卖票！")
#         break

# else:
#     print("票已售罄，结束卖票")

# # 结束提示
# print("可以下班了，结束回家")
    
# 总共的票数
ticket = 10

# 卖票的过程
while ticket > 0:
    ticket -= 1

    # 卖出票数详情
    print("已经卖出",10-ticket,"张票",)

    # 剩余票数详情
    print("剩余",ticket,"张票")

    # 是否有紧急事件发生
    exigency = input("是否有紧急情况:有y,没有任意键继续")
    

    # 有突发事件发生
    if exigency == "y":
        print("有紧急情况发生，暂停售票")

        is_not = input("紧急情况是否结束：结束任意键继续售票，没有n结束本次售票")

        if is_not == "n":
            break

        



else:
    print("票已卖完可以下班")



