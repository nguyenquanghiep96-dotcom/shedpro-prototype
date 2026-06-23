from bs4 import BeautifulSoup
import re

def process_file(file_path):
    with open(file_path, 'r') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the span with "Premium Shed" or "Chalet" inside the options list
    target_span = soup.find('span', class_='ssb-option-name', string=re.compile(r'Premium Shed|Chalet'))
    if not target_span:
        print(f"Target span not found in {file_path}")
        return
        
    # Find the parent ul
    ul = target_span.find_parent('ul')
    if not ul:
        print(f"UL not found in {file_path}")
        return
        
    allowed_names = ['Premium Shed', 'Chalet', 'Tiny Home', 'Lean To', 'Aframe', 'Log Cabin', 'Garden Shed']
    
    for li in ul.find_all('li', class_='ssb-option'):
        name_span = li.find('span', class_='ssb-option-name')
        if not name_span:
            continue
            
        name = name_span.text.strip()
        if name not in allowed_names:
            print(f"Removing {name} from {file_path}")
            li.decompose() # Remove the element
            
    with open(file_path, 'w') as f:
        f.write(str(soup))
    print(f"Processed {file_path}")

process_file('public/v1/shedpro-design/product/garden-shed/index.html')
process_file('public/v1/shedpro-design/product/chalet/index.html')
