from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    """User reviews and ratings for attractions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    attraction_name = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)  # For moderation
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return f"{self.user.username} - {self.attraction_name} ({self.rating}★)"

class UserProfile(models.Model):
    """Extended user profile for personalized recommendations"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    interests = models.JSONField(default=list)  # ['Historical', 'Nature', 'Museum']
    favorites = models.JSONField(default=list)  # ['Kingdom Centre Tower', 'Diriyah']
    visited = models.JSONField(default=list)  # ['Al Masmak Fortress']
    
    # Email notification preferences
    email_traffic_alerts = models.BooleanField(default=True)
    email_weather_alerts = models.BooleanField(default=True)
    email_tourism_digest = models.BooleanField(default=False)
    email_service_updates = models.BooleanField(default=False)
    email_frequency = models.CharField(
        max_length=20,
        choices=[('instant', 'Instant'), ('daily', 'Daily'), ('weekly', 'Weekly')],
        default='daily'
    )
    subscribed_routes = models.JSONField(default=list)  # ['King Fahd Road', 'Prince Mohammed Bin Salman Road']
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
