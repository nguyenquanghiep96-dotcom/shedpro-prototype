import re

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'r') as f:
    ds_html = f.read()

# 1. Add Navbar custom CSS to <style type="text/css">
css_to_add = """
        /* Header Customizations */
        .navbar {
            background-color: #FFFFFF !important;
            padding: 10px 20px;
        }
        .navbar .nav-link {
            color: var(--gray-1, #5E6578) !important;
        }
        .navbar .nav-link:hover {
            color: var(--primary, #FF7048) !important;
        }
"""
if "/* Header Customizations */" not in ds_html:
    ds_html = ds_html.replace('</style>', css_to_add + '</style>')

# 2. Fix layout of Colors section
colors_start_idx = ds_html.find('<h2 class="ds-title">1. Colors</h2>')
colors_end_idx = ds_html.find('</div>\n\n\t<div class="ds-section">\n\t\t<h2 class="ds-title">2. Typography</h2>')

if colors_start_idx != -1 and colors_end_idx != -1:
    colors_content = ds_html[colors_start_idx:colors_end_idx]
    
    # It currently has: <div class="d-flex flex-wrap" style="gap: 40px;">
    # Let's replace the outer wrapper with a bootstrap row.
    new_colors = colors_content.replace('<div class="d-flex flex-wrap" style="gap: 40px;">\n        <div>', '<div class="row">\n        <div class="col-lg-3 col-md-6 mb-4">')
    
    # Replace other dividers
    new_colors = new_colors.replace('</div>\n</div>\n\n        <div>\n<h4 class="mb-3">Secondary</h4>', '</div>\n        <div class="col-lg-3 col-md-6 mb-4">\n<h4 class="mb-3">Secondary</h4>')
    new_colors = new_colors.replace('</div>\n</div>\n\n        <div>\n<h4 class="mb-3">Support Color (Grays)</h4>', '</div>\n        <div class="col-lg-6 col-md-12 mb-4">\n<h4 class="mb-3">Support Color (Grays)</h4>')
    
    # We don't need to change the end wrapper because it's just </div>
    
    ds_html = ds_html[:colors_start_idx] + new_colors + ds_html[colors_end_idx:]

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'w') as f:
    f.write(ds_html)

print("Fixes applied.")
