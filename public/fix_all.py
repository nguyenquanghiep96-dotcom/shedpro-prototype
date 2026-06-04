import re

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'r') as f:
    ds_html = f.read()

# 1. Fix scrolling
if 'overflow-y: auto !important;' not in ds_html:
    scroll_css = "\n\t\tbody { overflow-y: auto !important; overflow-x: hidden !important; }\n"
    ds_html = ds_html.replace('<style type="text/css">', '<style type="text/css">' + scroll_css)

# 2. Fix Navbar Version 1 Link
ds_html = ds_html.replace('<a class="dropdown-item" href="#">Version 1</a>', '<a class="dropdown-item" href="product/garden-shed/index.html">Version 1</a>')
# Fix the active state for navbar if needed. The user wants identical, so it's fine.
# We also need to fix the dropdown toggle. Bootstrap dropdowns need jQuery/Popper, 
# but if it was working in index.html, it should work here if JS is included.
# Wait, did I include JS scripts in design-system.html? 
# The user said "khi click vào Version sẽ hiển thị dropdown version 1", this means it might not be opening!
# I will check and add bootstrap JS if missing at the end of body.

# 3. Add Favicon
favicon_tags = """
    <link rel="icon" href="/Favicon.png" sizes="32x32">
    <link rel="icon" href="/Favicon.png" sizes="192x192">
    <link rel="apple-touch-icon" href="/Favicon.png">
    <meta name="msapplication-TileImage" content="/Favicon.png">
"""
if '<link rel="icon"' not in ds_html:
    ds_html = ds_html.replace('</title>', '</title>\n' + favicon_tags)

# 4. Fix Colors Section CSS
# Update .color-box
ds_html = re.sub(r'\.color-box\s*{[^}]+}', 
    ".color-box {\n\t\t\twidth: 100px;\n\t\t\theight: 100px;\n\t\t\tborder-radius: 6px;\n\t\t\tdisplay: flex;\n\t\t\talign-items: center;\n\t\t\tjustify-content: center;\n\t\t\ttext-align: center;\n\t\t\tcolor: white;\n\t\t\tfont-weight: bold;\n\t\t\tfont-size: 13px;\n\t\t\ttext-shadow: 1px 1px 3px rgba(0,0,0,0.3);\n\t\t\tmargin-right: 15px;\n\t\t\tmargin-bottom: 15px;\n\t\t\ttransition: transform 0.2s ease;\n\t\t}", ds_html)

# Let's restore the Colors section HTML to a clean flex layout, removing the .row/.col grid I added.
colors_start_idx = ds_html.find('<h2 class="ds-title">1. Colors</h2>')
colors_end_idx = ds_html.find('</div>\n\n\t<div class="ds-section">\n\t\t<h2 class="ds-title">2. Typography</h2>')

if colors_start_idx != -1 and colors_end_idx != -1:
    # Rewrite the colors section HTML
    clean_colors = """<h2 class="ds-title">1. Colors</h2>

        <h4 class="mb-3">Primary</h4>
		<div class="d-flex flex-wrap mb-4" style="max-width: 960px;">
			<div class="color-box" style="background-color: var(--primary);">Original<br>#FF7048</div>
			<div class="color-box" style="background-color: var(--primary-hover);">Hover<br>#FF8765</div>
			<div class="color-box" style="background-color: var(--primary-light);">Light<br>#FFB7A3</div>
		</div>

        <h4 class="mb-3">Secondary</h4>
		<div class="d-flex flex-wrap mb-4" style="max-width: 960px;">
			<div class="color-box" style="background-color: var(--secondary);">Original<br>#2B3B63</div>
			<div class="color-box" style="background-color: var(--secondary-hover);">Hover<br>#556272</div>
			<div class="color-box" style="background-color: var(--secondary-dark);">Dark<br>#222F4F</div>
		</div>

        <h4 class="mb-3">Support Color (Grays)</h4>
		<div class="d-flex flex-wrap mb-4" style="max-width: 960px;">
			<div class="color-box" style="background-color: var(--gray-0);">Gray 0<br>#2E323D</div>
			<div class="color-box" style="background-color: var(--gray-1);">Gray 1<br>#5E6578</div>
			<div class="color-box" style="background-color: var(--gray-2);">Gray 2<br>#959DB1</div>
			<div class="color-box light-text" style="background-color: var(--gray-3);">Gray 3<br>#BCBFC8</div>
			<div class="color-box light-text" style="background-color: var(--gray-4);">Gray 4<br>#EAECF0</div>
			<div class="color-box light-text" style="background-color: var(--gray-5);">Gray 5<br>#E0E0E0</div>
			<div class="color-box light-text" style="background-color: var(--gray-6);">Gray 6<br>#EDEDED</div>
			<div class="color-box light-text" style="background-color: var(--gray-7);">Gray 7<br>#F5F5F5</div>
		</div>
"""
    ds_html = ds_html[:colors_start_idx] + clean_colors + ds_html[colors_end_idx:]


with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'w') as f:
    f.write(ds_html)

print("Done phase 1.")
