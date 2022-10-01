import requests
from celery import shared_task
from channels.layers import get_channel_layer#You'll often want to send to the channel layer from outside of the scope of a consumer, and so you won't have self.channel_layer. In this case, you should use the get_channel_layer function to retrieve it:
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

from .models import Coin


#?channel_layer
channel_layer = get_channel_layer()

#!get_coins_data
@shared_task(bind=True,name='get_coins_data')
def get_coins_data(self):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    coins = requests.get(url).json()

    coins_list = []
    
    for coin in coins:
        coin_obj,created = Coin.objects.get_or_create(symbol=coin['symbol'])
        coin_obj.name = coin['name']
        coin_obj.symbol = coin['symbol']
        
        if coin_obj.price > coin['current_price']:
            state = 'fall'
            print('FALL...')
        elif coin_obj.price == coin['current_price']:
            state = 'same'
            print('SAME...')
        elif coin_obj.price < coin['current_price']:
            state = 'raise'
            print('RAISE...')
        
        #save
        coin_obj.image = coin['image']
        coin_obj.price = coin['current_price']
        coin_obj.rank = coin['market_cap_rank']
        coin_obj.save()

        print('Created Coin Object...')
        
        new_data = model_to_dict(coin_obj)
        new_data.update({'state':state})
        coins_list.append(new_data)
    
    async_to_sync(channel_layer.group_send)('coin_room',{'type':'bring_coin','coins':coins_list})