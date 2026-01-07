from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
import json
import requests
from .data import TRAFFIC_DATA, WEATHER_DATA, SERVICES_DATA, EMERGENCY_NUMBERS, TOURISM_DATA, TRANSPORTATION_DATA, EMBASSY_CONTACTS
from .chatbot import get_groq_response
from .forms import SimpleSignupForm
from .models import Review, UserProfile
from .email_utils import send_welcome_email

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SimpleSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile with default settings
            UserProfile.objects.get_or_create(user=user)
            # Send welcome email
            try:
                if user.email:
                    email_sent = send_welcome_email(user)
                    if email_sent:
                        print(f"✅ Welcome email sent to {user.email}")
                    else:
                        print(f"⚠️ Failed to send welcome email to {user.email}")
                else:
                    print("⚠️ User registered without email")
            except Exception as e:
                print(f"❌ Email error: {e}")
            login(request, user)
            return redirect('dashboard')
    else:
        form = SimpleSignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    context = {
        'user': request.user,
        'traffic_summary': len([v for v in TRAFFIC_DATA.values() if v['status'] == 'Clear']),
        'weather': WEATHER_DATA,
    }
    return render(request, 'dashboard.html', context)

@login_required
def traffic(request):
    context = {
        'traffic_data': TRAFFIC_DATA,
        'traffic_data_json': json.dumps(TRAFFIC_DATA)
    }
    return render(request, 'traffic.html', context)

@login_required
def weather(request):
    from django.conf import settings
    
    # Fetch weather for Riyadh (primary city)
    api_key = settings.OPENWEATHER_API_KEY
    weather_data = {}
    
    if api_key:
        try:
            # Riyadh coordinates
            lat, lon = 24.7136, 46.6753
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'temperature': round(data['main']['temp']),
                    'condition': data['weather'][0]['main'],
                    'humidity': data['main']['humidity'],
                    'wind': round(data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                    'forecast': [
                        {'day': 'Monday', 'temp': round(data['main']['temp']), 'condition': data['weather'][0]['main']},
                        {'day': 'Tuesday', 'temp': round(data['main']['temp']) - 1, 'condition': data['weather'][0]['main']},
                        {'day': 'Wednesday', 'temp': round(data['main']['temp']) + 1, 'condition': data['weather'][0]['main']},
                        {'day': 'Thursday', 'temp': round(data['main']['temp']), 'condition': data['weather'][0]['main']},
                        {'day': 'Friday', 'temp': round(data['main']['temp']) + 2, 'condition': data['weather'][0]['main']},
                    ]
                }
                print(f"✅ Live weather data loaded: {weather_data['temperature']}°C, {weather_data['condition']}")
            else:
                print(f"⚠️ Weather API error: {response.status_code}")
                weather_data = WEATHER_DATA
        except Exception as e:
            print(f"❌ Error fetching weather: {e}")
            weather_data = WEATHER_DATA
    else:
        print("⚠️ OPENWEATHER_API_KEY not configured, using static data")
        weather_data = WEATHER_DATA
    
    return render(request, 'weather.html', {'weather': weather_data})

@login_required
def services(request):
    context = {
        'services': SERVICES_DATA,
        'emergency': EMERGENCY_NUMBERS,
        'embassies': EMBASSY_CONTACTS,
    }
    return render(request, 'services.html', context)

@login_required
def tourism(request):
    # Get reviews aggregates for each attraction
    reviews_data = {}
    for attraction in TOURISM_DATA:
        reviews = Review.objects.filter(attraction_name=attraction['name'], is_approved=True)
        recent_reviews = []
        for r in reviews[:3]:
            recent_reviews.append({
                'user__username': r.user.username,
                'rating': r.rating,
                'text': r.text,
                'created': r.created.isoformat()
            })
        
        reviews_data[attraction['name']] = {
            'avg_rating': reviews.aggregate(Avg('rating'))['rating__avg'] or attraction.get('rating', 0),
            'count': reviews.count(),
            'recent': recent_reviews
        }
    
    import json
    context = {
        'attractions': TOURISM_DATA,
        'reviews_data': json.dumps(reviews_data),
    }
    return render(request, 'tourism.html', context)

@login_required
def transportation(request):
    context = {
        'transportation': TRANSPORTATION_DATA,
    }
    return render(request, 'transportation.html', context)

@login_required
def map_view(request):
    context = {
        'traffic_data': TRAFFIC_DATA,
        'traffic_data_json': json.dumps(TRAFFIC_DATA)
    }
    return render(request, 'map.html', context)

@login_required
@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)
            
            # Get response from Groq
            bot_response = get_groq_response(user_message)
            
            return JsonResponse({'response': bot_response})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# New API endpoints for enhanced features

