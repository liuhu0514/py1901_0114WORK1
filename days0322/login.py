import pymysqlhelper as sql

# result = sql.MySqlHelper().queryone("select * from user where name = %s", ('lh1',))
# print(result)

# r = sql.MySqlHelper().update("insert into user(id,name) values(0,'你好')")
r = sql.MySqlHelper().querymany("select * from user", 3)
print(r)


