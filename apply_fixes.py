from bs4 import BeautifulSoup

def apply_fixes(file_path):
    with open(file_path, 'r') as f:
        html = f.read()
        
    # Fix 3: Change Location white box removal
    # The JS is in the HTML text
    old_css = """cl.css({
                'position': 'absolute',
                'top': '20px',
                'left': '50%',
                'transform': 'translateX(-50%)',
                'z-index': '100',
                'background': 'rgba(255,255,255,0.8)',
                'padding': '8px 12px',
                'border-radius': '6px',
                'box-shadow': '0 2px 4px rgba(0,0,0,0.1)'
            });"""
    new_css = """cl.css({
                'position': 'absolute',
                'top': '20px',
                'left': '50%',
                'transform': 'translateX(-50%)',
                'z-index': '100'
            });"""
    html = html.replace(old_css, new_css)
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Fix 1: Rename Premium Shed to Garden Shed in the Style Tab
    style_tab = soup.find('ul', class_='ssb-shed-options ssb-type-shedpro')
    if style_tab:
        for li in style_tab.find_all('li'):
            name_div = li.find('div', class_='name')
            if name_div and 'Premium Shed' in name_div.text:
                name_div.string = name_div.text.replace('Premium Shed', 'Garden Shed')
                
    # Fix 2: Add ic-arrow-down to Width x Length (ft) dropdown
    sizes_dropdown = soup.find('div', id='ssb-sizes')
    if sizes_dropdown:
        # Check if already has icon
        if not sizes_dropdown.find('i', class_='ic-arrow-down'):
            icon = soup.new_tag('i', attrs={'class': 'icon ic-arrow-down', 'style': 'position: absolute; right: 10px; top: 50%; transform: translateY(-50%); pointer-events: none; width: 16px; height: 16px;'})
            sizes_dropdown.append(icon)
            sizes_dropdown['style'] = sizes_dropdown.get('style', '') + '; position: relative;'
            
    with open(file_path, 'w') as f:
        f.write(str(soup))

apply_fixes('public/v1/shedpro-design/product/garden-shed/index.html')
print("Fixes applied successfully!")
