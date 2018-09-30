from django.core.management.base import BaseCommand

from apps.chat.models import Rooms


class Command(BaseCommand):
    def handle(self, *args, **options):
        Rooms.objects.create(name='python', description='Talk about python')
        Rooms.objects.create(name='django', description='Talk about django projects')
        Rooms.objects.create(name='reactjs', description='Talk about react.js projects')
