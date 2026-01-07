"""
Test email sending functionality
Run: python test_email.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruaa.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

print("=" * 50)
print("EMAIL CONFIGURATION TEST")
print("=" * 50)
print(f"Backend: {settings.EMAIL_BACKEND}")
print(f"Host: {settings.EMAIL_HOST}")
print(f"Port: {settings.EMAIL_PORT}")
print(f"User: {settings.EMAIL_HOST_USER}")
print(f"From: {settings.DEFAULT_FROM_EMAIL}")
print(f"Password configured: {'Yes' if settings.EMAIL_HOST_PASSWORD else 'No'}")
print(f"Password length: {len(settings.EMAIL_HOST_PASSWORD) if settings.EMAIL_HOST_PASSWORD else 0}")
print("=" * 50)

# Test sending email
try:
    print("\nSending test email...")
    result = send_mail(
        subject='Test Email from Smart City App',
        message='This is a test email. If you receive this, email is working!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_HOST_USER],  # Send to yourself
        fail_silently=False,
    )
    print(f"✅ Email sent successfully! (Result: {result})")
    print(f"Check inbox: {settings.EMAIL_HOST_USER}")
except Exception as e:
    print(f"❌ Error sending email:")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    print("\nCommon issues:")
    print("1. App password has spaces - remove them")
    print("2. App password not generated correctly")
    print("3. 2-Step Verification not enabled on Google account")
    print("4. 'Less secure app access' needed (if not using app password)")
