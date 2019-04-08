# 导入模块
import pymysql

# 创建链接实例
con = pymysql.Connect(user="root",password="123456",database="goods")

# 创建游标对象
cursor = con.cursor()
# 通过游标操作数据库
cursor.execute('select * from user')
# 获取游标中数据
result = cursor.fetchall()
print(result)
# 释放连接实例
cursor.close()
con.close()

