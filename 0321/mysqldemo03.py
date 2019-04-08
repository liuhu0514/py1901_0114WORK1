
import pymysql


def engn():
    username = input("请输入用户名:")
    pwd = input("请输入密码")
    return cun(username, pwd)


def cun(username, pwd):
    try:
        con = pymysql.Connect(user=username, password=pwd)
        con.select_db("goods")
        cursor = con.cursor()
        cursor.execute(f"insert into user values(0,\"王柳\",\"郑州\")")
        con.commit()
        cursor.close()
        con.close()
    except:
        input("您的用户名或者密码错误！请重新登录")
        return engn()


if __name__ == "__main__":
    engn()
