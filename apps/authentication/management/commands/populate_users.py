from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User(username='andresduque', first_name='Andres', last_name='Duque')
        user.set_password('123456')
        user.save()

        user = User(username='nelsonmartinez', first_name='Nelson', last_name='Martinez')
        user.set_password('123456')
        user.save()

        user = User(username='wendylugo', first_name='Wendy', last_name='Lugo')
        user.set_password('123456')
        user.save()
