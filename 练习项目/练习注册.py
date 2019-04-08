


usrelist=list([])
admin=list([])

while True:
    admin=list([])

    user=input("请输入账户：")
    password=input("请输入密码：")

    admin.append(user)
    admin.append(password)
    usrelist.append(admin)
    a=input("是否继续添加：继续y,退出任意键")
    if a=="y":
        continue
    else:
        break
 
    


print(usrelist)