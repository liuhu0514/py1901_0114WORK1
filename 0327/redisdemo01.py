import redis
try:
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    a = r.keys('*')
    print(a)
except Exception as e:
    print(e)
