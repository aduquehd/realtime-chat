from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = "superadmin"
        password = "123456"
        email = "admin@admin.com"

        if User.objects.filter(username=username).exists():
            print("-- Superuser with username: {} already exists".format(username))
        else:
            print("-- Creating superuser with username: {}, email: {}, and password: {}".format(
                username, email, password
            ))
            user = User.objects.create_superuser(username, email, password)
            user.save()
