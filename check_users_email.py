"""
Check which users have email addresses
Run: python check_users_email.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruaa.settings')
django.setup()

from django.contrib.auth.models import User

print("=" * 60)
print("USER EMAIL STATUS")
print("=" * 60)

users = User.objects.all()
for user in users:
    status = "✅ Has email" if user.email else "❌ No email"
    print(f"{user.username:20} | {user.email:30} | {status}")

print("=" * 60)
print(f"Total users: {users.count()}")
print(f"Users with email: {users.exclude(email='').count()}")
print(f"Users without email: {users.filter(email='').count()}")
