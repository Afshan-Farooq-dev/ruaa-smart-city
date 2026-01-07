import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruaa.settings')
django.setup()

from django.contrib.auth.models import User

try:
    admin = User.objects.get(username='Admin')
    print(f"Username: {admin.username}")
    print(f"Is superuser: {admin.is_superuser}")
    print(f"Is staff: {admin.is_staff}")
    print(f"Is active: {admin.is_active}")
    print(f"Email: {admin.email}")
    print("-" * 40)
    
    if not admin.is_staff:
        admin.is_staff = True
        admin.save()
        print("✓ Fixed: Set is_staff to True")
    
    if not admin.is_active:
        admin.is_active = True
        admin.save()
        print("✓ Fixed: Set is_active to True")
        
    print("\n✓ Admin user is properly configured!")
    print("✓ You can login at: http://127.0.0.1:8000/admin/")
    print(f"✓ Username: {admin.username}")
    
except User.DoesNotExist:
    print("✗ Admin user not found!")
