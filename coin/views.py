from django.shortcuts import render
import requests
# Create your views here.

#!indexView
def indexView(request):
    #?For Testing
    # url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    # coins = requests.get(url).json()
    # print('len coind ', len(coins))
    return render(request,'index.html')