"""
Send test welcome email to a specific user
Run: python send_test_welcome.py username
Example: python send_test_welcome.py Afshan1
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruaa.settings')
django.setup()

from django.contrib.auth.models import User
from main.email_utils import send_welcome_email

if len(sys.argv) < 2:
    print("Usage: python send_test_welcome.py <username>")
    print("\nAvailable users with emails:")
    for user in User.objects.exclude(email=''):
        print(f"  - {user.username} ({user.email})")
    sys.exit(1)

username = sys.argv[1]

try:
    user = User.objects.get(username=username)
    
    if not user.email:
        print(f"❌ User '{username}' has no email address!")
        sys.exit(1)
    
    print(f"Sending welcome email to {user.username} ({user.email})...")
    result = send_welcome_email(user)
    
    if result:
        print(f"\n✅ SUCCESS! Check inbox: {user.email}")
    else:
        print(f"\n❌ Failed to send email. Check console output above for errors.")
        
except User.DoesNotExist:
    print(f"❌ User '{username}' not found!")
    print("\nAvailable users:")
    for user in User.objects.all():
        print(f"  - {user.username}")
