import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruaa.settings')
django.setup()

from django.contrib.auth.models import User

# Change this to your username
USERNAME = 'Afshan1'

try:
    user = User.objects.get(username=USERNAME)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f"✓ User '{user.username}' is now a superuser!")
    print(f"✓ You can now access admin at: http://127.0.0.1:8000/admin/")
    print(f"✓ Login with username: {user.username}")
except User.DoesNotExist:
    print(f"✗ User '{USERNAME}' not found!")
