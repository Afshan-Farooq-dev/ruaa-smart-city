"""
Email utility functions for Smart City notifications
"""
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile


def send_welcome_email(user):
    """Send welcome email to new user"""
    if not user.email:
        print(f"⚠️ Cannot send email: User {user.username} has no email address")
        return False
    
    subject = 'Welcome to Smart City Saudi Arabia! 🏙️'
    
    # Render HTML template
    html_content = render_to_string('emails/welcome.html', {
        'user': user,
        'site_url': 'http://localhost:8000',  # Update for production
    })
    
    # Plain text fallback
    text_content = f"""
    Welcome to Smart City Saudi Arabia!
    
    Hello {user.first_name or user.username}!
    
    Thank you for joining Smart City Saudi Arabia. Explore real-time traffic, 
    discover attractions, find services, and more.
    
    Visit your dashboard: http://localhost:8000/dashboard/
    
    - The Smart City Team
    """
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    
    try:
        email.send()
        print(f"✅ Welcome email sent successfully to {user.email}")
        return True
    except Exception as e:
        print(f"❌ Error sending welcome email to {user.email}: {e}")
        return False


def send_traffic_alert(user, route_data):
    """Send traffic alert for subscribed route"""
    profile = getattr(user, 'profile', None)
    if not profile or not profile.email_traffic_alerts:
        return False
    
    # Status color mapping
    status_colors = {
        'Clear': '#10b981',
        'Moderate': '#f59e0b',
        'Heavy': '#ef4444',
        'Congested': '#dc2626'
    }
    
    subject = f"🚦 Traffic Alert: {route_data.get('name', 'Route')} - {route_data.get('status', 'Update')}"
    
    html_content = render_to_string('emails/traffic_alert.html', {
        'user': user,
        'route_name': route_data.get('name', 'Unknown Route'),
        'status': route_data.get('status', 'Unknown'),
        'city': route_data.get('city', 'N/A'),
        'area': route_data.get('area', 'N/A'),
        'description': route_data.get('description', ''),
        'recommendation': route_data.get('recommendation', ''),
        'status_color': status_colors.get(route_data.get('status', ''), '#f59e0b'),
        'site_url': 'http://localhost:8000',
    })
    
    text_content = f"""
    Traffic Alert: {route_data.get('name')}
    
    Status: {route_data.get('status')}
    City: {route_data.get('city')}
    Area: {route_data.get('area')}
    
    {route_data.get('description', '')}
    
    View full traffic map: http://localhost:8000/traffic/
    """
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    
    try:
        email.send()
        return True
    except Exception as e:
        print(f"Error sending traffic alert: {e}")
        return False


def send_tourism_digest(user, attractions):
    """Send weekly tourism digest"""
    profile = getattr(user, 'profile', None)
    if not profile or not profile.email_tourism_digest:
        return False
    
    subject = '🌟 Your Weekly Tourism Digest - Discover Saudi Arabia'
    
    html_content = render_to_string('emails/tourism_digest.html', {
        'user': user,
        'attractions': attractions[:5],  # Top 5 attractions
        'site_url': 'http://localhost:8000',
    })
    
    text_content = f"""
    Your Weekly Tourism Digest
    
    Hello {user.first_name or user.username}!
    
    Here are some attractions you might enjoy this week:
    
    """
    for attr in attractions[:5]:
        text_content += f"\n- {attr.get('name')} ({attr.get('city')})\n  {attr.get('description', '')[:100]}...\n"
    
    text_content += "\n\nExplore all attractions: http://localhost:8000/tourism/"
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    
    try:
        email.send()
        return True
    except Exception as e:
        print(f"Error sending tourism digest: {e}")
        return False


def send_batch_traffic_alerts(route_name, route_data):
    """Send traffic alerts to all users subscribed to a specific route"""
    users = User.objects.filter(
        profile__email_traffic_alerts=True,
        profile__subscribed_routes__contains=[route_name]
    )
    
    sent_count = 0
    for user in users:
        if send_traffic_alert(user, route_data):
            sent_count += 1
    
    return sent_count


def send_weekly_tourism_digests():
    """Send weekly tourism digest to all opted-in users"""
    from .data import TOURISM_DATA
    
    users = User.objects.filter(
        profile__email_tourism_digest=True
    )
    
    sent_count = 0
    for user in users:
        if send_tourism_digest(user, TOURISM_DATA):
            sent_count += 1
    
    return sent_count


