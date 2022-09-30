import requests
from celery import shared_task

from .models import Coin

#!get_coins_data
@shared_task(bind=True,name='get_coins_data')
def get_coins_data(self):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    coins = requests.get(url).json()
    
    for coin in coins:
        coin_obj,created = Coin.objects.get_or_create(symbol=coin['symbol'])
        if created:
            print('Created Coin Obj,because not in database before')
            coin_obj.name = coin['name']
            coin_obj.symbol = coin['symbol']
            coin_obj.image = coin['image']
            coin_obj.price = coin['current_price']
            coin_obj.rank = coin['market_cap_rank']
            
            coin_obj.save()