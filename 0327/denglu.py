import redis
import pymysqlhelper
import hashlib
name = input('请输入用户名')
pwd = input('请输入密码')

sha1 = hashlib.sha1()
sha1.update(pwd.encode('utf8'))
pwd1 = sha1.hexdigest()

try:
    redis = redis.StrictRedis()
    r = redis.get('uname')

    if redis.get('uname') == name:
        print('ok')
    else:
        mysql = pymysqlhelper.MySqlHelper(_database='user')
        upwd = mysql.queryone('select upwd from userinfos where uname = %s', name)
        if upwd is None:
            print('用户名错误')
        elif upwd[0] == pwd1:
            redis.set('uname', name)
            print('登录成功！')
        else:
            print('密码错误！')

except Exception as e:
    print(e)
