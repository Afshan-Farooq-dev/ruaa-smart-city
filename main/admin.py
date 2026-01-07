from django.contrib import admin
from .models import Review, UserProfile

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'attraction_name', 'rating', 'created', 'is_approved']
    list_filter = ['is_approved', 'rating', 'created']
    search_fields = ['user__username', 'attraction_name', 'text']
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_interests', 'get_favorites_count']
    
    def get_interests(self, obj):
        return ', '.join(obj.interests) if obj.interests else 'None'
    get_interests.short_description = 'Interests'
    
    def get_favorites_count(self, obj):
        return len(obj.favorites) if obj.favorites else 0
    get_favorites_count.short_description = 'Favorites'
