import os
import shutil
import re

base_dir = r'c:\Users\DELL\OneDrive\Desktop\HTML FILES\Soul-Restaurant\restaurant-website'

# 1. Rename Images
image_map = {
    '2025-09-21.jpg': 'hero-bg.jpg',
    '2025-09-21 (1).jpg': 'cta-bg.jpg',
    'unnamed.jpg': 'about-hero-bg.jpg',
    'unnamed (1).jpg': 'restaurant-interior.jpg',
    'unnamed (2).jpg': 'comfort-food-bg.jpg',
    'unnamed (3).jpg': 'menu-hero-bg.jpg',
    'unnamed (4).jpg': 'grilled-salmon.jpg',
    'unnamed (5).jpg': 'chicken-pizza.jpg',
    'unnamed (6).jpg': 'beef-steak.jpg',
    'unnamed (7).jpg': 'tropical-cocktail.jpg',
    'unnamed (8).jpg': 'chocolate-lava-cake.jpg',
    'unnamed (9).jpg': 'gallery-hero-bg.jpg',
    'unnamed (10).jpg': 'gallery-interior.jpg',
    'unnamed (11).jpg': 'gallery-signature-dish.jpg',
    'unnamed (12).jpg': 'gallery-cocktails.jpg',
}

img_dir = os.path.join(base_dir, 'assets', 'images')
for old, new in image_map.items():
    old_path = os.path.join(img_dir, old)
    new_path = os.path.join(img_dir, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)

# 2. Delete sections folder
sections_dir = os.path.join(base_dir, 'sections')
if os.path.exists(sections_dir):
    shutil.rmtree(sections_dir)

# 3. Process HTML files
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

footer_content = '''    <!-- FOOTER -->
    <footer data-aos="fade-in" data-aos-duration="1200">
        <div class="footer-container">
            <div class="footer-brand">
                <h3 class="mb-3" style="color:var(--color-gold);">Soul Restaurant and Bar</h3>
                <p>Taste the perfection in every bite.</p>
                <div class="social-icons">
                    <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook">Fb</a>
                    <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram">Ig</a>
                    <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" aria-label="Twitter">Tw</a>
                </div>
            </div>
            <div class="footer-hours">
                <h4>Opening Hours</h4>
                <ul>
                    <li><strong>Saturday:</strong> 11am – 12am</li>
                    <li><strong>Sun – Thu:</strong> 11am – 11pm</li>
                    <li><strong>Friday:</strong> 11am – 12am</li>
                </ul>
            </div>
            <div class="footer-contact">
                <h4>Contact Details</h4>
                <p>📞 <a href="tel:+233555777025">055 577 7025</a></p>
                <p>💬 <a href="https://wa.me/233555777025?text=Hello%20I%20want%20to%20order" target="_blank" rel="noopener noreferrer">WhatsApp Us</a></p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Soul Restaurant and Bar. All rights reserved.</p>
        </div>
    </footer>'''

