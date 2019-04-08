import random as r

users="6"
while True:
    user=list()
    for i in range(1):
        user.append(str(r.randint(0,9)))
    user="".join(user)
    if user==users:
        continue
    else:
        print("你的账号为",user)
        break