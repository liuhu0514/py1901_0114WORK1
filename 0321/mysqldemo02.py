import pymysql
username = input("请输入用户名：")
pwd = input("请输入密码：")
try:
    # 创建连接实例
    con = pymysql.Connect(user=username, password=pwd)
    # 引入数据库
    con.select_db("goods")
    # 创建游标对象
    cursor = con.cursor()
    # 通过游标操作数据库
    cursor.execute("select * from user")
    # 获取数据
    a = cursor.fetchall()
    # 打印数据
    print(a)
except Exception:
    print("您的输入有误")
finally:
    # 关闭数据库
    cursor.close()
    con.close()

