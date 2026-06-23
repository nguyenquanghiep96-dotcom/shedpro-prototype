from bs4 import BeautifulSoup
import re

def fix_style_tab(file_path):
    with open(file_path, 'r') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    style_tab = soup.find('ul', class_='ssb-shed-options ssb-type-shedpro')
    if style_tab:
        # We only want Premium Shed, Chalet, Aframe, Log Cabin
        allowed = ['Premium Shed', 'Garden Shed', 'Chalet', 'Aframe', 'Log Cabin', 'Logcabin']
        
        items_kept = []
        for li in style_tab.find_all('li', recursive=False):
            name_div = li.find('div', class_='name')
            if name_div:
                name = name_div.text.strip()
                
                # Check if it matches our allowed list
                keep = False
                for a in allowed:
                    if a.lower() in name.lower():
                        keep = True
                        break
                        
                if keep:
                    # If not Premium Shed (or Garden Shed), block click
                    if 'premium' not in name.lower() and 'garden' not in name.lower():
                        if 'data-href' in li.attrs:
                            del li['data-href']
                        # Add a style to block click
                        li['style'] = li.get('style', '') + '; cursor: not-allowed; pointer-events: none;'
                        # Make sure it's not active
                        li['class'] = [c for c in li.get('class', []) if c != 'active']
                    else:
                        # Make Premium Shed active
                        if 'active' not in li.get('class', []):
                            li['class'] = li.get('class', []) + ['active']
                            
                    items_kept.append(li)
                    
        # Clear the UL and append the kept items
        style_tab.clear()
        for item in items_kept:
            style_tab.append(item)
            
    with open(file_path, 'w') as f:
        f.write(str(soup))

fix_style_tab('public/v1/shedpro-design/product/garden-shed/index.html')
print("Fixed Style Tab to exactly 4 items with locked clicks!")
