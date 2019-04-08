import pymysql

try:
    # 创建数据库连接实例
    con = pymysql.Connect(user="root",password="123456",database="school")
    # 创建游标对象
    cursor = con.cursor()
    # 通过游标操作数据库、
    cursor.execute("select count(*) from student;")
    num = cursor.fetchone()
    print(num)
except Exception as e:
    print(e)

finally:
    # 释放连接实例
    cursor.close()
    con.close()
