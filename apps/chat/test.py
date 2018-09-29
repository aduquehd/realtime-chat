import datetime
import json
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from apps.chat.models import Chat, Rooms


class ChatAPITests(TestCase):

    def setUp(self):
        user = User(username='andresduque', first_name='Andres', last_name='Duque')
        user.set_password('123456')
        user.save()
        room = Rooms(name='python', description='Talk about python')
        room.save()

        Chat.objects.get_or_create(user=user, room=room, message='Hello world!')
        Chat.objects.get_or_create(user=user, room=room, message='how are you?!')

    def test_list(self):
        room = Rooms.objects.first()

        url = reverse('chat:get-rooms-api', kwargs={'room_id': room.id})

        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

        data = json.loads(response.content)

        for result in data:
            chat = Chat.objects.get(id=result['id'])
            self.assertEquals(result['publisher_full_name'], "{} {}".format(chat.user.first_name, chat.user.last_name))
            datetime.datetime.strptime(result['created_at'], '%H:%M:%S %Y/%m/%d')
            datetime.datetime.strptime(result['updated_at'], '%H:%M:%S %Y/%m/%d')
