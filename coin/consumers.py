import json
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer

#!CoinConsumer
class CoinConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'coin_room'
        await self.channel_layer.group_add(#allow you to talk between different instance of an application => Redis,RabbiqMq,Channel Layers allow us to create interaction between different instances of an application
            self.room_group_name,
            self.channel_name#create automaticiliy channel name
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def bring_coin(self,event):
        coins = event['coins']
        await self.send(json.dumps(coins))