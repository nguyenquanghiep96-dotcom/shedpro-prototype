import re

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/product/garden-shed/index.html', 'r') as f:
    index_html = f.read()

# Extract navbar
navbar_match = re.search(r'<!-- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* The Navbar Area \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* -->(.*?)<!-- #wrapper-navbar end -->', index_html, re.DOTALL)
if not navbar_match:
    print("Navbar not found in index.html")
    exit(1)

navbar_content = '<!-- ******************* The Navbar Area ******************* -->' + navbar_match.group(1) + '<!-- #wrapper-navbar end -->'

# Adjust links for design-system.html
navbar_content = navbar_content.replace('href="../../design-system.html"', 'href="#"')
# Add link back to prototype
prototype_link = '<li class="nav-item"><a class="nav-link" href="product/garden-shed/index.html">Prototype 3D</a></li>'
navbar_content = navbar_content.replace('<li class="nav-item"><a class="nav-link" href="#">Design System</a></li>', prototype_link + '<li class="nav-item active"><a class="nav-link" href="#">Design System</a></li>')

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'r') as f:
    ds_html = f.read()

# Replace the existing nav in design system
ds_html = re.sub(r'<nav class="navbar.*?</nav>', navbar_content, ds_html, flags=re.DOTALL)

# Re-layout the Colors section
# Find the start of Colors section
colors_start_idx = ds_html.find('<h2 class="ds-title">1. Colors</h2>')
if colors_start_idx != -1:
    colors_end_idx = ds_html.find('</div>\n\n\t<div class="ds-section">\n\t\t<h2 class="ds-title">2. Typography</h2>')
    if colors_end_idx != -1:
        colors_content = ds_html[colors_start_idx:colors_end_idx]
        
        # We need to wrap Primary, Secondary, Grays in a flex row
        # They start with <h4 class="mb-3">
        new_colors_content = colors_content.replace('<h4 class="mb-3">', '<div>\n<h4 class="mb-3">')
        new_colors_content = new_colors_content.replace('</div>\n\n        <div>\n<h4 class="mb-3">Secondary</h4>', '</div>\n</div>\n\n        <div>\n<h4 class="mb-3">Secondary</h4>')
        new_colors_content = new_colors_content.replace('</div>\n\n        <div>\n<h4 class="mb-3">Support Color (Grays)</h4>', '</div>\n</div>\n\n        <div>\n<h4 class="mb-3">Support Color (Grays)</h4>')
        new_colors_content = new_colors_content + '</div>'
        
        # wrap the whole thing inside a flex container
        # The first <h4> is after <h2 class="ds-title">1. Colors</h2>
        new_colors_content = new_colors_content.replace('<h2 class="ds-title">1. Colors</h2>\n        <div>', '<h2 class="ds-title">1. Colors</h2>\n<div class="d-flex flex-wrap" style="gap: 40px;">\n        <div>')
        # Close the flex container at the end
        new_colors_content += '\n</div>'
        
        ds_html = ds_html[:colors_start_idx] + new_colors_content + ds_html[colors_end_idx:]

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'w') as f:
    f.write(ds_html)

print("Design System updated successfully.")
