import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LiveDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "live_data",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "live_data",
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle incoming data or broadcast it
        await self.channel_layer.group_send(
            "live_data",
            {
                'type': 'live_data_message',
                'message': data['message']
            }
        )

    async def live_data_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))