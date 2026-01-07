TRAFFIC_DATA = {
    # Riyadh (الرياض) - Blue #3B82F6
    'Al Olaya': {
        'city': 'Riyadh',
        'city_ar': 'الرياض',
        'area_ar': 'العليا',
        'city_color': '#3B82F6',
        'status': 'Clear',
        'color': 'success',
        'traffic_color': '#10B981',
        'description': 'Free flowing traffic in Al Olaya business district. Smooth journey ahead with minimal delays.',
        'lat': 24.7500,
        'lng': 46.6667
    },
    'King Fahd District': {
        'city': 'Riyadh',
        'city_ar': 'الرياض',
        'area_ar': 'حي الملك فهد',
        'city_color': '#3B82F6',
        'status': 'Moderate',
        'color': 'warning',
        'traffic_color': '#FBBF24',
        'description': 'Moderate traffic congestion in King Fahd District. Expected delays 10-15 minutes during peak hours.',
        'lat': 24.6800,
        'lng': 46.7200
    },
    'Diriyah': {
        'city': 'Riyadh',
        'city_ar': 'الرياض',
        'area_ar': 'الدرعية',
        'city_color': '#3B82F6',
        'status': 'Clear',
        'color': 'success',
        'traffic_color': '#10B981',
        'description': 'Light traffic in historic Diriyah area. No significant delays expected on main routes.',
        'lat': 24.7350,
        'lng': 46.5750
    },
    
    # Jeddah (جدة) - Red #EF4444
    'Al Balad': {
        'city': 'Jeddah',
        'city_ar': 'جدة',
        'area_ar': 'البلد',
        'city_color': '#EF4444',
        'status': 'Heavy',
        'color': 'danger',
        'traffic_color': '#F97316',
        'description': 'Heavy congestion in historic Al Balad district. Narrow streets causing delays. Seek alternative routes.',
        'lat': 21.4858,
        'lng': 39.1925
    },
    'Corniche Jeddah': {
        'city': 'Jeddah',
        'city_ar': 'جدة',
        'area_ar': 'كورنيش جدة',
        'city_color': '#EF4444',
        'status': 'Clear',
        'color': 'success',
        'traffic_color': '#10B981',
        'description': 'Clear traffic along scenic Jeddah Waterfront. Perfect conditions for coastal drive with light traffic.',
        'lat': 21.6000,
        'lng': 39.1000
    },
    'Al Salamah': {
        'city': 'Jeddah',
        'city_ar': 'جدة',
        'area_ar': 'السلامة',
        'city_color': '#EF4444',
        'status': 'Moderate',
        'color': 'warning',
        'traffic_color': '#FBBF24',
        'description': 'Moderate traffic in Al Salamah residential area. Some congestion at intersections during rush hours.',
        'lat': 21.5000,
        'lng': 39.2500
    },
    
    # Makkah (مكة المكرمة) - Brown #92400E
    'Al Haram Area': {
        'city': 'Makkah',
        'city_ar': 'مكة المكرمة',
        'area_ar': 'الحرم',
        'city_color': '#92400E',
        'status': 'Heavy',
        'color': 'danger',
        'traffic_color': '#F97316',
        'description': 'Heavy traffic near Holy Mosque area. High pedestrian and vehicle congestion. Plan extra travel time.',
        'lat': 21.4225,
        'lng': 39.8262
    },
    'Aziziyah': {
        'city': 'Makkah',
        'city_ar': 'مكة المكرمة',
        'area_ar': 'العزيزية',
        'city_color': '#92400E',
        'status': 'Moderate',
        'color': 'warning',
        'traffic_color': '#FBBF24',
        'description': 'Moderate congestion in Aziziyah district. Main roads experiencing steady traffic flow with minor delays.',
        'lat': 21.3800,
        'lng': 39.8800
    },
    'Misfalah': {
        'city': 'Makkah',
        'city_ar': 'مكة المكرمة',
        'area_ar': 'المسفلة',
        'city_color': '#92400E',
        'status': 'Clear',
        'color': 'success',
        'traffic_color': '#10B981',
        'description': 'Clear traffic in Misfalah residential area. Roads are free flowing with minimal congestion.',
        'lat': 21.4600,
        'lng': 39.7700
    },
    
    # Madinah (المدينة المنورة) - Green #10B981
    'Central Area Madinah': {
        'city': 'Madinah',
        'city_ar': 'المدينة المنورة',
        'area_ar': 'المنطقة المركزية',
        'city_color': '#10B981',
        'status': 'Heavy',
        'color': 'danger',
        'traffic_color': '#F97316',
        'description': 'Heavy traffic in Central Area near Prophet\'s Mosque. High volume of visitors causing significant delays.',
        'lat': 24.4672,
        'lng': 39.6108
    },
    'Quba': {
        'city': 'Madinah',
        'city_ar': 'المدينة المنورة',
        'area_ar': 'قباء',
        'city_color': '#10B981',
        'status': 'Moderate',
        'color': 'warning',
        'traffic_color': '#FBBF24',
        'description': 'Moderate traffic on Quba road. Steady flow with occasional slowdowns near Quba Mosque area.',
        'lat': 24.4000,
        'lng': 39.6500
    },
    'Uhud': {
        'city': 'Madinah',
        'city_ar': 'المدينة المنورة',
        'area_ar': 'أحد',
        'city_color': '#10B981',
        'status': 'Clear',
        'color': 'success',
        'traffic_color': '#10B981',
        'description': 'Clear roads to Mount Uhud area. Light traffic with excellent travel conditions on northern routes.',
        'lat': 24.5200,
        'lng': 39.5400
    },
    
    # Dammam (الدمام) - Yellow #FBBF24
    'Al Faisaliah': {
        'city': 'Dammam',
        'city_ar': 'الدمام',
        'area_ar': 'الفيصلية',
        'city_color': '#FBBF24',
        'status': 'Moderate',
        'color': 'warning',
        'traffic_color': '#FBBF24',
        'description': 'Moderate traffic in Al Faisaliah commercial district. Some congestion during business hours.',
        'lat': 26.3700,
        'lng': 50.1500
    },
    'Corniche Dammam': {
        'city': 'Dammam',
        'city_ar': 'الدمام',
        'area_ar': 'كورنيش الدمام',
        'city_color': '#FBBF24',
        'status': 'Clear',
        'color': 'success',
        'traffic_color': '#10B981',
        'description': 'Clear traffic along Dammam Corniche waterfront. Smooth coastal road with beautiful Gulf views.',
        'lat': 26.4700,
        'lng': 50.1200
    },
    'Al Rakah': {
        'city': 'Dammam',
        'city_ar': 'الدمام',
        'area_ar': 'الراكه',
        'city_color': '#FBBF24',
        'status': 'Clear',
        'color': 'success',
        'traffic_color': '#10B981',
        'description': 'Clear traffic in Al Rakah residential area. Free flowing roads with minimal delays expected.',
        'lat': 26.4500,
        'lng': 50.2800
    },
}

