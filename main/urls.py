from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('traffic/', views.traffic, name='traffic'),
    path('weather/', views.weather, name='weather'),
    path('services/', views.services, name='services'),
    path('tourism/', views.tourism, name='tourism'),
    path('transportation/', views.transportation, name='transportation'),
    path('map/', views.map_view, name='map'),
    path('chatbot/', views.chatbot_response, name='chatbot'),
    path('settings/', views.settings_view, name='settings'),
    # New API endpoints
    path('api/submit-review/', views.submit_review, name='submit_review'),
    path('api/weather/<str:attraction_name>/', views.get_weather_for_attraction, name='get_weather'),
    path('api/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('api/recommendations/', views.get_recommendations, name='get_recommendations'),
    path('api/subscribe-route/', views.subscribe_route, name='subscribe_route'),
]