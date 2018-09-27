import json
from channels.generic.websocket import AsyncWebsocketConsumer

from apps.chat.models import Chat, Rooms


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        if self.user and not self.user.is_authenticated:
            return

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        full_name = "{} {}".format(self.user.first_name, self.user.last_name)
        if full_name == " ":
            full_name = "--"

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'message': message,
                'user_id': self.user.id,
                'publisher_full_name': full_name,
            }
        )

    async def chat_message(self, event):
        if self.user and not self.user.is_authenticated:
            return

        message = event['message']
        user_id = event['user_id']
        publisher_full_name = event['publisher_full_name']

        try:
            room = Rooms.objects.get(name=self.room_name)
        except Rooms.DoesNotExist:
            return

        chat_object = Chat.objects.create(user_id=self.user.id, text=message, room=room)

        created_at = chat_object.created_at.strftime('%H:%M:%S %Y/%m/%d')

        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'message': "{}".format(message),
            'created_at': created_at,
            'publisher_full_name': publisher_full_name,
        }))
