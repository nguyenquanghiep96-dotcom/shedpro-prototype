import re

def extract_css(source_path):
    with open(source_path, 'r') as f:
        content = f.read()
    
    # Extract <link rel="stylesheet" href="../../design-system.css">
    # Wait, in garden-shed/index.html, it might not exist yet? Let's check!
    # If not, we just hardcode the link.
    
    # Extract custom-theme-overrides
    match = re.search(r'(<style id="custom-theme-overrides">[\s\S]*?</style>)', content)
    overrides = match.group(1) if match else ''
    
    return overrides

def sync_file(file_path, is_chalet=False):
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update Change Location CSS
    # First, let's remove the old JS snippet we injected in apply_mvp_fixes.py
    # and replace the cl.css(...) part.
    old_css = """'position': 'absolute',
                'bottom': '20px',
                'left': '20px',"""
    new_css = """'position': 'absolute',
                'top': '20px',
                'left': '50%',
                'transform': 'translateX(-50%)',"""
    content = content.replace(old_css, new_css)
    
    # 2. Fix Style Tab items
    # Remove Alpine Chalet entirely
    content = re.sub(r'<li class="ssb-option[^>]*data-href="[^"]*alpine-chalet/"[\s\S]*?</li>', '', content)
    
    # Update the remaining disabled items: remove opacity:0.4, use pointer-events: none
    content = content.replace('style="opacity:0.4; cursor:not-allowed;"', 'style="pointer-events:none; cursor:not-allowed;"')

    if is_chalet:
        # Inject design-system.css and custom-theme-overrides
        overrides = extract_css('public/v1/shedpro-design/product/garden-shed/index.html')
        
        # Check if design-system.css is linked
        if 'href="../../design-system.css"' not in content:
            content = content.replace('</head>', '<link rel="stylesheet" href="../../design-system.css">\n</head>')
            
        if 'id="custom-theme-overrides"' not in content:
            content = content.replace('</head>', f'{overrides}\n</head>')
            
    with open(file_path, 'w') as f:
        f.write(content)

# Update Garden Shed
sync_file('public/v1/shedpro-design/product/garden-shed/index.html', is_chalet=False)

# Update Chalet
# Wait, for Chalet, if we already ran setup_chalet.py, it's missing the CSS.
sync_file('public/v1/shedpro-design/product/chalet/index.html', is_chalet=True)

print("Synchronized UI components successfully!")