WEATHER_DATA = {
    'temperature': 27,
    'condition': 'Sunny',
    'humidity': 35,
    'wind': 11,
    'forecast': [
        {'day': 'Monday', 'temp': 28, 'condition': 'Sunny'},
        {'day': 'Tuesday', 'temp': 26, 'condition': 'Partly Cloudy'},
        {'day': 'Wednesday', 'temp': 29, 'condition': 'Sunny'},
        {'day': 'Thursday', 'temp': 27, 'condition': 'Sunny'},
        {'day': 'Friday', 'temp': 30, 'condition': 'Clear'},
    ]
}

SERVICES_DATA = {
    'hospitals': [
        {
            'name': 'King Fahd Medical City',
            'location': 'Al Maathar District',
            'phone': '011-288-9999',
            'lat': 24.7136,
            'lng': 46.7253,
            'specialties': '24/7 Emergency, Surgery, Cardiology'
        },
        {
            'name': 'King Faisal Specialist Hospital',
            'location': 'Al Maathar',
            'phone': '011-464-7272',
            'lat': 24.6901,
            'lng': 46.6947,
            'specialties': 'Oncology, Transplant, Research'
        },
        {
            'name': 'Riyadh Care Hospital',
            'location': 'Olaya District',
            'phone': '011-419-0000',
            'lat': 24.7136,
            'lng': 46.6753,
            'specialties': 'General Medicine, Pediatrics'
        },
        {
            'name': 'National Guard Hospital',
            'location': 'King Abdulaziz Road',
            'phone': '011-252-0088',
            'lat': 24.7539,
            'lng': 46.7286,
            'specialties': 'Emergency Care, ICU'
        },
    ],
    'parks': [
        {'name': 'King Abdullah Park', 'location': 'Malaz District', 'facilities': 'Playground, Walking Trails'},
        {'name': 'Salam Park', 'location': 'Al Malqa', 'facilities': 'Lake, Picnic Areas'},
        {'name': 'Al Nahda Park', 'location': 'Nahda District', 'facilities': 'Sports Courts, Gardens'},
    ],
}

