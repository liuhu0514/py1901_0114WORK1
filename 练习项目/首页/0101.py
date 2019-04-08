lists=list()

while True:
    a=input("请输入a")
    if a=="n":
        break
    b=input("请输入b")
    admin=[a,b]
    lists.append(admin)
    print("lists是",lists)
lists[0][1]="666"
print (lists[0][1])
print(lists)
for x,(i,y) in lists:
    print(x,(i,y))