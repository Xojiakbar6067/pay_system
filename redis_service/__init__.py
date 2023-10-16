import redis

#sozdat podklyucheniya k redis
redis_db = redis.from_url('redis://redis_db')

#sozdat zapis v baze dannix
redis_db.set('spam',10) #{'spam': 10}

#poluchit znacheniya iz bazi
data = redis_db.get('spam')
print(data)

#zadat vremya sushestvovaniya peremennoy
redis_db.set('spam2', 'hello', 5)
date2 = redis_db.get('spam2')
print(date2)