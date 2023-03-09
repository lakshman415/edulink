
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edulink.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    username = input("Enter username: ")
    email = input("Enter email address: ")
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return

    try:
        user = User.objects.create_superuser(username, email, password)
        print(f"Superuser {username} created successfully.")
    except Exception as e:
        print(f"Error creating superuser: {str(e)}")

if __name__ == '__main__':
    create_superuser()