for f in html_files:
    path = os.path.join(base_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace image names
    for old, new in image_map.items():
        content = content.replace(f'assets/images/{old}', f'assets/images/{new}')
        content = content.replace(f'assets/images/{old.replace(" ", "%20")}', f'assets/images/{new}')
    
    # Add meta description and favicon
    meta_tags = '''    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Soul Restaurant and Bar offers a premium dining experience with delicious meals, great vibes, and exceptional service in Accra, Ghana.">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍽️</text></svg>">'''
    content = re.sub(r'<meta name="viewport" content="width=device-width, initial-scale=1.0">', meta_tags, content)
    
    # Fix tel links
    content = content.replace('tel:0555777025', 'tel:+233555777025')
    
    # Fix WhatsApp target blank noopener
    content = re.sub(r'target="_blank"(?!\s+rel="noopener noreferrer")', 'target="_blank" rel="noopener noreferrer"', content)
    
    # Fix aria-label on mobile menu
    content = content.replace('<div class="menu-toggle" id="mobile-menu">', '<div class="menu-toggle" id="mobile-menu" aria-label="Toggle navigation" role="button" tabindex="0">')
    
    # Replace footer
    content = re.sub(r'<footer.*?</footer>', footer_content, content, flags=re.DOTALL)
    
    # Menu grouping
    if f == 'menu.html':
        content = re.sub(r'<div class="menu-filters".*?</div>', '', content, flags=re.DOTALL)
        
        mains = '''<h2 class="section-title text-gold mt-5 mb-4" style="margin-top: 50px;">Main Meals</h2>
                <div class="grid-card-layout">
                    <div class="menu-card glass-card-solid" data-aos="fade-up" data-aos-delay="100">
                        <div class="img-wrapper menu-img"><img src="assets/images/grilled-salmon.jpg" alt="Grilled Salmon" loading="lazy"></div>
                        <div class="card-content">
                            <h3>Grilled Salmon</h3>
                            <p class="desc">Fresh salmon grilled with garlic butter and herbs.</p>
                            <a href="https://wa.me/233555777025?text=Hello%20I%20want%20to%20order%20Grilled%20Salmon" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm w-100 hover-glow">Order on WhatsApp</a>
                        </div>
                    </div>

                    <div class="menu-card glass-card-solid" data-aos="fade-up" data-aos-delay="200">
                        <div class="img-wrapper menu-img"><img src="assets/images/chicken-pizza.jpg" alt="Pizza" loading="lazy"></div>
                        <div class="card-content">
                            <h3>Supreme Chicken Pizza</h3>
                            <p class="desc">Hand-tossed crust packed with mozzarella and chicken.</p>
                            <a href="https://wa.me/233555777025?text=Hello%20I%20want%20to%20order%20Supreme%20Chicken%20Pizza" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm w-100 hover-glow">Order on WhatsApp</a>
                        </div>
                    </div>

                    <div class="menu-card glass-card-solid" data-aos="fade-up" data-aos-delay="300">
                        <div class="img-wrapper menu-img"><img src="assets/images/beef-steak.jpg" alt="Steak" loading="lazy"></div>
                        <div class="card-content">
                            <h3>Premium Beef Steak</h3>
                            <p class="desc">Tender pan-seared steak coated in a peppercorn sauce.</p>
                            <a href="https://wa.me/233555777025?text=Hello%20I%20want%20to%20order%20Premium%20Beef%20Steak" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm w-100 hover-glow">Order on WhatsApp</a>
                        </div>
                    </div>
                </div>'''

        drinks = '''<h2 class="section-title text-gold mt-5 mb-4" style="margin-top: 50px;">Drinks</h2>
                <div class="grid-card-layout">
                    <div class="menu-card glass-card-solid" data-aos="fade-up" data-aos-delay="100">
                        <div class="img-wrapper menu-img"><img src="assets/images/tropical-cocktail.jpg" alt="Cocktail" loading="lazy"></div>
                        <div class="card-content">
                            <h3>Tropical Cocktail</h3>
                            <p class="desc">A refreshing blend of mango, pineapple, and premium spirits.</p>
                            <a href="https://wa.me/233555777025?text=Hello%20I%20want%20to%20order%20Tropical%20Cocktail" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm w-100 hover-glow">Order on WhatsApp</a>
                        </div>
                    </div>
                </div>'''

        desserts = '''<h2 class="section-title text-gold mt-5 mb-4" style="margin-top: 50px;">Desserts</h2>
                <div class="grid-card-layout">
                    <div class="menu-card glass-card-solid" data-aos="fade-up" data-aos-delay="100">
                        <div class="img-wrapper menu-img"><img src="assets/images/chocolate-lava-cake.jpg" alt="Cake" loading="lazy"></div>
                        <div class="card-content">
                            <h3>Chocolate Lava Cake</h3>
                            <p class="desc">A warm rich chocolate cake served with vanilla ice cream.</p>
                            <a href="https://wa.me/233555777025?text=Hello%20I%20want%20to%20order%20Chocolate%20Lava%20Cake" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm w-100 hover-glow">Order on WhatsApp</a>
                        </div>
                    </div>
                </div>'''
        
        content = re.sub(r'<div class="grid-card-layout">.*?</div>\s*</div>\s*</section>', f'{mains}\n{drinks}\n{desserts}\n</div>\n</section>', content, flags=re.DOTALL)
        
    # Open Graph meta tags on index.html
    if f == 'index.html':
        og_tags = '''    <meta property="og:title" content="Soul Restaurant and Bar | Premium Dining">
    <meta property="og:description" content="Experience great food, great vibes, and unforgettable moments at Soul Restaurant and Bar in Accra, Ghana.">
    <meta property="og:image" content="assets/images/hero-bg.jpg">
    <meta property="og:url" content="https://soulrestaurant.example.com">'''
        content = content.replace('<title>', f'{og_tags}\n    <title>')

    # Contact labels
    if f == 'contact.html':
        content = content.replace('<label>Name</label>', '<label for="name">Name</label>')
        content = content.replace('<label>Phone / Email</label>', '<label for="contact">Phone / Email</label>')
        content = content.replace('<label>Message</label>', '<label for="message">Message</label>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