TOURISM_DATA = [
    {
        'name': 'Kingdom Centre Tower',
        'description': 'Iconic 302m skyscraper with sky bridge observatory offering panoramic city views and luxury shopping.',
        'category': 'Landmark',
        'image': '/static/kingdom_center_tower.png',
        'virtual_tour': '',
        'rating': 4.8,
        'reviews_count': 523,
        'gallery': [
            '/static/kingdom_center_tower.png',
            'https://images.unsplash.com/photo-1549880338-65ddcdfd017b?w=1200',
            'https://images.unsplash.com/photo-1509395176047-4a66953fd231?w=1200'
        ],
        'video': '',
        'hours': '09:00 - 22:00 (Sky Bridge varies)',
        'price': 'Observation deck fee applies',
        'tips': 'Buy tickets in advance; best at sunset for photos.',
        'facts': ['Best sunset view', 'Popular shopping destination'],
        'lat': 24.7114,
        'lng': 46.6753
    },
    {
        'name': 'Al Masmak Fortress',
        'description': 'Historic clay and mud-brick fort, crucial to the establishment of modern Saudi Arabia.',
        'category': 'Historical',
        'image': 'https://images.unsplash.com/photo-1580837119756-563d608dd119?w=800',
        'virtual_tour': '',
        'rating': 4.6,
        'reviews_count': 289,
        'gallery': [
            'https://images.unsplash.com/photo-1580837119756-563d608dd119?w=1200',
            'https://images.unsplash.com/photo-1546488638-7f1b2f6f3d8b?w=1200'
        ],
        'video': '',
        'hours': '08:00 - 16:00',
        'price': 'Free',
        'tips': 'Wear comfortable shoes; guided tours available.',
        'facts': ['Historic fortress', 'Interactive displays'],
        'lat': 24.6308,
        'lng': 46.7135
    },
    {
        'name': 'Diriyah Historic District',
        'description': 'UNESCO World Heritage site, birthplace of the Saudi state with restored mud-brick buildings.',
        'category': 'UNESCO Site',
        'image': 'https://images.unsplash.com/photo-1512632578888-169bbbc64f33?w=800',
        'virtual_tour': '',
        'rating': 4.9,
        'reviews_count': 417,
        'gallery': [
            'https://images.unsplash.com/photo-1512632578888-169bbbc64f33?w=1200',
            'https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=1200'
        ],
        'video': '',
        'hours': 'Open area - daytime recommended',
        'price': 'Varies by exhibit',
        'tips': 'Morning visits avoid heat; plenty of photo spots.',
        'facts': ['UNESCO site', 'Cultural events held regularly'],
        'lat': 24.7333,
        'lng': 46.5667
    },
    {
        'name': 'National Museum',
        'description': 'Eight halls showcasing Saudi history from prehistoric times to the modern Kingdom.',
        'category': 'Museum',
        'image': '/static/nationa_museum.png',
        'gallery': [
            '/static/nationa_museum.png',
            'https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=1200'
        ],
        'virtual_tour': 'https://www.google.com/maps/@24.6478,46.7103,3a,75y,90t/data=!3m6!1e1!3m4!1s-placeholder',
        'rating': 4.7,
        'reviews_count': 342,
        'video': '',
        'hours': '09:00 - 18:00',
        'price': 'Ticketed exhibitions may apply',
        'tips': 'Allocate 2-3 hours for a full visit.',
        'facts': ['Major historical collection', 'Great for families'],
        'lat': 24.6478,
        'lng': 46.7103
    },
    {
        'name': 'Wadi Hanifah',
        'description': '120km valley oasis with walking trails, picnic areas, and natural beauty.',
        'category': 'Nature',
        'image': '/static/images/Wadi Hanifa.jpeg',
        'virtual_tour': '',
        'rating': 4.5,
        'reviews_count': 198,
        'gallery': [
            '/static/images/Wadi Hanifa.jpeg',
            'https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=1200'
        ],
        'video': '',
        'hours': 'Open 24 hours',
        'price': 'Free',
        'tips': 'Bring water and sun protection for long walks.',
        'facts': ['Scenic valley', 'Popular with locals'],
        'lat': 24.6194,
        'lng': 46.6175
    },
    {
        'name': 'Boulevard Riyadh City',
        'description': 'Modern entertainment destination with dining, shopping, and cultural experiences.',
        'category': 'Entertainment',
        'image': '/static/images/boulevard riyadh city.jpeg',
        'virtual_tour': '',
        'rating': 4.7,
        'reviews_count': 651,
        'gallery': [
            '/static/images/boulevard riyadh city.jpeg',
            'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200'
        ],
        'video': '',
        'hours': 'Evenings best for entertainment',
        'price': 'Varies',
        'tips': 'Great for dining and night activities.',
        'facts': ['Modern entertainment hub', 'Nightlife and shows'],
        'lat': 24.7900,
        'lng': 46.6294
    },
    {
        'name': 'Al-Ula (Hegra / Madain Saleh)',
        'description': "Saudi Arabia's first UNESCO World Heritage Site featuring ancient Nabataean tombs and rock formations.",
        'category': 'UNESCO Site',
        'image': '/static/images/Al-Ula.png',
        'virtual_tour': '',
        'rating': 4.9,
        'reviews_count': 834,
        'gallery': [
            '/static/images/Al-Ula.png',
            'https://images.unsplash.com/photo-1578070181910-f1e514afdd08?w=1200',
            'https://images.unsplash.com/photo-1591608971362-f08b2a75731a?w=1200'
        ],
        'video': '',
        'hours': '08:00 - 20:00 (seasonal variations)',
        'price': 'Entry ticket required - booking recommended',
        'tips': 'Book guided tours in advance; bring sun protection and water.',
        'facts': ['Ancient Nabataean city', '111 monumental tombs', 'Archaeological wonder'],
        'lat': 26.6084,
        'lng': 37.9206
    },
    {
        'name': 'Edge of the World (Jebel Fihrayn)',
        'description': 'Dramatic cliff escarpment offering breathtaking panoramic views of the surrounding plains.',
        'category': 'Nature',
        'image': '/static/images/Edge of the World.png',
        'virtual_tour': '',
        'rating': 4.8,
        'reviews_count': 567,
        'gallery': [
            '/static/images/Edge of the World.png',
            'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1200',
            'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200'
        ],
        'video': '',
        'hours': 'Best visited during sunrise or sunset',
        'price': 'Free (4WD vehicle recommended)',
        'tips': 'Hire a guide or join a tour; terrain is rough and requires off-road vehicle.',
        'facts': ['Part of Tuwaiq escarpment', 'Spectacular sunset views', 'Adventure destination'],
        'lat': 25.0881,
        'lng': 45.9469
    },
    {
        'name': 'Diriyah - At-Turaif District',
        'description': 'UNESCO World Heritage Site and the original home of the Saudi royal family with preserved mud-brick architecture.',
        'category': 'UNESCO Site',
        'image': '/static/images/Diriyah - At-Turaif.png',
        'virtual_tour': '',
        'rating': 4.9,
        'reviews_count': 612,
        'gallery': [
            '/static/images/Diriyah - At-Turaif.png',
            'https://images.unsplash.com/photo-1512632578888-169bbbc64f33?w=1200',
            'https://images.unsplash.com/photo-1591370874773-6702e8f12fd8?w=1200'
        ],
        'video': '',
        'hours': '09:00 - 21:00',
        'price': 'Entry ticket required',
        'tips': 'Wear comfortable walking shoes; evening visits offer cooler temperatures and beautiful lighting.',
        'facts': ['Birthplace of first Saudi state', 'Traditional Najdi architecture', 'Cultural heritage site'],
        'lat': 24.7333,
        'lng': 46.5667
    },
    {
        'name': 'Al-Bujairi Heritage Park',
        'description': 'Cultural heritage park featuring traditional Najdi architecture, museums, and authentic Saudi dining experiences.',
        'category': 'Heritage',
        'image': '/static/images/Al-Bujairi Heritage Park.png',
        'virtual_tour': '',
        'rating': 4.6,
        'reviews_count': 423,
        'gallery': [
            '/static/images/Al-Bujairi Heritage Park.png',
            'https://images.unsplash.com/photo-1512632578888-169bbbc64f33?w=1200',
            'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1200'
        ],
        'video': '',
        'hours': '09:00 - 22:00',
        'price': 'Free entry (dining and activities priced separately)',
        'tips': 'Visit in the evening for beautiful illumination; try traditional Saudi cuisine at the restaurants.',
        'facts': ['Part of Diriyah Gate project', 'Traditional mud-brick buildings', 'Cultural events and exhibitions'],
        'lat': 24.7326,
        'lng': 46.5691
    },
    {
        'name': 'King Abdulaziz Memorial Hall & Al Murabba Palace',
        'description': "Historic palace complex showcasing the life and achievements of Saudi Arabia's founder, King Abdulaziz.",
        'category': 'Museum',
        'image': '/static/images/King Abdulaziz.png',
        'virtual_tour': '',
        'rating': 4.5,
        'reviews_count': 287,
        'gallery': [
            '/static/images/King Abdulaziz.png',
            'https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=1200',
            'https://images.unsplash.com/photo-1512632578888-169bbbc64f33?w=1200'
        ],
        'video': '',
        'hours': '08:00 - 20:00 (Closed Tuesdays)',
        'price': 'Free admission',
        'tips': 'Allow 1-2 hours for exploration; photography permitted in most areas.',
        'facts': ['Built in 1938', 'Historical royal residence', 'Rich collection of artifacts'],
        'lat': 24.6534,
        'lng': 46.7089
    },
    {
        'name': 'Riyadh Zoo',
        'description': 'Largest zoo in Saudi Arabia home to over 1,500 animals from around the world in naturalistic habitats.',
        'category': 'Entertainment',
        'image': '/static/images/Riyadh Zoo.png',
        'virtual_tour': '',
        'rating': 4.3,
        'reviews_count': 756,
        'gallery': [
            '/static/images/Riyadh Zoo.png',
            'https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=1200',
            'https://images.unsplash.com/photo-1535338623351-67762daa75e4?w=1200'
        ],
        'video': '',
        'hours': '08:30 - 17:30 (Closed Tuesdays)',
        'price': '10 SAR adults, 5 SAR children',
        'tips': 'Visit early morning to see animals most active; bring water and wear comfortable shoes.',
        'facts': ['Opened in 1987', '55 acres of exhibits', 'Conservation and education programs'],
        'lat': 24.7517,
        'lng': 46.6417
    },
    {
        'name': 'Saudi Aviation Museum (Saqr Al-Jazira)',
        'description': 'Aviation museum showcasing the history of Saudi Arabian aviation with historic aircraft and interactive exhibits.',
        'category': 'Museum',
        'image': '/static/images/Saudi Aviation Museum (Saqr Al-Jazira).png',
        'virtual_tour': '',
        'rating': 4.7,
        'reviews_count': 389,
        'gallery': [
            '/static/images/Saudi Aviation Museum (Saqr Al-Jazira).png',
            'https://images.unsplash.com/photo-1540962351504-03099e0a754b?w=1200',
            'https://images.unsplash.com/photo-1583523292466-f61ef49cd414?w=1200'
        ],
        'video': '',
        'hours': '09:00 - 21:00 (Closed Mondays)',
        'price': '25 SAR general admission',
        'tips': 'Great for aviation enthusiasts and families; interactive flight simulators available.',
        'facts': ['Royal Saudi Air Force heritage', 'Vintage aircraft collection', 'Modern interactive displays'],
        'lat': 24.7240,
        'lng': 46.7250
    },
]

