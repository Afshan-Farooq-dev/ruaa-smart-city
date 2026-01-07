"""
Test weather API connection
Run: python test_weather.py
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')

print("=" * 60)
print("WEATHER API TEST")
print("=" * 60)
print(f"API Key configured: {'Yes' if API_KEY else 'No'}")
print(f"API Key: {API_KEY[:10]}..." if API_KEY else "API Key: NOT SET")
print("=" * 60)

if not API_KEY:
    print("\n❌ OPENWEATHER_API_KEY not set in .env file")
    print("Get your free API key at: https://openweathermap.org/api")
    exit(1)

# Test with Riyadh
city = "Riyadh"
lat, lon = 24.7136, 46.6753

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

print(f"\nTesting weather API for {city}...")
print(f"URL: {url[:80]}...")

try:
    response = requests.get(url, timeout=10)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ SUCCESS! Live weather data retrieved:")
        print(f"  City: {data['name']}")
        print(f"  Temperature: {data['main']['temp']}°C")
        print(f"  Feels Like: {data['main']['feels_like']}°C")
        print(f"  Condition: {data['weather'][0]['main']} - {data['weather'][0]['description']}")
        print(f"  Humidity: {data['main']['humidity']}%")
        print(f"  Wind Speed: {data['wind']['speed']} m/s")
        print(f"  Pressure: {data['main']['pressure']} hPa")
    elif response.status_code == 401:
        print("\n❌ ERROR: Invalid API Key")
        print("   Check your OPENWEATHER_API_KEY in .env file")
        print("   Make sure the API key is activated (can take a few minutes)")
    else:
        print(f"\n❌ ERROR: {response.status_code}")
        print(f"   Response: {response.text}")
        
except Exception as e:
    print(f"\n❌ Exception: {e}")
