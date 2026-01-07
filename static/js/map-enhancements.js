// Additional Map Enhancements and Interactivity
(function() {
	// Wait for map to be initialized
	setTimeout(function() {
		const mapEl = document.getElementById('attractions-map');
		if (!mapEl || !window.L || !window.ATTRACTIONS) return;

		// Store all markers with their categories
		const allMarkers = [];
		
		// Get the map instance (it's already created in app_enhanced.js)
		const map = mapEl._leaflet_map;
		if (!map) return;

		// Collect all existing markers
		map.eachLayer(function(layer) {
			if (layer instanceof L.Marker) {
				allMarkers.push(layer);
			}
		});

		// Add category filter controls
		const filterContainer = document.createElement('div');
		filterContainer.id = 'map-filters';
		filterContainer.style.cssText = `
			position: absolute;
			top: 20px;
			left: 60px;
			z-index: 1000;
			background: white;
			padding: 1rem;
			border-radius: 16px;
			box-shadow: 0 8px 32px rgba(0,0,0,0.2);
			display: flex;
			gap: 0.5rem;
			flex-wrap: wrap;
			max-width: calc(100% - 120px);
			animation: slideInLeft 0.6s ease-out;
		`;

		const categories = [
			{ name: 'All', icon: 'fa-globe', color: '#2D7A40' },
			{ name: 'Landmark', icon: 'fa-monument', color: '#FF6B6B' },
			{ name: 'Historical', icon: 'fa-landmark', color: '#4ECDC4' },
			{ name: 'UNESCO Site', icon: 'fa-star', color: '#FFD93D' },
			{ name: 'Museum', icon: 'fa-university', color: '#6C5CE7' },
			{ name: 'Nature', icon: 'fa-tree', color: '#00B894' },
			{ name: 'Entertainment', icon: 'fa-ticket-alt', color: '#FD79A8' },
			{ name: 'Heritage', icon: 'fa-archway', color: '#E17055' }
		];

		let activeCategory = 'All';

		// Create filter buttons
		categories.forEach(cat => {
			const btn = document.createElement('button');
			btn.className = 'map-filter-btn';
			btn.dataset.category = cat.name;
			btn.style.cssText = `
				padding: 0.6rem 1.2rem;
				border: 3px solid ${cat.color};
				background: ${cat.name === 'All' ? cat.color : 'white'};
				color: ${cat.name === 'All' ? 'white' : cat.color};
				border-radius: 24px;
				font-size: 0.9rem;
				font-weight: 700;
				cursor: pointer;
				transition: all 0.3s ease;
				display: flex;
				align-items: center;
				gap: 0.5rem;
				box-shadow: 0 4px 12px rgba(0,0,0,0.1);
			`;
			btn.innerHTML = `<i class="fas ${cat.icon}"></i><span>${cat.name}</span>`;
			
			btn.addEventListener('click', function() {
				// Update active state
				document.querySelectorAll('.map-filter-btn').forEach(b => {
					const catData = categories.find(c => c.name === b.dataset.category);
					b.style.background = 'white';
					b.style.color = catData.color;
					b.style.transform = 'scale(1)';
				});
				this.style.background = cat.color;
				this.style.color = 'white';
				this.style.transform = 'scale(1.1)';
				
				activeCategory = cat.name;
				filterMarkersByCategory(cat.name);
			});
			
			btn.addEventListener('mouseenter', function() {
				if (this.dataset.category !== activeCategory) {
					this.style.transform = 'translateY(-3px) scale(1.05)';
					this.style.boxShadow = `0 8px 24px ${cat.color}60`;
				}
			});
			
			btn.addEventListener('mouseleave', function() {
				if (this.dataset.category !== activeCategory) {
					this.style.transform = 'scale(1)';
					this.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
				}
			});
			
			filterContainer.appendChild(btn);
		});

		mapEl.parentElement.style.position = 'relative';
		mapEl.parentElement.insertBefore(filterContainer, mapEl);

		// Filter markers by category
		function filterMarkersByCategory(category) {
			let visibleCount = 0;
			
			// Get all attraction names and their categories
			Object.keys(window.ATTRACTIONS).forEach(function(name, index) {
				const attr = window.ATTRACTIONS[name];
				const markerCategory = window.getCategoryForAttraction ? window.getCategoryForAttraction(name) : '';
				
				if (allMarkers[index]) {
					if (category === 'All' || markerCategory === category) {
						if (!map.hasLayer(allMarkers[index])) {
							map.addLayer(allMarkers[index]);
						}
						visibleCount++;
					} else {
						if (map.hasLayer(allMarkers[index])) {
							map.removeLayer(allMarkers[index]);
						}
					}
				}
			});
			
			// Update counter
			const counter = document.getElementById('attractions-counter');
			if (counter) {
				counter.innerHTML = `
					<i class="fas fa-map-marked-alt me-2"></i>
					<span style="font-size: 1.8rem; font-weight: 800;">${visibleCount}</span>
					<span style="font-size: 0.95rem; opacity: 0.95; margin-left: 0.5rem;">${category === 'All' ? 'Total ' : ''}Attractions</span>
				`;
			}
		}

		// Add search box
		const searchBox = document.createElement('div');
		searchBox.style.cssText = `
			position: absolute;
			top: 90px;
			left: 60px;
			z-index: 1000;
			background: white;
			padding: 0.5rem;
			border-radius: 12px;
			box-shadow: 0 8px 32px rgba(0,0,0,0.2);
			width: 320px;
			animation: slideInLeft 0.6s ease-out 0.2s backwards;
		`;
		searchBox.innerHTML = `
			<input type="text" id="map-search" placeholder="Search attractions..." style="
				width: 100%;
				padding: 0.85rem 1rem;
				border: 3px solid #e5e7eb;
				border-radius: 10px;
				font-size: 0.95rem;
				font-weight: 600;
				outline: none;
				transition: all 0.3s ease;
			" />
		`;
		mapEl.parentElement.insertBefore(searchBox, mapEl);

		const searchInput = document.getElementById('map-search');
		searchInput.addEventListener('focus', function() {
			this.style.borderColor = '#2D7A40';
			this.style.boxShadow = '0 0 0 4px rgba(45, 122, 64, 0.15)';
			this.style.transform = 'scale(1.02)';
		});
		searchInput.addEventListener('blur', function() {
			this.style.borderColor = '#e5e7eb';
			this.style.boxShadow = 'none';
			this.style.transform = 'scale(1)';
		});

		searchInput.addEventListener('input', function(e) {
			const query = e.target.value.toLowerCase();
			let visibleCount = 0;
			
			Object.keys(window.ATTRACTIONS).forEach(function(name, index) {
				if (allMarkers[index]) {
					if (!query || name.toLowerCase().includes(query)) {
						if (!map.hasLayer(allMarkers[index])) {
							map.addLayer(allMarkers[index]);
						}
						visibleCount++;
					} else {
						if (map.hasLayer(allMarkers[index])) {
							map.removeLayer(allMarkers[index]);
						}
					}
				}
			});
			
			const counter = document.getElementById('attractions-counter');
			if (counter) {
				counter.innerHTML = `
					<i class="fas fa-search me-2"></i>
					<span style="font-size: 1.8rem; font-weight: 800;">${visibleCount}</span>
					<span style="font-size: 0.95rem; opacity: 0.95; margin-left: 0.5rem;">Found</span>
				`;
			}
		});

		// Add legend
		const legend = document.createElement('div');
		legend.style.cssText = `
			position: absolute;
			bottom: 30px;
			right: 20px;
			z-index: 1000;
			background: white;
			padding: 1.25rem;
			border-radius: 16px;
			box-shadow: 0 8px 32px rgba(0,0,0,0.2);
			animation: slideInRight 0.6s ease-out 0.4s backwards;
			border: 3px solid #2D7A40;
		`;
		legend.innerHTML = `
			<div style="font-weight: 800; margin-bottom: 1rem; color: #1B1B1B; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem;">
				<i class="fas fa-info-circle" style="color: #2D7A40; font-size: 1.25rem;"></i>
				Map Legend
			</div>
			${categories.slice(1).map(cat => `
				<div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem; padding: 0.5rem; border-radius: 8px; transition: all 0.3s ease; cursor: pointer;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background='transparent'">
					<div style="width: 20px; height: 20px; background: ${cat.color}; border-radius: 50%; box-shadow: 0 3px 8px rgba(0,0,0,0.3); border: 3px solid white;"></div>
					<span style="font-size: 0.9rem; color: #1B1B1B; font-weight: 600;">${cat.name}</span>
				</div>
			`).join('')}
		`;
		mapEl.parentElement.appendChild(legend);

		// Add attractions counter
		const counter = document.createElement('div');
		counter.id = 'attractions-counter';
		counter.style.cssText = `
			position: absolute;
			bottom: 30px;
			left: 20px;
			z-index: 1000;
			background: linear-gradient(135deg, #2D7A40 0%, #1a4d28 100%);
			color: white;
			padding: 1.25rem 1.75rem;
			border-radius: 16px;
			box-shadow: 0 8px 32px rgba(45, 122, 64, 0.4);
			font-weight: 700;
			animation: slideInLeft 0.6s ease-out 0.6s backwards;
			display: flex;
			align-items: center;
			gap: 0.75rem;
			border: 3px solid white;
		`;
		const attractionCount = Object.keys(window.ATTRACTIONS).length;
		counter.innerHTML = `
			<i class="fas fa-map-marked-alt" style="font-size: 1.5rem;"></i>
			<span style="font-size: 1.8rem; font-weight: 800;">${attractionCount}</span>
			<span style="font-size: 0.95rem; opacity: 0.95;">Total Attractions</span>
		`;
		mapEl.parentElement.appendChild(counter);

	}, 1500); // Wait for map to fully initialize

})();
