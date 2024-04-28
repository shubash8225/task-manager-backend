from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a new user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the new user')
        parser.add_argument('password', type=str, help='Password for the new user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS('User created successfully'))
        else:
            self.stdout.write(self.style.ERROR('User with this username already exists'))
