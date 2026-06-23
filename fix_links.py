from bs4 import BeautifulSoup
import re

def fix_links(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    style_tab = soup.find('ul', class_='ssb-shed-options ssb-type-shedpro')
    if style_tab:
        for li in style_tab.find_all('li'):
            name = li.text.strip()
            if 'Premium Shed' in name or 'Garden Shed' in name:
                li['data-href'] = '../garden-shed/index.html'
            elif 'Chalet' in name:
                li['data-href'] = '../chalet/index.html'
                
    with open(file_path, 'w') as f:
        f.write(str(soup))
        
fix_links('public/v1/shedpro-design/product/garden-shed/index.html')
fix_links('public/v1/shedpro-design/product/chalet/index.html')
print("Links updated to local paths!")
