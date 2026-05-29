/**
 * Soul Restaurant & Bar | Premium JS Controllers
 */

// 1. Page Loader Logic
window.addEventListener('load', () => {
    const loader = document.querySelector('.page-loader');
    if(loader) {
        setTimeout(() => {
            loader.classList.add('hidden');
        }, 300); // give it a brief moment before fading out
    }
});

document.addEventListener('DOMContentLoaded', () => {
    
    // 2. Sticky Glass Navbar
    const nav = document.querySelector('.glass-nav');
    window.addEventListener('scroll', () => {
        if(window.scrollY > 80) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    // 3. Current Page Highlighting
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-link').forEach(link => {
        if(link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });

    // 4. Mobile Hamburger Menu
    const menuToggle = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');
    if(menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('is-active');
            navLinks.classList.toggle('active');
        });
        
        // Close menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('is-active');
                navLinks.classList.remove('active');
            });
        });
    }

    // 5. Smooth scrolling for internal anchor links (if any like #menu)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetAttr = this.getAttribute('href');
            if (targetAttr !== "#") {
                const targetElement = document.querySelector(targetAttr);
                if (targetElement) {
                    e.preventDefault();
                    targetElement.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // 6. Menu Dynamic Filtering
    const filterBtns = document.querySelectorAll('.filter-btn');
    const menuItems = document.querySelectorAll('.menu-card');

    if (filterBtns.length > 0 && menuItems.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filterValue = btn.getAttribute('data-filter');
                
                menuItems.forEach(item => {
                    if (filterValue === 'all' || item.classList.contains(filterValue)) {
                        item.classList.remove('hidden');
                        setTimeout(() => item.style.opacity = '1', 50);
                    } else {
                        item.style.opacity = '0';
                        setTimeout(() => item.classList.add('hidden'), 300);
                    }
                });
            });
        });
    }

    // 7. Gallery Lightbox Logic
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.lightbox-close');
    const galleryImages = document.querySelectorAll('.gallery-img');

    if (lightbox && galleryImages.length > 0) {
        galleryImages.forEach(img => {
            img.parentElement.addEventListener('click', () => {
                lightbox.style.display = 'flex';
                setTimeout(() => {
                    lightbox.classList.add('active');
                    lightboxImg.src = img.src;
                }, 10);
            });
        });

        const closeLightbox = () => {
            lightbox.classList.remove('active');
            setTimeout(() => {
                lightbox.style.display = 'none';
                lightboxImg.src = '';
            }, 400); // Syncs with CSS opacity timing
        }

        if(closeBtn) closeBtn.addEventListener('click', closeLightbox);
        
        lightbox.addEventListener('click', (e) => {
            if (e.target !== lightboxImg && e.target !== closeBtn) closeLightbox();
        });

        document.addEventListener('keydown', (e) => {
            if(e.key === "Escape" && lightbox.classList.contains('active')) closeLightbox();
        });
    }

    // 8. Contact Form WhatsApp Auto-Route Logic
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const contactMsg = document.getElementById('message').value;
            
            const waNumber = '233555777025';
            const textContent = encodeURIComponent(`Hello, my name is ${name}.\n\n${contactMsg}`);
            const waURL = `https://wa.me/${waNumber}?text=${textContent}`;
            
            window.open(waURL, '_blank');
        });
    }
});
