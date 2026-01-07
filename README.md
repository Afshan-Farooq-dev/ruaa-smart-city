# Ruaa Smart City

A professional Django-based smart city management system with AI chatbot, traffic monitoring, weather forecasts, and interactive maps.

## Quick Start

For detailed installation instructions, see **INSTALLATION_GUIDE.txt**

### Basic Steps:
1. Install Python 3.10+
2. Extract project files
3. Run: `pip install -r requirements.txt`
4. Run: `python manage.py migrate`
5. Run: `python manage.py runserver`
6. Open: http://127.0.0.1:8000/

## Features

- **AI Chatbot**: Smart assistant powered by Groq API (llama-3.1-8b-instant)
- **Traffic Monitor**: Real-time traffic status for major roads
- **Weather Forecast**: 3-day weather predictions
- **Public Services**: Hospitals and emergency contacts directory
- **Interactive Map**: Leaflet.js powered city map with markers
- **User Authentication**: Secure login/signup system
- **Responsive Design**: Professional UI with modern styling

## Technology Stack

- Django 5.1.14
- Python 3.10+
- Groq AI API
- Leaflet.js
- Bootstrap 5
- Font Awesome 6
- SQLite Database

## Project Structure

```
ruaa_smart_city/
├── main/                   # Main application
│   ├── templates/          # HTML templates
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   ├── data.py             # Static data
│   ├── chatbot.py          # Groq AI integration
│   └── forms.py            # Custom forms
├── ruaa/                   # Project settings
│   ├── settings.py         # Configuration
│   └── urls.py             # Main URL config
├── static/                 # Static files
│   ├── css/style.css       # Custom styles
│   └── js/app.js           # JavaScript
├── .env                    # Environment variables
├── requirements.txt        # Dependencies
├── manage.py               # Django management
└── INSTALLATION_GUIDE.txt  # Setup instructions
```

## Configuration

The `.env` file contains:
- `GROQ_API_KEY`: Your Groq API key
- `GROQ_MODEL`: AI model (llama-3.1-8b-instant)

## User Accounts

### Regular Users:
- Signup at: http://127.0.0.1:8000/signup/
- Simple password requirements (easy registration)

### Admin Access:
- Create superuser: `python manage.py createsuperuser`
- Access at: http://127.0.0.1:8000/admin/

## Main Pages

| Page | URL | Description |
|------|-----|-------------|
| Dashboard | `/dashboard/` | AI chatbot interface |
| Traffic | `/traffic/` | Live traffic status |
| Weather | `/weather/` | Weather forecasts |
| Services | `/services/` | Public facilities |
| Map | `/map/` | Interactive city map |

## Requirements

- Python 3.10 or higher
- Internet connection (for map tiles and AI API)
- Modern web browser
- 2 GB RAM minimum

## Support

For questions or issues, contact the project administrator.

---

**Version**: 1.0.0  
**License**: MIT  
**Developed**: 2025