TRANSPORTATION_DATA = {
    'metro': [
        {
            'line': 'Blue Line',
            'stations': 12,
            'route': 'Olaya - King Abdullah Financial District',
            'frequency': 'Every 5 minutes',
            'operating_hours': '06:00 - 00:00'
        },
        {
            'line': 'Red Line',
            'stations': 18,
            'route': 'King Khalid Airport - King Abdulaziz Historical Center',
            'frequency': 'Every 6 minutes',
            'operating_hours': '06:00 - 00:00'
        },
        {
            'line': 'Green Line',
            'stations': 11,
            'route': 'Al Yasmin - Diplomatic Quarter',
            'frequency': 'Every 7 minutes',
            'operating_hours': '06:00 - 00:00'
        },
    ],
    'buses': [
        {
            'route': 'Route 101',
            'path': 'City Center - University',
            'frequency': 'Every 15 minutes',
            'fare': '4 SAR'
        },
        {
            'route': 'Route 202',
            'path': 'Airport - Downtown',
            'frequency': 'Every 20 minutes',
            'fare': '6 SAR'
        },
        {
            'route': 'Route 303',
            'path': 'Olaya - Diplomatic Quarter',
            'frequency': 'Every 12 minutes',
            'fare': '4 SAR'
        },
    ]
}

