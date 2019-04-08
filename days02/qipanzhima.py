h=int(input("请输入棋盘高："))
w=int(input("请输入棋盘宽："))
f=int(input("请输入第一个方格的数量："))
one_weight=float(input("请输入一个芝麻的重量"))
zong_ge=h*w
i=0
y=0
for i in range(zong_ge):
    y=y+f*(2**i)
    i+=1
print(y)
zong_zhong=y*one_weight
print("高为：%s;宽为：%s的棋盘\n总格数为：%s。\n第一个格数的芝麻为%s,总芝麻数为：%s"%(h,w,zong_ge,f,y))
print("总重量为：",zong_zhong)
