// AI Recommendations System for Ruaa Smart City

// Create AI recommendation button and modal HTML
function initAIRecommendations() {
    // Create AI button
    const aiButton = document.createElement('button');
    aiButton.className = 'ai-recommend-btn';
    aiButton.innerHTML = '<i class="fas fa-robot"></i>';
    aiButton.title = 'Get AI Recommendations';
    aiButton.onclick = openAIModal;
    document.body.appendChild(aiButton);

    // Create AI modal
    const aiModal = document.createElement('div');
    aiModal.className = 'ai-modal';
    aiModal.id = 'aiModal';
    aiModal.innerHTML = `
        <div class="ai-modal-content">
            <div class="ai-modal-header">
                <h3>
                    <i class="fas fa-brain"></i>
                    AI Smart Recommendations
                </h3>
                <button class="ai-modal-close" onclick="closeAIModal()">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="ai-modal-body" id="aiModalBody">
                <div class="ai-loading">
                    <div class="ai-loading-spinner"></div>
                    <div class="ai-loading-text">Analyzing your needs...</div>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(aiModal);

    // Close modal when clicking outside
    aiModal.addEventListener('click', function(e) {
        if (e.target === aiModal) {
            closeAIModal();
        }
    });
}

// Open AI Modal
function openAIModal() {
    const modal = document.getElementById('aiModal');
    modal.classList.add('active');
    
    // Get recommendations based on current page
    const pageName = getPageName();
    fetchAIRecommendations(pageName);
}

// Close AI Modal
function closeAIModal() {
    const modal = document.getElementById('aiModal');
    modal.classList.remove('active');
}

// Get current page name
function getPageName() {
    const path = window.location.pathname;
    if (path.includes('traffic')) return 'traffic';
    if (path.includes('weather')) return 'weather';
    if (path.includes('services')) return 'healthcare';
    if (path.includes('tourism')) return 'tourism';
    if (path.includes('transportation')) return 'transportation';
    if (path.includes('map')) return 'map';
    return 'dashboard';
}

// Fetch AI Recommendations
async function fetchAIRecommendations(pageName) {
    const modalBody = document.getElementById('aiModalBody');
    
    // Show loading
    modalBody.innerHTML = `
        <div class="ai-loading">
            <div class="ai-loading-spinner"></div>
            <div class="ai-loading-text">Generating smart recommendations...</div>
        </div>
    `;

    // Simulate AI processing (in real app, call API)
    setTimeout(() => {
        const recommendations = getRecommendationsForPage(pageName);
        displayRecommendations(recommendations);
    }, 1500);
}

// Get recommendations based on page
function getRecommendationsForPage(pageName) {
    const recommendations = {
        dashboard: [
            {
                icon: 'fa-lightbulb',
                title: 'Start Your Day Right',
                text: 'Check weather conditions and traffic status before heading out. Currently 27°C with clear skies - perfect for outdoor activities!'
            },
            {
                icon: 'fa-hospital',
                title: 'Health First',
                text: 'King Fahd Medical City offers 24/7 emergency services. Save their contact: 011-288-9999 for quick access.'
            },
            {
                icon: 'fa-route',
                title: 'Smart Commute',
                text: 'King Fahd Road has moderate traffic. Consider taking Olaya Street for faster travel. Metro Blue Line runs every 5 minutes.'
            },
            {
                icon: 'fa-star',
                title: 'Weekend Plans',
                text: 'Visit Diriyah UNESCO site this weekend. Best time: 4 PM - 7 PM for cooler weather and stunning sunset views.'
            }
        ],
        traffic: [
            {
                icon: 'fa-route',
                title: 'Avoid Corniche Road',
                text: 'Heavy congestion detected on Corniche Road. Alternative route: Use King Fahd Road then merge to Olaya Street to save 15-20 minutes.'
            },
            {
                icon: 'fa-clock',
                title: 'Best Travel Times',
                text: 'Peak hours are 7-9 AM and 4-7 PM. For smooth travel, plan your trips between 10 AM - 3 PM or after 8 PM.'
            },
            {
                icon: 'fa-subway',
                title: 'Try Metro Instead',
                text: 'Riyadh Metro Blue Line covers major business districts. Trains every 5 minutes - faster than driving during rush hour!'
            },
            {
                icon: 'fa-mobile-alt',
                title: 'Real-Time Updates',
                text: 'Enable notifications for live traffic alerts. We\'ll notify you of accidents, road closures, and optimal departure times.'
            }
        ],
        weather: [
            {
                icon: 'fa-sun',
                title: 'Perfect Outdoor Weather',
                text: '27°C with clear skies is ideal for sightseeing. Visit outdoor attractions like Wadi Hanifah or King Abdullah Park.'
            },
            {
                icon: 'fa-tint',
                title: 'Stay Hydrated',
                text: 'Low humidity at 35% but warm temperatures. Carry water bottle and apply sunscreen if spending time outdoors.'
            },
            {
                icon: 'fa-calendar-alt',
                title: 'Week Ahead',
                text: 'Temperatures will rise to 30°C by Friday. Plan indoor activities for hot days - visit museums or shopping malls.'
            },
            {
                icon: 'fa-running',
                title: 'Best Exercise Time',
                text: 'Early morning (6-8 AM) or evening (6-8 PM) are optimal for outdoor exercise. Temperature will be 20-24°C.'
            }
        ],
        healthcare: [
            {
                icon: 'fa-ambulance',
                title: 'Emergency Contacts',
                text: 'Save these numbers: Ambulance: 997, Red Crescent: 997. King Fahd Medical City has the closest 24/7 emergency room.'
            },
            {
                icon: 'fa-map-marker-alt',
                title: 'Nearest Hospital',
                text: 'Based on typical traffic, King Faisal Specialist Hospital is 12 minutes away. King Fahd Medical City is 15 minutes away.'
            },
            {
                icon: 'fa-calendar-check',
                title: 'Schedule Check-up',
                text: 'Regular health screenings are important. Riyadh Care Hospital offers comprehensive check-up packages. Book online for faster service.'
            },
            {
                icon: 'fa-prescription',
                title: '24/7 Pharmacies',
                text: 'Multiple 24-hour pharmacies available on Tahlia Street and Olaya District. Download pharmacy app for home delivery.'
            }
        ],
        tourism: [
            {
                icon: 'fa-camera',
                title: 'Must-Visit This Month',
                text: 'Al Masmak Fortress and Diriyah are spectacular in current weather. Book guided tours online for 20% discount!'
            },
            {
                icon: 'fa-clock',
                title: 'Optimal Visit Times',
                text: 'Visit outdoor sites 4-7 PM for golden hour photography. Indoor attractions like National Museum best visited during peak heat (12-3 PM).'
            },
            {
                icon: 'fa-utensils',
                title: 'Culinary Experience',
                text: 'Try traditional Saudi cuisine at Najd Village Restaurant. Boulevard Riyadh City offers international dining with live entertainment.'
            },
            {
                icon: 'fa-ticket-alt',
                title: 'Weekend Events',
                text: 'Boulevard Riyadh hosts cultural performances every Friday-Saturday. Check event calendar for concerts and exhibitions.'
            }
        ],
        transportation: [
            {
                icon: 'fa-subway',
                title: 'Metro Pass Savings',
                text: 'Monthly pass (180 SAR) saves money if you commute daily. That\'s just 6 SAR per day vs 8-12 SAR for single journeys.'
            },
            {
                icon: 'fa-mobile-alt',
                title: 'Smart Ticketing',
                text: 'Download Riyadh Public Transport app for contactless payments, real-time tracking, and route planning. First ride free!'
            },
            {
                icon: 'fa-route',
                title: 'Best Routes',
                text: 'Red Line connects Airport to city center in 40 minutes. Blue Line serves business districts. Green Line for diplomatic area.'
            },
            {
                icon: 'fa-clock',
                title: 'Off-Peak Travel',
                text: 'Travel between 10 AM - 3 PM for less crowded trains and buses. Frequency increases during peak hours (6-9 AM, 4-7 PM).'
            }
        ],
        map: [
            {
                icon: 'fa-map-marked-alt',
                title: 'Explore Nearby',
                text: 'Click on markers to discover hospitals, attractions, and public transport stations. Get directions to any location instantly.'
            },
            {
                icon: 'fa-layer-group',
                title: 'Map Layers',
                text: 'Toggle layers to view traffic conditions, metro lines, or tourist attractions. Satellite view available for detailed area exploration.'
            },
            {
                icon: 'fa-bookmark',
                title: 'Save Favorites',
                text: 'Mark frequently visited locations for quick access. Your saved places sync across all devices.'
            },
            {
                icon: 'fa-share-alt',
                title: 'Share Locations',
                text: 'Share locations with friends via WhatsApp or SMS. Include estimated travel time and best route automatically.'
            }
        ]
    };

    return recommendations[pageName] || recommendations.dashboard;
}

// Display recommendations
function displayRecommendations(recommendations) {
    const modalBody = document.getElementById('aiModalBody');
    
    let html = '<div class="ai-recommendations">';
    
    recommendations.forEach(rec => {
        html += `
            <div class="ai-recommendation-card">
                <h4>
                    <i class="fas ${rec.icon}"></i>
                    ${rec.title}
                </h4>
                <p>${rec.text}</p>
            </div>
        `;
    });
    
    html += '</div>';
    
    modalBody.innerHTML = html;
}

// Initialize when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAIRecommendations);
} else {
    initAIRecommendations();
}
