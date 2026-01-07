"""
Management command to send weekly tourism digest emails
Usage: python manage.py send_tourism_digest
"""
from django.core.management.base import BaseCommand
from main.email_utils import send_weekly_tourism_digests


class Command(BaseCommand):
    help = 'Send weekly tourism digest emails to all subscribed users'

    def handle(self, *args, **options):
        self.stdout.write('Sending weekly tourism digests...')
        sent_count = send_weekly_tourism_digests()
        self.stdout.write(
            self.style.SUCCESS(f'Successfully sent {sent_count} tourism digest emails')
        )
