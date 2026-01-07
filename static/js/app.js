// Enhanced interactivity for Tourism page: modal, filtering, facts, reactions
console.log('Ruaa Smart City app loaded');

document.addEventListener('DOMContentLoaded', function () {
	// Bootstrap modal element
	const modalEl = document.getElementById('attraction-modal');
	let modal = null;
	if (modalEl && window.bootstrap && window.bootstrap.Modal) {
		modal = new bootstrap.Modal(modalEl);
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
		// open modal when clicking card (but ignore clicks on buttons inside)
		card.addEventListener('click', function (e) {
			if (e.target.closest('.fact-btn') || e.target.closest('.react-btn')) return;
			const img = card.querySelector('.tourism-image')?.src || '';
			const name = card.dataset.name || card.querySelector('.tourism-title')?.innerText || '';
			const category = card.dataset.category || '';
			const lat = card.dataset.lat || '';
			const lng = card.dataset.lng || '';
			const desc = card.querySelector('.tourism-description')?.innerText || '';

			if (modal) {
				modalEl.querySelector('#modal-name').innerText = name;
				modalEl.querySelector('#modal-category').innerText = category;
				modalEl.querySelector('#modal-desc').innerText = desc;
				modalEl.querySelector('#modal-location').innerText = (lat && lng) ? `Approx. ${lat}, ${lng}` : 'Not specified';
				const info = window.ATTRACTIONS && window.ATTRACTIONS[name] ? window.ATTRACTIONS[name] : null;
				// gallery handling
				if (info && info.gallery && info.gallery.length) {
					modalEl.querySelector('#modal-image').src = info.gallery[0];
					modalEl._gallery = info.gallery.slice();
					modalEl._galleryIndex = 0;
				} else {
					modalEl.querySelector('#modal-image').src = img;
					modalEl._gallery = [img];
					modalEl._galleryIndex = 0;
				}
				// video
				if (info && info.video) {
					modalEl.querySelector('#modal-video').style.display = '';
					modalEl.querySelector('#modal-video-src').src = info.video;
					const v = modalEl.querySelector('#modal-video-el'); v.load();
				} else {
					modalEl.querySelector('#modal-video').style.display = 'none';
					modalEl.querySelector('#modal-video-src').src = '';
				}
				// meta
				modalEl.querySelector('#modal-hours').innerText = info?.hours || 'Check official site';
				modalEl.querySelector('#modal-price').innerText = info?.price || 'Varies / N/A';
				modalEl.querySelector('#modal-tips').innerText = info?.tips || 'Respect local customs.';
				modal.show();
			}
		});

		// init reaction counts from localStorage
		// Emoji reactions: toggle + persist per-card in localStorage
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

		// quick facts
		card.querySelectorAll('.fact-btn').forEach(fb => {
			fb.addEventListener('click', function (ev) {
				ev.stopPropagation();
				const tip = fb.title || fb.dataset.fact || fb.innerText || 'Fun fact!';
				showMiniPopup(fb, tip);
			});
		});
	});

	// Filtering

	// helper to hide/show cards with fade animations
	function hideCard(card) {
		card.classList.remove('fade-in');
		card.classList.add('fade-out');
		setTimeout(() => {
			card.style.display = 'none';
		}, 320);
	}

	function showCard(card) {
		card.style.display = '';
		// Filtering
		document.querySelectorAll('.filter-badge').forEach(btn => {
			btn.addEventListener('click', function () {
				document.querySelectorAll('.filter-badge').forEach(x => x.classList.remove('active'));
				btn.classList.add('active');
				const filter = btn.dataset.filter;
				document.querySelectorAll('.tourism-card').forEach(card => {
					const match = (!filter || filter === 'All' || card.dataset.category === filter);
					if (match) showCard(card); else hideCard(card);
				});
			});
		});

		// Trip recommendation logic (very simple): pick attractions by category mapping (single listener)
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

		// Map: inline the SVG so markers are fully interactive and stylable
		const mapContainer = document.createElement('div');
		mapContainer.style.marginTop = '1.5rem';
		mapContainer.style.borderRadius = '0.75rem';
		mapContainer.style.overflow = 'hidden';
		const tourismGrid = document.querySelector('.tourism-grid');
		if (tourismGrid && tourismGrid.parentNode) {
			tourismGrid.parentNode.insertBefore(mapContainer, tourismGrid.nextSibling);
			fetch('/static/svg/riyadh_map.svg').then(r => r.text()).then(svgText => {
				mapContainer.innerHTML = svgText;
				const svgEl = mapContainer.querySelector('svg');
				if (!svgEl) return;
				// add pulse class to dots
				svgEl.querySelectorAll('.map-dot').forEach(d => d.classList.add('pulse'));

				// create reusable popup element for map
				const mapPopup = document.createElement('div');
				mapPopup.className = 'map-popup card shadow';
				mapPopup.style.position = 'absolute';
				mapPopup.style.display = 'none';
				mapPopup.style.zIndex = 9999;
				mapPopup.style.padding = '0.5rem';
				mapPopup.style.borderRadius = '0.5rem';
				document.body.appendChild(mapPopup);

				function showMapPopup(name, img, desc, pageX, pageY, cardEl) {
					mapPopup.innerHTML = `<div style="display:flex; gap:0.5rem; align-items:center;"><img src="${img}" style="width:96px;height:64px;object-fit:cover;border-radius:6px"><div><strong>${name}</strong><div style="font-size:0.85rem;color:#666">${desc}</div><div style="margin-top:6px;text-align:right"><button class='btn btn-sm btn-primary view-details'>View Details</button> <button class='btn btn-sm btn-outline-secondary close-map'>Close</button></div></div></div>`;
					mapPopup.style.left = Math.max(8, pageX) + 'px';
					mapPopup.style.top = Math.max(8, pageY) + 'px';
					mapPopup.style.display = '';

					const vbtn = mapPopup.querySelector('.view-details');
					if (vbtn && cardEl) vbtn.addEventListener('click', ()=>{ cardEl.click(); mapPopup.style.display='none'; });
					const closeBtn = mapPopup.querySelector('.close-map');
					if (closeBtn) closeBtn.addEventListener('click', ()=> mapPopup.style.display='none');
				}

				svgEl.querySelectorAll('.map-dot').forEach(dot => {
					dot.style.cursor = 'pointer';
					dot.addEventListener('click', function (ev) {
						ev.stopPropagation();
						const name = this.getAttribute('data-name') || this.id.replace('dot-','');
						const img = this.getAttribute('data-image') || '';
						const desc = this.getAttribute('data-desc') || '';
						const card = Array.from(document.querySelectorAll('.tourism-card')).find(c => (c.dataset.name||'') === name || (c.dataset.id||'') === (name.replace(/\s+/g,'-').toLowerCase()));
						const pt = this.getBoundingClientRect();
						const pageX = pt.left + (pt.width/2);
						const pageY = pt.top + (pt.height/2);
						showMapPopup(name, img, desc, pageX + 10, pageY + 10, card);
					});
				});
			}).catch(()=>{});
		}

		// Scroll-triggered animations (Intersection Observer)
		const observer = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					entry.target.classList.add('in-view');
					// stagger children for cards
					if (entry.target.classList.contains('tourism-card')) {
						const els = entry.target.querySelectorAll('.tourism-image, .tourism-content');
						els.forEach((ch, idx) => setTimeout(() => ch.classList.add('in-view'), idx * 80));
					}
					observer.unobserve(entry.target);
				}
			});
		}, { threshold: 0.12 });

		// observe hero and cards
		document.querySelectorAll('.scroll-animate').forEach(el => observer.observe(el));

			// modal gallery controls
			const prevBtn = document.getElementById('modal-prev');
			const nextBtn = document.getElementById('modal-next');
			if (prevBtn && nextBtn) {
				prevBtn.addEventListener('click', function (ev) {
					ev.stopPropagation();
					const g = modalEl._gallery || [];
					if (!g.length) return;
					modalEl._galleryIndex = (modalEl._galleryIndex - 1 + g.length) % g.length;
					modalEl.querySelector('#modal-image').src = g[modalEl._galleryIndex];
				});
				nextBtn.addEventListener('click', function (ev) {
					ev.stopPropagation();
					const g = modalEl._gallery || [];
					if (!g.length) return;
					modalEl._galleryIndex = (modalEl._galleryIndex + 1) % g.length;
					modalEl.querySelector('#modal-image').src = g[modalEl._galleryIndex];
				});
			}
		}
});


