from bs4 import BeautifulSoup
import re

def fix_canvas():
    print("Reading files...")
    with open('public/v1/shedpro-design/product/chalet/index.html', 'r') as f:
        chalet_html = f.read()
    with open('public/v1/shedpro-design/product/chalet/index.html', 'r') as f:
        chalet = BeautifulSoup(f.read(), 'html.parser')
        
    with open('public/v1/shedpro-design/product/chalet/original_chalet.html', 'r') as f:
        orig_html = f.read()
    with open('public/v1/shedpro-design/product/chalet/original_chalet.html', 'r') as f:
        orig = BeautifulSoup(f.read(), 'html.parser')
        
    print("Swapping canvas...")
    c_canvas = chalet.find(id='ssb-canvas')
    o_canvas = orig.find(id='ssb-canvas')
    if c_canvas and o_canvas:
        c_canvas.replace_with(o_canvas)
        
    # Write the modified soup back to string
    new_html = str(chalet)
    
    print("Swapping var ssb...")
    # Find var ssb in original
    orig_ssb_match = re.search(r'var\s+ssb\s*=\s*({[^;]+});', orig_html)
    if orig_ssb_match:
        orig_ssb = orig_ssb_match.group(0)
        # Find and replace in new_html
        new_html = re.sub(r'var\s+ssb\s*=\s*{[^;]+};', orig_ssb, new_html)
    else:
        print("var ssb not found in original!")
        
    with open('public/v1/shedpro-design/product/chalet/index.html', 'w') as f:
        f.write(new_html)
        
    print("Fixed canvas and var ssb!")

fix_canvas()
