import redis

r = redis.Redis()

for k in r.keys():
    if k.startswith(b'[c'):
        print (k)
        r.delete(k)