@login_required
@csrf_exempt
def submit_review(request):
    """Submit a new review for an attraction"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            attraction_name = data.get('attraction_name')
            rating = int(data.get('rating', 0))
            text = data.get('text', '')
            
            if not attraction_name or rating < 1 or rating > 5:
                return JsonResponse({'error': 'Invalid data'}, status=400)
            
            review = Review.objects.create(
                user=request.user,
                attraction_name=attraction_name,
                rating=rating,
                text=text
            )
            
            return JsonResponse({
                'success': True,
                'review': {
                    'username': request.user.username,
                    'rating': review.rating,
                    'text': review.text,
                    'created': review.created.strftime('%Y-%m-%d %H:%M')
                }
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def get_weather_for_attraction(request, attraction_name):
    """Get real-time weather for attraction location"""
    try:
        # Find attraction coordinates
        attraction = next((a for a in TOURISM_DATA if a['name'] == attraction_name), None)
        if not attraction:
            return JsonResponse({'error': 'Attraction not found'}, status=404)
        
        # Use OpenWeatherMap API (free tier)
        # Note: User needs to add OPENWEATHER_API_KEY to .env
        import os
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('OPENWEATHER_API_KEY', '')
        if not api_key:
            # Fallback to mock data if no API key
            return JsonResponse({
                'temp': 28,
                'condition': 'Clear',
                'icon': '01d',
                'best_time': 'Morning (7-10 AM) or Evening (5-8 PM)',
                'crowd_level': 'Moderate'
            })
        
        lat = attraction.get('lat', 24.7136)
        lng = attraction.get('lng', 46.6753)
        
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            condition = data['weather'][0]['main']
            icon = data['weather'][0]['icon']
            
            # Simple heuristic for best visit time
            if temp > 35:
                best_time = 'Evening (6-9 PM) - cooler temperatures'
            elif temp < 15:
                best_time = 'Midday (12-3 PM) - warmer hours'
            else:
                best_time = 'Morning (8-11 AM) or Evening (5-7 PM)'
            
            return JsonResponse({
                'temp': round(temp),
                'condition': condition,
                'icon': icon,
                'best_time': best_time,
                'crowd_level': 'Low' if temp > 35 or temp < 15 else 'Moderate'
            })
        else:
            return JsonResponse({'error': 'Weather API error'}, status=500)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@csrf_exempt
def toggle_favorite(request):
    """Add or remove attraction from user favorites"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            attraction_name = data.get('attraction_name')
            
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            
            if attraction_name in profile.favorites:
                profile.favorites.remove(attraction_name)
                is_favorite = False
            else:
                profile.favorites.append(attraction_name)
                is_favorite = True
            
            profile.save()
            
            return JsonResponse({
                'success': True,
                'is_favorite': is_favorite,
                'favorites': profile.favorites
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def get_recommendations(request):
    """Get AI-powered personalized recommendations"""
    try:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        
        # Build context for AI
        context = f"User has visited: {', '.join(profile.visited) if profile.visited else 'none'}. "
        context += f"User favorites: {', '.join(profile.favorites) if profile.favorites else 'none'}. "
        context += f"User interests: {', '.join(profile.interests) if profile.interests else 'exploring'}. "
        
        # Get recommendations from Groq AI
        prompt = f"{context}Based on this, recommend 3 attractions from: {', '.join([a['name'] for a in TOURISM_DATA])}. Give only names, comma-separated."
        
        recommendations = get_groq_response(prompt)
        
        # Parse recommended attractions
        rec_names = [name.strip() for name in recommendations.split(',')[:3]]
        rec_attractions = [a for a in TOURISM_DATA if a['name'] in rec_names]
        
        return JsonResponse({
            'recommendations': rec_attractions,
            'reason': 'Based on your preferences and visit history'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def settings_view(request):
    """User notification settings page"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update email preferences
        profile.email_traffic_alerts = request.POST.get('email_traffic_alerts') == 'on'
        profile.email_weather_alerts = request.POST.get('email_weather_alerts') == 'on'
        profile.email_tourism_digest = request.POST.get('email_tourism_digest') == 'on'
        profile.email_service_updates = request.POST.get('email_service_updates') == 'on'
        profile.email_frequency = request.POST.get('email_frequency', 'daily')
        
        # Update subscribed routes
        subscribed_routes = request.POST.getlist('subscribed_routes')
        profile.subscribed_routes = subscribed_routes
        
        profile.save()
        
        # Send confirmation email
        from .email_utils import send_settings_confirmation_email
        try:
            if request.user.email:
                send_settings_confirmation_email(request.user, profile)
        except Exception as e:
            print(f"Error sending settings confirmation: {e}")
        
        return JsonResponse({'success': True, 'message': 'Settings updated successfully!'})
    
    # Get all available routes from TRAFFIC_DATA
    all_routes = []
    for city, city_data in TRAFFIC_DATA.items():
        if 'sub_areas' in city_data:
            for area in city_data['sub_areas']:
                all_routes.append({
                    'name': area.get('name', ''),
                    'city': city
                })
    
    context = {
        'profile': profile,
        'all_routes': all_routes,
    }
    return render(request, 'settings.html', context)


@login_required
@csrf_exempt
def subscribe_route(request):
    """Subscribe/unsubscribe to traffic alerts for a route"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            route_name = data.get('route_name')
            action = data.get('action')  # 'subscribe' or 'unsubscribe'
            
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            
            if action == 'subscribe':
                if route_name not in profile.subscribed_routes:
                    profile.subscribed_routes.append(route_name)
                    message = f'Subscribed to {route_name} alerts!'
                    
                    # Send immediate confirmation email with current traffic status
                    from .email_utils import send_subscription_confirmation_email
                    try:
                        if request.user.email:
                            # Get route data
                            route_data = None
                            for area, info in TRAFFIC_DATA.items():
                                if area == route_name:
                                    route_data = {
                                        'name': area,
                                        'status': info.get('status', 'Unknown'),
                                        'city': info.get('city', 'N/A'),
                                        'area': info.get('area_ar', 'N/A'),
                                        'description': info.get('description', ''),
                                    }
                                    break
                            
                            if route_data:
                                send_subscription_confirmation_email(request.user, route_data)
                    except Exception as e:
                        print(f"Error sending subscription email: {e}")
            else:
                if route_name in profile.subscribed_routes:
                    profile.subscribed_routes.remove(route_name)
                    message = f'Unsubscribed from {route_name} alerts.'
            
            profile.save()
            
            return JsonResponse({
                'success': True,
                'message': message,
                'subscribed': route_name in profile.subscribed_routes
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)