from fastapi import APIRouter, Depends
import requests

from redis_service import redis_db

currensy_router = APIRouter(prefix='/currency', tags=['Kurs valyuti'])

#proverka redis bazi estli tam informatsiya o kurse valyut
def _check_currency_rates_redis():
    usd = redis_db.get('rates')
    rub = redis_db.get('rates')
    eur = redis_db.get('rates')
    jpy = redis_db.get('rates')
    if usd and rub and eur and jpy:
        return {'USD': usd.decode(), 'RUB': rub.decode(), 'EUR': eur.decode(), 'JPY': jpy.decode()}
    return False

#zapros na polucheniya vsex kursov valyuti

@currensy_router.post('/get-rates')
async def get_currency_rates(redis_checker=Depends(_check_currency_rates_redis)):
    #esli v redise est dannie to pokazivaem ottuda
    if redis_checker:
        print('dostal iz redisa')
        return {'status': 1, 'rates': redis_checker}

    #a esli v redise nichego net, perexodim po silke i zapisavaem

    cb_url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'

    response = requests.get(cb_url).json()

    #sohranyay tolko te valyuti kotorie nam nujni
    usd_eur_rub_jpy = [i for i in response if i['Ccy'] in ['EUR', 'RUB', 'USD', 'JPY']]

    #sohranim v redis bazu
    redis_db.set('USD', usd_eur_rub_jpy[0]['Rate'], 5)
    redis_db.set('EUR', usd_eur_rub_jpy[1]['Rate'], 5)
    redis_db.set('RUB', usd_eur_rub_jpy[2]['Rate'], 5)
    redis_db.set('JPY', usd_eur_rub_jpy[3]['Rate'], 5)
    print('not redis')

    return {'status': 1, 'rates': usd_eur_rub_jpy}