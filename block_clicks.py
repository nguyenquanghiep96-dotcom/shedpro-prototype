from bs4 import BeautifulSoup

def block_clicks(file_path):
    with open(file_path, 'r') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Elements to block
    selectors = [
        '.ssb-share-model',
        '.wc-standard-checkout',
        '.wc-quick-checkout',
        '.single_add_to_cart_button',
        '.ssb-mobile-button-request-a-quote'
    ]
    
    for selector in selectors:
        elements = soup.select(selector)
        for el in elements:
            el['onclick'] = "event.stopPropagation(); event.preventDefault(); return false;"
            # Preserve hover but show not-allowed cursor if desired, but user just said "chỉ có trạng thái Hover, block nó để ko click được"
            # I will add cursor: not-allowed so it's clear it's blocked, but still triggers hover
            current_style = el.get('style', '')
            if 'cursor' not in current_style:
                el['style'] = current_style + ('; ' if current_style and not current_style.endswith(';') else '') + 'cursor: not-allowed !important;'
                
    # Check if there are any other share buttons
    
    with open(file_path, 'w') as f:
        f.write(str(soup))

block_clicks('public/v1/shedpro-design/product/garden-shed/index.html')
print("Click blocking applied!")
