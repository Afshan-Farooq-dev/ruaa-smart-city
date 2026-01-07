// Enhanced Tourism App with 6 New Features:
// Feature 2: Accessibility (WCAG 2.1 AA)
// Feature 3: Virtual Tours & 360° Views
// Feature 5: User Reviews & Ratings
// Feature 6: Real-Time Weather & Best Visit Times
// Feature 7: Personalized AI Recommendations
// Feature 14: Transportation Integration with Leaflet.js

console.log('Ruaa Smart City Enhanced App loaded');

document.addEventListener('DOMContentLoaded', function () {
	// Bootstrap modal elements
	const modalEl = document.getElementById('attraction-modal');
	const directionsModalEl = document.getElementById('directions-modal');
	let modal = null;
	let directionsModal = null;
	
	if (modalEl && window.bootstrap && window.bootstrap.Modal) {
		modal = new bootstrap.Modal(modalEl);
	}
	if (directionsModalEl && window.bootstrap && window.bootstrap.Modal) {
		directionsModal = new bootstrap.Modal(directionsModalEl);
	}

	// Current attraction context
	let currentAttraction = null;
	let userFavorites = JSON.parse(localStorage.getItem('user_favorites') || '[]');
	
	// FEATURE 2: Accessibility - High Contrast Mode
	const accessibilityToggle = document.getElementById('accessibility-toggle');
	if (accessibilityToggle) {
		const isHighContrast = localStorage.getItem('high_contrast') === 'true';
		if (isHighContrast) document.body.classList.add('high-contrast');
		
		accessibilityToggle.addEventListener('click', function() {
			document.body.classList.toggle('high-contrast');
			const enabled = document.body.classList.contains('high-contrast');
			localStorage.setItem('high_contrast', enabled);
			announceToScreenReader(enabled ? 'High contrast mode enabled' : 'High contrast mode disabled');
		});
		
		// Keyboard navigation (Enter/Space)
		accessibilityToggle.addEventListener('keydown', function(e) {
			if (e.key === 'Enter' || e.key === ' ') {
				e.preventDefault();
				this.click();
			}
		});
	}
	
	// Screen reader announcements
	function announceToScreenReader(message) {
		const announce = document.createElement('div');
		announce.setAttribute('role', 'status');
		announce.setAttribute('aria-live', 'polite');
		announce.className = 'sr-only';
		announce.textContent = message;
		document.body.appendChild(announce);
		setTimeout(() => announce.remove(), 1000);
	}

	// Helper to show short popups for quick facts
	function showMiniPopup(el, text) {
		const popup = document.createElement('div');
		popup.className = 'mini-popup';
		popup.innerText = text;
		Object.assign(popup.style, {
			position: 'absolute',
			background: '#fff',
			border: '1px solid rgba(0,0,0,0.06)',
			padding: '0.4rem 0.6rem',
			borderRadius: '0.5rem',
			boxShadow: '0 6px 18px rgba(0,0,0,0.08)',
			zIndex: 9999,
			fontSize: '0.9rem',
			color: '#111'
		});
		document.body.appendChild(popup);
		const rect = el.getBoundingClientRect();
		popup.style.left = (rect.left + window.scrollX) + 'px';
		popup.style.top = (rect.bottom + window.scrollY + 8) + 'px';
		setTimeout(() => popup.remove(), 2200);
	}

	// Initialize cards
	document.querySelectorAll('.tourism-card').forEach(card => {
		// FEATURE 2: Accessibility - Keyboard navigation for cards
		card.setAttribute('tabindex', '0');
		card.setAttribute('role', 'button');
		card.setAttribute('aria-label', `View details for ${card.dataset.name}`);
		
		// Open modal when clicking card or pressing Enter/Space
		function openCardModal(e) {
			if (e.target.closest('.fact-btn') || e.target.closest('.react-btn')) return;
			if (e.type === 'keydown' && e.key !== 'Enter' && e.key !== ' ') return;
			if (e.type === 'keydown') e.preventDefault();
			
			const img = card.querySelector('.tourism-image')?.src || '';
			const name = card.dataset.name || card.querySelector('.tourism-title')?.innerText || '';
			const category = card.dataset.category || '';
			const lat = card.dataset.lat || '';
			const lng = card.dataset.lng || '';
			const desc = card.querySelector('.tourism-description')?.innerText || '';

			currentAttraction = name;
			
			if (modal) {
				modalEl.querySelector('#modal-name').innerText = name;
				modalEl.querySelector('#modalTitle').innerText = name;
				modalEl.querySelector('#modal-category').innerText = category;
				modalEl.querySelector('#modal-desc').innerText = desc;
				modalEl.querySelector('#modal-location').innerText = (lat && lng) ? `${lat}, ${lng}` : 'Not specified';
				
				const info = window.ATTRACTIONS && window.ATTRACTIONS[name] ? window.ATTRACTIONS[name] : null;
				
				// Gallery handling
				if (info && info.gallery && info.gallery.length) {
					modalEl.querySelector('#modal-image').src = info.gallery[0];
					modalEl.querySelector('#modal-image').alt = `${name} - Image 1 of ${info.gallery.length}`;
					modalEl._gallery = info.gallery.slice();
					modalEl._galleryIndex = 0;
				} else {
					modalEl.querySelector('#modal-image').src = img;
					modalEl.querySelector('#modal-image').alt = name;
					modalEl._gallery = [img];
					modalEl._galleryIndex = 0;
				}
				
				// Video
				if (info && info.video) {
					modalEl.querySelector('#modal-video').style.display = '';
					modalEl.querySelector('#modal-video-src').src = info.video;
					const v = modalEl.querySelector('#modal-video-el'); v.load();
				} else {
					modalEl.querySelector('#modal-video').style.display = 'none';
					modalEl.querySelector('#modal-video-src').src = '';
				}
				
				// Metadata
				modalEl.querySelector('#modal-hours').innerText = info?.hours || 'Check official site';
				modalEl.querySelector('#modal-price').innerText = info?.price || 'Varies / N/A';
				modalEl.querySelector('#modal-tips').innerText = info?.tips || 'Respect local customs.';
				
				// FEATURE 3: Virtual Tours
				const virtualTourSection = modalEl.querySelector('#virtual-tour-section');
				const virtualTourBtn = modalEl.querySelector('#virtual-tour-btn');
				const virtualTourFrame = modalEl.querySelector('#virtual-tour-frame');
				
				if (info && info.virtual_tour) {
					virtualTourSection.style.display = '';
					virtualTourBtn.onclick = function() {
						virtualTourFrame.src = info.virtual_tour;
						virtualTourFrame.style.display = '';
						virtualTourBtn.style.display = 'none';
						announceToScreenReader('Virtual tour loaded');
					};
				} else {
					virtualTourSection.style.display = 'none';
				}
				
				// FEATURE 5: Reviews & Ratings
				loadReviews(name);
				
				// FEATURE 6: Weather Widget
				loadWeather(name);
				
				// FEATURE 7: Favorite button
				updateFavoriteButton(name);
				
				modal.show();
				announceToScreenReader(`Opened details for ${name}`);
			}
		}
		
		card.addEventListener('click', openCardModal);
		card.addEventListener('keydown', openCardModal);

		// Initialize reaction counts from localStorage
		const STORAGE_KEY = 'reactions_DATA';
		let allReactions = {};
		try { allReactions = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); } catch (err) { allReactions = {}; }
		const cardId = card.dataset.id || (card.dataset.name || '').replace(/\s+/g,'_');
		if (!allReactions[cardId]) {
			allReactions[cardId] = { counts: { heart: 0, star: 0, camera: 0 }, selected: { heart: false, star: false, camera: false } };
		}
		const cardData = allReactions[cardId];
		
		card.querySelectorAll('.react-btn').forEach(btn => {
			const type = btn.dataset.reaction;
			const span = btn.querySelector('.count');
			if (span) span.innerText = cardData.counts[type] || 0;
			if (cardData.selected[type]) btn.classList.add('active');
			
			btn.addEventListener('click', function (ev) {
				ev.stopPropagation();
				cardData.selected[type] = !cardData.selected[type];
				if (cardData.selected[type]) {
					cardData.counts[type] = (cardData.counts[type] || 0) + 1;
					btn.classList.add('active');
				} else {
					cardData.counts[type] = Math.max(0, (cardData.counts[type] || 0) - 1);
					btn.classList.remove('active');
				}
				if (span) span.innerText = cardData.counts[type];
				allReactions[cardId] = cardData;
				localStorage.setItem(STORAGE_KEY, JSON.stringify(allReactions));
			});
		});

		// Quick facts
		card.querySelectorAll('.fact-btn').forEach(fb => {
			fb.addEventListener('click', function (ev) {
				ev.stopPropagation();
				const tip = fb.title || fb.dataset.fact || fb.innerText || 'Fun fact!';
				showMiniPopup(fb, tip);
			});
		});
	});

	// FEATURE 5: Reviews - Load and display reviews
	function loadReviews(attractionName) {
		const reviewsData = window.REVIEWS_DATA || {};
		const data = reviewsData[attractionName] || { avg_rating: 0, count: 0, recent: [] };
		
		// Update rating display
		document.getElementById('avg-rating').innerText = data.avg_rating ? data.avg_rating.toFixed(1) : '—';
		document.getElementById('rating-count').innerText = `${data.count} reviews`;
		
		// Update stars
		const stars = '★'.repeat(Math.round(data.avg_rating)) + '☆'.repeat(5 - Math.round(data.avg_rating));
		document.getElementById('rating-stars').innerText = stars;
		
		// Display recent reviews
		const reviewsList = document.getElementById('reviews-list');
		if (data.recent && data.recent.length > 0) {
			reviewsList.innerHTML = data.recent.map(r => `
				<div class="card" style="padding:1rem; margin:0.5rem 0; background:#fafafa;">
					<div style="display:flex; justify-content:space-between; align-items:center;">
						<strong>${r.user__username}</strong>
						<span style="color:#f59e0b;">${'★'.repeat(r.rating)}${'☆'.repeat(5-r.rating)}</span>
					</div>
					<p style="margin:0.5rem 0 0 0; font-size:0.9rem;">${r.text}</p>
					<small style="color:#999;">${new Date(r.created).toLocaleDateString()}</small>
				</div>
			`).join('');
		} else {
			reviewsList.innerHTML = '<p style="color:#999; font-style:italic;">No reviews yet. Be the first!</p>';
		}
	}
	
	// FEATURE 5: Submit Review
	const submitReviewBtn = document.getElementById('submit-review-btn');
	let selectedRating = 0;
	
	// Star rating selection
	document.querySelectorAll('#review-stars .star').forEach((star, index) => {
		star.addEventListener('click', function() {
			selectedRating = parseInt(this.dataset.rating);
			document.querySelectorAll('#review-stars .star').forEach((s, i) => {
				s.innerText = i < selectedRating ? '★' : '☆';
				s.setAttribute('aria-checked', i < selectedRating ? 'true' : 'false');
			});
		});
		
		// Keyboard navigation for stars
		star.addEventListener('keydown', function(e) {
			if (e.key === 'Enter' || e.key === ' ') {
				e.preventDefault();
				this.click();
			}
		});
	});
	
	if (submitReviewBtn) {
		submitReviewBtn.addEventListener('click', async function() {
			const text = document.getElementById('review-text').value.trim();
			
			if (selectedRating === 0 || !text) {
				alert('Please provide both a rating and review text.');
				return;
			}
			
			try {
				const response = await fetch('/api/submit-review/', {
					method: 'POST',
					headers: { 'Content-Type': 'application/json' },
					body: JSON.stringify({
						attraction_name: currentAttraction,
						rating: selectedRating,
						text: text
					})
				});
				
				const result = await response.json();
				
				if (result.success) {
					alert('Review submitted successfully!');
					document.getElementById('review-text').value = '';
					selectedRating = 0;
					document.querySelectorAll('#review-stars .star').forEach(s => s.innerText = '☆');
					loadReviews(currentAttraction); // Reload reviews
					announceToScreenReader('Review submitted successfully');
				} else {
					alert('Error submitting review: ' + (result.error || 'Unknown error'));
				}
			} catch (error) {
				console.error('Error:', error);
				alert('Failed to submit review. Please try again.');
			}
		});
	}
	
	// FEATURE 6: Real-Time Weather
	async function loadWeather(attractionName) {
		try {
			const response = await fetch(`/api/weather/${encodeURIComponent(attractionName)}/`);
			const data = await response.json();
			
			if (!data.error) {
				document.getElementById('weather-temp').innerText = `${data.temp}°C`;
				document.getElementById('weather-condition').innerText = data.condition;
				document.getElementById('best-time').innerText = data.best_time;
				document.getElementById('crowd-level').innerText = data.crowd_level;
				
				// Simple icon mapping
				const iconMap = {
					'Clear': '☀️',
					'Clouds': '☁️',
					'Rain': '🌧️',
					'Snow': '❄️',
					'Thunderstorm': '⛈️',
					'Drizzle': '🌦️',
					'Mist': '🌫️',
					'Fog': '🌫️'
				};
				document.getElementById('weather-icon').innerText = iconMap[data.condition] || '☀️';
			}
		} catch (error) {
			console.error('Weather error:', error);
		}
	}
	
	// FEATURE 7: Favorite Toggle
	const favoriteBtn = document.getElementById('favorite-btn');
	if (favoriteBtn) {
		favoriteBtn.addEventListener('click', async function(e) {
			e.stopPropagation();
			
			try {
				const response = await fetch('/api/toggle-favorite/', {
					method: 'POST',
					headers: { 'Content-Type': 'application/json' },
					body: JSON.stringify({ attraction_name: currentAttraction })
				});
				
				const result = await response.json();
				
				if (result.success) {
					userFavorites = result.favorites;
					localStorage.setItem('user_favorites', JSON.stringify(userFavorites));
					updateFavoriteButton(currentAttraction);
					announceToScreenReader(result.is_favorite ? 'Added to favorites' : 'Removed from favorites');
				}
			} catch (error) {
				console.error('Favorite error:', error);
			}
		});
	}
	
	function updateFavoriteButton(attractionName) {
		const isFavorite = userFavorites.includes(attractionName);
		favoriteBtn.innerHTML = isFavorite ? '<i class="fas fa-heart"></i>' : '<i class="far fa-heart"></i>';
		favoriteBtn.setAttribute('aria-label', isFavorite ? 'Remove from favorites' : 'Add to favorites');
		favoriteBtn.className = isFavorite ? 'btn btn-sm btn-danger' : 'btn btn-sm btn-outline-danger';
	}
	
	// FEATURE 7: AI Recommendations
	const getRecommendationsBtn = document.getElementById('get-recommendations-btn');
	if (getRecommendationsBtn) {
		getRecommendationsBtn.addEventListener('click', async function() {
			this.disabled = true;
			this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Loading...';
			
			try {
				const response = await fetch('/api/recommendations/');
				const result = await response.json();
				
				if (!result.error && result.recommendations) {
				const grid = document.getElementById('recommendations-grid');
				grid.innerHTML = result.recommendations.map(attr => `
					<div class="card recommendation-card" style="
						padding:0; 
						cursor:pointer; 
						border-radius:16px; 
						overflow:hidden; 
						border:3px solid #2D7A40; 
						box-shadow:0 8px 24px rgba(45, 122, 64, 0.2);
						transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
						animation: bounceIn 0.6s ease-out;
					" data-rec-name="${attr.name}">
						<img src="${attr.image}" style="
							width:100%; 
							height:160px; 
							object-fit:cover;
							transition: all 0.4s ease;
						" alt="${attr.name}" />
						<div style="padding:1rem; background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);">
							<h6 style="margin:0 0 0.5rem 0; color:#1B1B1B; font-weight:700; font-size:1rem;">${attr.name}</h6>
							<p style="font-size:0.85rem; margin:0; color:white; background:linear-gradient(135deg, #2D7A40 0%, #1a4d28 100%); padding:0.4rem 0.8rem; border-radius:20px; display:inline-block; font-weight:600;">
								<i class="fas fa-tag me-1"></i>${attr.category}
							</p>
						</div>
					</div>
				`).join('');
				
				document.getElementById('recommendations-result').style.display = '';
				
				// Make recommendation cards clickable with hover effects
				grid.querySelectorAll('[data-rec-name]').forEach(recCard => {
					recCard.addEventListener('mouseenter', function() {
						this.style.transform = 'translateY(-12px) scale(1.03)';
						this.style.boxShadow = '0 16px 48px rgba(45, 122, 64, 0.4)';
						this.querySelector('img').style.transform = 'scale(1.1)';
					});
					recCard.addEventListener('mouseleave', function() {
						this.style.transform = 'translateY(0) scale(1)';
						this.style.boxShadow = '0 8px 24px rgba(45, 122, 64, 0.2)';
						this.querySelector('img').style.transform = 'scale(1)';
					});
					recCard.addEventListener('click', function() {
						const card = Array.from(document.querySelectorAll('.tourism-card')).find(c => c.dataset.name === this.dataset.recName);
						if (card) card.click();
					});
				});
									announceToScreenReader('AI recommendations loaded');
				}
			} catch (error) {
				console.error('Recommendations error:', error);
			} finally {
				this.disabled = false;
				this.innerHTML = '<i class="fas fa-magic me-2"></i>Get AI Recommendations';
			}
		});
	}
	
	// FEATURE 14: Leaflet Directions
	const directionsBtn = document.getElementById('directions-btn');
	if (directionsBtn) {
		directionsBtn.addEventListener('click', function() {
			modal.hide();
			showDirectionsMap();
		});
	}
	
	let leafletMap = null;
	function showDirectionsMap() {
		if (!directionsModal) return;
		
		directionsModal.show();
		
		setTimeout(() => {
			if (!leafletMap) {
				const info = window.ATTRACTIONS[currentAttraction];
				const lat = info?.lat || 24.7136;
				const lng = info?.lng || 46.6753;
				
				leafletMap = L.map('leaflet-map').setView([lat, lng], 14);
				
				L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
					attribution: '© OpenStreetMap contributors'
				}).addTo(leafletMap);
				
				// Add marker
				L.marker([lat, lng]).addTo(leafletMap)
					.bindPopup(`<b>${currentAttraction}</b>`)
					.openPopup();
				
				// Mock transit info
				document.getElementById('transit-list').innerHTML = `
					<div style="margin-top:0.5rem;">
						<p><strong>🚇 Nearest Metro:</strong> King Abdullah Financial District Station (2.3 km)</p>
						<p><strong>🚌 Bus Routes:</strong> 12, 45, 67 (Stop at City Center)</p>
						<p style="margin-top:1rem;"><em>Note: Real-time transit data integration coming soon!</em></p>
					</div>
				`;
			} else {
				leafletMap.invalidateSize();
			}
		}, 300);
	}

	// Trip recommendation logic
	const tripBtn = document.getElementById('trip-btn');
	if (tripBtn) {
		tripBtn.addEventListener('click', function () {
			const type = document.getElementById('trip-type').value;
			const time = parseInt(document.getElementById('trip-time').value, 10);
			const map = {
				'History': ['Historical','Museum','UNESCO Site'],
				'Culture': ['Museum','UNESCO Site','Landmark'],
				'Modern': ['Entertainment','Landmark'],
				'Outdoor': ['Nature']
			};
			const cats = map[type] || ['Landmark'];
			const cards = Array.from(document.querySelectorAll('.tourism-card')).filter(c => cats.includes(c.dataset.category));
			const count = time === 1 ? 1 : (time === 3 ? 2 : 3);
			const picks = cards.slice(0, count).map(c => c.dataset.name || c.querySelector('.tourism-title')?.innerText);
			const out = document.getElementById('trip-result');
			if (out) {
				if (!picks.length) out.innerText = 'No matching attractions found.';
				else out.innerHTML = '<strong>Suggested itinerary:</strong><br>' + picks.map((p,i)=>`${i+1}. ${p}`).join('<br>');
			}
		});
	}

	// INTERACTIVE LEAFLET MAP with Custom Markers
	const attractionsMapEl = document.getElementById('attractions-map');
	if (attractionsMapEl && window.L && window.ATTRACTIONS) {
		// Initialize map centered on Riyadh
		const attractionsMap = L.map('attractions-map').setView([24.7136, 46.6753], 11);
		
		// Add OpenStreetMap tiles
		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			attribution: '© OpenStreetMap contributors',
			maxZoom: 18
		}).addTo(attractionsMap);
		
		// Custom marker icons by category
		const iconColors = {
			'Landmark': '#FF6B6B',
			'Historical': '#4ECDC4',
			'UNESCO Site': '#FFD93D',
			'Museum': '#6C5CE7',
			'Nature': '#00B894',
			'Entertainment': '#FD79A8'
		};
		
		function createCustomIcon(category) {
			const color = iconColors[category] || '#2D7A40';
			return L.divIcon({
				className: 'custom-marker',
				html: `
					<div style="position: relative;">
						<div style="
							width: 40px;
							height: 40px;
							background: ${color};
							border: 4px solid white;
							border-radius: 50% 50% 50% 0;
							transform: rotate(-45deg);
							box-shadow: 0 4px 12px rgba(0,0,0,0.3);
							display: flex;
							align-items: center;
							justify-content: center;
						">
							<i class="fas fa-map-marker-alt" style="
								color: white;
								font-size: 1.25rem;
								transform: rotate(45deg);
							"></i>
						</div>
						<div style="
							position: absolute;
							top: -8px;
							left: 50%;
							transform: translateX(-50%);
							width: 12px;
							height: 12px;
							background: white;
							border: 2px solid ${color};
							border-radius: 50%;
							animation: pulse-marker 2s infinite;
						"></div>
					</div>
				`,
				iconSize: [40, 40],
				iconAnchor: [20, 40],
				popupAnchor: [0, -40]
			});
		}
		
		// Add CSS for marker animation
		const style = document.createElement('style');
		style.textContent = `
			@keyframes pulse-marker {
				0%, 100% { transform: translateX(-50%) scale(1); opacity: 1; }
				50% { transform: translateX(-50%) scale(1.5); opacity: 0.5; }
			}
			.custom-marker {
				background: none;
				border: none;
			}
			.leaflet-popup-content-wrapper {
				border-radius: 12px;
				box-shadow: 0 8px 24px rgba(0,0,0,0.2);
			}
			.leaflet-popup-content {
				margin: 0;
				padding: 0;
			}
		`;
		document.head.appendChild(style);
		
		// Add markers for each attraction
		Object.keys(window.ATTRACTIONS).forEach(name => {
			const attraction = window.ATTRACTIONS[name];
			if (attraction.lat && attraction.lng) {
				const marker = L.marker([attraction.lat, attraction.lng], {
					icon: createCustomIcon(getCategoryForAttraction(name))
				}).addTo(attractionsMap);
				
				// Create rich popup content
				const popupContent = `
					<div style="width: 280px; padding: 1rem;">
						<div style="display: flex; align-items: start; gap: 1rem; margin-bottom: 1rem;">
							<img src="${attraction.gallery[0]}" alt="${name}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 8px;" />
							<div style="flex: 1;">
								<h6 style="margin: 0 0 0.25rem 0; font-size: 1rem; color: #1B1B1B;">${name}</h6>
								<div style="display: flex; align-items: center; gap: 0.25rem; color: #F59E0B; font-size: 0.9rem; margin-bottom: 0.25rem;">
									${'★'.repeat(Math.round(attraction.rating))}${'☆'.repeat(5 - Math.round(attraction.rating))}
									<span style="color: #6B7280; font-size: 0.85rem;">(${attraction.reviews_count})</span>
								</div>
								<div style="font-size: 0.85rem; color: #6B7280;">${getCategoryForAttraction(name)}</div>
							</div>
						</div>
						<div style="display: grid; gap: 0.5rem; font-size: 0.85rem; color: #4B5563;">
							<div><i class="fas fa-clock" style="color: #2D7A40; width: 16px;"></i> ${attraction.hours}</div>
							<div><i class="fas fa-ticket-alt" style="color: #2D7A40; width: 16px;"></i> ${attraction.price}</div>
						</div>
						<button class="btn btn-sm btn-primary w-100" onclick="openAttractionModal('${name}')" style="margin-top: 1rem; background: linear-gradient(135deg, #2D7A40 0%, #1a4d28 100%); border: none;">
							<i class="fas fa-info-circle me-1"></i>View Details
						</button>
					</div>
				`;
				
				marker.bindPopup(popupContent, {
					maxWidth: 300,
					className: 'attraction-popup'
				});
				
				// Pulse effect on hover
				marker.on('mouseover', function() {
					this.getElement().style.transform = 'scale(1.2)';
					this.getElement().style.transition = 'transform 0.3s ease';
				});
				marker.on('mouseout', function() {
					this.getElement().style.transform = 'scale(1)';
				});
			}
		});
		
		// Helper function to get category for an attraction
		function getCategoryForAttraction(name) {
			const cards = document.querySelectorAll('.tourism-card');
			for (let card of cards) {
				if (card.dataset.name === name) {
					return card.dataset.category || 'Other';
				}
			}
			return 'Other';
		}
		
		// Global function to open modal from map popup
		window.openAttractionModal = function(name) {
			const card = Array.from(document.querySelectorAll('.tourism-card')).find(c => c.dataset.name === name);
			if (card) {
				card.click();
				attractionsMap.closePopup();
			}
		};
	}

	// Modal gallery controls
	const prevBtn = document.getElementById('modal-prev');
	const nextBtn = document.getElementById('modal-next');
	if (prevBtn && nextBtn) {
		prevBtn.addEventListener('click', function (ev) {
			ev.stopPropagation();
			const g = modalEl._gallery || [];
			if (!g.length) return;
			modalEl._galleryIndex = (modalEl._galleryIndex - 1 + g.length) % g.length;
			modalEl.querySelector('#modal-image').src = g[modalEl._galleryIndex];
			modalEl.querySelector('#modal-image').alt = `${currentAttraction} - Image ${modalEl._galleryIndex + 1} of ${g.length}`;
			announceToScreenReader(`Image ${modalEl._galleryIndex + 1} of ${g.length}`);
		});
		
		nextBtn.addEventListener('click', function (ev) {
			ev.stopPropagation();
			const g = modalEl._gallery || [];
			if (!g.length) return;
			modalEl._galleryIndex = (modalEl._galleryIndex + 1) % g.length;
			modalEl.querySelector('#modal-image').src = g[modalEl._galleryIndex];
			modalEl.querySelector('#modal-image').alt = `${currentAttraction} - Image ${modalEl._galleryIndex + 1} of ${g.length}`;
			announceToScreenReader(`Image ${modalEl._galleryIndex + 1} of ${g.length}`);
		});
		
		// Keyboard navigation for gallery
		prevBtn.addEventListener('keydown', function(e) {
			if (e.key === 'Enter' || e.key === ' ') {
				e.preventDefault();
				this.click();
			}
		});
		nextBtn.addEventListener('keydown', function(e) {
			if (e.key === 'Enter' || e.key === ' ') {
				e.preventDefault();
				this.click();
			}
		});
	}

	// Scroll-triggered animations (Intersection Observer)
	const observer = new IntersectionObserver((entries) => {
		entries.forEach((entry) => {
			if (entry.isIntersecting) {
				entry.target.classList.add('in-view');
				if (entry.target.classList.contains('tourism-card')) {
					const els = entry.target.querySelectorAll('.tourism-image, .tourism-content');
					els.forEach((ch, idx) => setTimeout(() => ch.classList.add('in-view'), idx * 80));
				}
				observer.unobserve(entry.target);
			}
		});
	}, { threshold: 0.12 });

	document.querySelectorAll('.scroll-animate').forEach(el => observer.observe(el));
});