EMERGENCY_NUMBERS = {
    'Police': '911',
    'Ambulance': '997',
    'Fire Department': '998',
    'Civil Defense': '998',
    'Traffic Accidents': '993',
    'Red Crescent': '997',
}

# Embassy contacts in Riyadh with country codes
EMBASSY_CONTACTS = [
    {
        'country': 'United States',
        'country_ar': 'الولايات المتحدة',
        'phone': '+966 11 488 3800',
        'flag': '🇺🇸',
        'flag_code': 'US'
    },
    {
        'country': 'United Kingdom',
        'country_ar': 'المملكة المتحدة',
        'phone': '+966 11 481 9100',
        'flag': '🇬🇧',
        'flag_code': 'GB'
    },
    {
        'country': 'United Arab Emirates',
        'country_ar': 'الإمارات العربية المتحدة',
        'phone': '+966 11 482 7272',
        'flag': '🇦🇪',
        'flag_code': 'AE'
    },
    {
        'country': 'Egypt',
        'country_ar': 'مصر',
        'phone': '+966 11 493 1600',
        'flag': '🇪🇬',
        'flag_code': 'EG'
    },
    {
        'country': 'India',
        'country_ar': 'الهند',
        'phone': '+966 11 488 4144',
        'flag': '🇮🇳',
        'flag_code': 'IN'
    },
    {
        'country': 'Pakistan',
        'country_ar': 'باكستان',
        'phone': '+966 11 488 7272',
        'flag': '🇵🇰',
        'flag_code': 'PK'
    },
    {
        'country': 'Philippines',
        'country_ar': 'الفلبين',
        'phone': '+966 11 482 3559',
        'flag': '🇵🇭',
        'flag_code': 'PH'
    },
    {
        'country': 'Canada',
        'country_ar': 'كندا',
        'phone': '+966 11 488 2288',
        'flag': '🇨🇦',
        'flag_code': 'CA'
    },
    {
        'country': 'France',
        'country_ar': 'فرنسا',
        'phone': '+966 11 434 4100',
        'flag': '🇫🇷',
        'flag_code': 'FR'
    },
    {
        'country': 'Germany',
        'country_ar': 'ألمانيا',
        'phone': '+966 11 483 1131',
        'flag': '🇩🇪',
        'flag_code': 'DE'
    },
]