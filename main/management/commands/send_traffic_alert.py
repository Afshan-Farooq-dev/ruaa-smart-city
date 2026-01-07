"""
Management command to send traffic alerts for a specific route
Usage: python manage.py send_traffic_alert "King Fahd Road"
"""
from django.core.management.base import BaseCommand
from main.email_utils import send_batch_traffic_alerts
from main.data import TRAFFIC_DATA


class Command(BaseCommand):
    help = 'Send traffic alerts to users subscribed to a specific route'

    def add_arguments(self, parser):
        parser.add_argument('route_name', type=str, help='Name of the route')

    def handle(self, *args, **options):
        route_name = options['route_name']
        
        # Find route data
        route_data = None
        for area, info in TRAFFIC_DATA.items():
            if area == route_name:
                route_data = {
                    'name': area,
                    'status': info.get('status', 'Unknown'),
                    'city': info.get('city', 'N/A'),
                    'area': info.get('area_ar', 'N/A'),
                    'description': info.get('description', ''),
                    'recommendation': f"Current status: {info.get('status', 'Unknown')}"
                }
                break
        
        if not route_data:
            self.stdout.write(
                self.style.ERROR(f'Route "{route_name}" not found in TRAFFIC_DATA')
            )
            return
        
        self.stdout.write(f'Sending alerts for {route_name}...')
        sent_count = send_batch_traffic_alerts(route_name, route_data)
        self.stdout.write(
            self.style.SUCCESS(f'Successfully sent {sent_count} traffic alert emails')
        )
