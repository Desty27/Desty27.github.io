#!/usr/bin/env python3
import os

pages = {
    'services': 'Services',
    'work': 'Our Works',
    'websites': 'Websites',
    'leads': 'Leads',
    'reviews': 'Reviews',
    'pricing': 'Pricing'
}

base_path = r'c:\Users\vikas\Downloads\Desty27.github.io'
pages_path = os.path.join(base_path, 'pages')

for page_name in pages.keys():
    old_file = os.path.join(pages_path, f'{page_name}.html')
    new_file = os.path.join(base_path, page_name, 'index.html')
    
    if os.path.exists(old_file):
        with open(old_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update asset paths: ../assets/ → ../../assets/
        content = content.replace('href="../assets/', 'href="../../assets/')
        content = content.replace('src="../assets/', 'src="../../assets/')
        
        # Update style and script paths
        content = content.replace('href="../style.css"', 'href="../../style.css"')
        content = content.replace('src="../script.js"', 'src="../../script.js"')
        
        # Update home page link
        content = content.replace('href="../index.html"', 'href="/"')
        
        # Update canonical URLs
        old_canonical = f'href="https://corner-stone.me/pages/{page_name}.html"'
        new_canonical = f'href="https://corner-stone.me/{page_name}/"'
        content = content.replace(old_canonical, new_canonical)
        
        # Update og:url
        old_og_url = f'<meta property="og:url" content="https://corner-stone.me/pages/{page_name}.html">'
        new_og_url = f'<meta property="og:url" content="https://corner-stone.me/{page_name}/">'
        content = content.replace(old_og_url, new_og_url)
        
        # Change same-directory links to root-relative links
        content = content.replace('href="services.html"', 'href="/services/"')
        content = content.replace('href="work.html"', 'href="/work/"')
        content = content.replace('href="websites.html"', 'href="/websites/"')
        content = content.replace('href="leads.html"', 'href="/leads/"')
        content = content.replace('href="reviews.html"', 'href="/reviews/"')
        content = content.replace('href="pricing.html"', 'href="/pricing/"')
        
        # Write to new location
        os.makedirs(os.path.dirname(new_file), exist_ok=True)
        with open(new_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✓ Migrated {page_name}.html → {page_name}/index.html')

print('\nAll pages migrated successfully!')
