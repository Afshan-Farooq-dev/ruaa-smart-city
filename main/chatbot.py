import os
import httpx
from groq import Groq
from django.conf import settings
from .data import TRAFFIC_DATA, WEATHER_DATA, SERVICES_DATA, EMERGENCY_NUMBERS

def get_groq_response(user_message):
    """
    Process user message and get response from Groq API
    """
    try:
        # Initialize Groq client
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            return "Error: Groq API key not configured."
        
        # Create an httpx.Client explicitly and pass it to Groq to avoid
        # incompatibilities where Groq attempts to pass `proxies=` to the
        # underlying Client (some httpx versions expect `proxy=`).
        http_client = httpx.Client()
        client = Groq(api_key=api_key, http_client=http_client)
        
        # Build context from our dummy data
        context = f"""
You are Ruaa, a helpful Smart City AI Assistant for Riyadh city. You have access to the following information:

TRAFFIC STATUS:
{format_traffic_data()}

WEATHER:
{format_weather_data()}

PUBLIC SERVICES:
{format_services_data()}

EMERGENCY NUMBERS:
{format_emergency_numbers()}

Provide helpful, friendly, and concise answers about the city. If asked about something not in your data, politely explain that you don't have that specific information but offer related help.
"""
        
        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_message}
            ],
            model=getattr(settings, 'GROQ_MODEL', 'llama-3.1-8b-instant'),
            temperature=0.7,
            max_tokens=500,
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

def format_traffic_data():
    result = []
    for road, info in TRAFFIC_DATA.items():
        result.append(f"- {road}: {info['status']}")
    return "\n".join(result)

def format_weather_data():
    return f"Temperature: {WEATHER_DATA['temperature']}°C, Condition: {WEATHER_DATA['condition']}, Humidity: {WEATHER_DATA['humidity']}%, Wind: {WEATHER_DATA['wind']} km/h"

def format_services_data():
    result = ["Hospitals:"]
    for h in SERVICES_DATA['hospitals']:
        result.append(f"- {h['name']}: {h['phone']}")
    result.append("\nParks:")
    for p in SERVICES_DATA['parks']:
        result.append(f"- {p['name']}: {p['location']}")
    return "\n".join(result)

def format_emergency_numbers():
    result = []
    for service, number in EMERGENCY_NUMBERS.items():
        result.append(f"- {service}: {number}")
    return "\n".join(result)