def send_subscription_confirmation_email(user, route_data):
    """Send confirmation email when user subscribes to a route"""
    if not user.email:
        return False
    
    # Status color mapping
    status_colors = {
        'Clear': '#10b981',
        'Moderate': '#f59e0b',
        'Heavy': '#ef4444',
        'Congested': '#dc2626'
    }
    
    subject = f"✅ Subscribed to {route_data.get('name')} Traffic Alerts"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0;">
            <h1 style="margin: 0;">🔔 Subscription Confirmed!</h1>
        </div>
        <div style="background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px;">
            <p>Hello {user.first_name or user.username}!</p>
            <p>You're now subscribed to traffic alerts for <strong>{route_data.get('name')}</strong>.</p>
            
            <div style="background: white; padding: 20px; border-left: 4px solid {status_colors.get(route_data.get('status', ''), '#667eea')}; margin: 20px 0; border-radius: 5px;">
                <h3 style="margin-top: 0; color: {status_colors.get(route_data.get('status', ''), '#667eea')};">Current Status: {route_data.get('status', 'Unknown')}</h3>
                <p><strong>City:</strong> {route_data.get('city', 'N/A')}</p>
                <p><strong>Area:</strong> {route_data.get('area', 'N/A')}</p>
                <p>{route_data.get('description', '')}</p>
            </div>
            
            <p>You'll receive email notifications when traffic conditions change on this route.</p>
            
            <p style="color: #666; font-size: 12px; margin-top: 30px;">
                Manage your subscriptions anytime in <a href="http://localhost:8000/settings/">Settings</a>
            </p>
        </div>
    </body>
    </html>
    """
    
    text_content = f"""
    Subscription Confirmed!
    
    Hello {user.first_name or user.username}!
    
    You're now subscribed to traffic alerts for {route_data.get('name')}.
    
    Current Status: {route_data.get('status')}
    City: {route_data.get('city')}
    
    You'll receive email notifications when traffic conditions change.
    
    Manage subscriptions: http://localhost:8000/settings/
    """
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    
    try:
        email.send()
        print(f"✅ Subscription confirmation sent to {user.email}")
        return True
    except Exception as e:
        print(f"❌ Error sending subscription confirmation to {user.email}: {e}")
        return False


def send_settings_confirmation_email(user, profile):
    """Send confirmation email when user updates settings"""
    if not user.email:
        return False
    
    subject = "⚙️ Email Settings Updated"
    
    enabled_notifications = []
    if profile.email_traffic_alerts:
        enabled_notifications.append("🚦 Traffic Alerts")
    if profile.email_weather_alerts:
        enabled_notifications.append("🌤️ Weather Alerts")
    if profile.email_tourism_digest:
        enabled_notifications.append("🏛️ Tourism Digest")
    if profile.email_service_updates:
        enabled_notifications.append("🏥 Service Updates")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0;">
            <h1 style="margin: 0;">⚙️ Settings Updated</h1>
        </div>
        <div style="background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px;">
            <p>Hello {user.first_name or user.username}!</p>
            <p>Your email notification preferences have been updated successfully.</p>
            
            <div style="background: white; padding: 20px; margin: 20px 0; border-radius: 5px;">
                <h3 style="margin-top: 0;">Active Notifications:</h3>
                {"".join([f'<p style="margin: 10px 0;">✅ {notif}</p>' for notif in enabled_notifications]) if enabled_notifications else '<p>No notifications enabled</p>'}
                
                <p style="margin-top: 20px;"><strong>Frequency:</strong> {profile.email_frequency.capitalize()}</p>
                
                {f'<p style="margin-top: 20px;"><strong>Subscribed Routes:</strong> {len(profile.subscribed_routes)}</p>' if profile.subscribed_routes else ''}
            </div>
            
            <p>You can update these settings anytime.</p>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="http://localhost:8000/settings/" style="background: #667eea; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block;">Manage Settings</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    text_content = f"""
    Settings Updated
    
    Hello {user.first_name or user.username}!
    
    Your email notification preferences have been updated.
    
    Active Notifications:
    {"".join([f'- {notif}\\n' for notif in enabled_notifications]) if enabled_notifications else 'None'}
    
    Frequency: {profile.email_frequency}
    
    Manage settings: http://localhost:8000/settings/
    """
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    
    try:
        email.send()
        print(f"✅ Settings confirmation sent to {user.email}")
        return True
    except Exception as e:
        print(f"❌ Error sending settings confirmation to {user.email}: {e}")
        return False
        if send_tourism_digest(user, TOURISM_DATA):
            sent_count += 1
    
    return sent_count
