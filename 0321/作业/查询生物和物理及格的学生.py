import pymysql

try:
    # 创建数据库连接实例
    con = pymysql.Connect(user="root",password="123456",database="school")
    # 创建游标对象
    cursor = con.cursor()
    # 通过游标操作数据库、
    cursor.execute("select sid,sname from student inner join \
        (select t1.stuid,t1.biology_score,t2.physical_score from \
        (select stuid,score as biology_score from score where courseid = \
        (select cid from course where cname = \"生物\") ) as t1  inner join \
        (select stuid,score as physical_score from score where courseid =\
            (select cid from course where cname = \"物理\"))  as t2\
        on t1.stuid = t2.stuid\
        having biology_score >= 60 and physical_score >= 60) as t3\
        on t3.stuid = student.sid;")
    num = cursor.fetchall()
    print(num)
except Exception as e:
    print(e)

finally:
    # 释放连接实例
    cursor.close()
    con.close()