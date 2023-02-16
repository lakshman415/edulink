from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a new superuser account'

    def handle(self, *args, **options):
        UserModel = get_user_model()
        user_data = {
            'username': 'lakshman',
            'email': 'lakshman@gmail.com',
            'password': 'lakshman',
        }
        UserModel._default_manager.db_manager().create_superuser(**user_data)
