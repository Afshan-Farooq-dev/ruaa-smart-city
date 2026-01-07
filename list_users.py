import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruaa.settings')
django.setup()

from django.contrib.auth.models import User

print("Existing users in database:")
print("-" * 40)
for user in User.objects.all():
    superuser = "✓ SUPERUSER" if user.is_superuser else "✗ Regular"
    print(f"{user.username} - {superuser}")
print("-" * 40)
print(f"Total users: {User.objects.count()}")
