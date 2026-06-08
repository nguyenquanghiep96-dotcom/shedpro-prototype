import re

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/product/garden-shed/index.html', 'r') as f:
    html = f.read()

# 1. CSS for mobile logo
mobile_css = """
<style>
@media (max-width: 767px) {
    .navbar-brand { max-width: 70%; white-space: nowrap; }
    .navbar-brand svg { max-width: 110px; height: auto; }
    .navbar-brand span { font-size: 11px !important; }
}
</style>
</head>
"""
html = html.replace('</head>', mobile_css)

# 2. Add Pen icon to Edit Shed button
edit_btn_old = '<span id="mobile-custom-shed">Edit Shed</span>'
edit_btn_new = '<span id="mobile-custom-shed" style="display:inline-flex;align-items:center;justify-content:center;gap:6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/><path d="m15 5 4 4"/></svg>Edit Shed</span>'
html = html.replace(edit_btn_old, edit_btn_new)

# 3. Add Center Icon to Center item button
center_btn_old = '<button id="center-item-button">Center Items</button>'
center_btn_new = '<button id="center-item-button" style="display:inline-flex;align-items:center;justify-content:center;gap:6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2.26 0H0V24H2.26V0Z" fill="currentColor"/><path d="M24 0H21.74V24H24V0Z" fill="currentColor"/><path d="M17.3901 2.15997H6.62012V21.85H17.3901V2.15997Z" fill="currentColor"/></svg>Center Items</button>'
html = html.replace(center_btn_old, center_btn_new)

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/product/garden-shed/index.html', 'w') as f:
    f.write(html)

print("UI fixes applied.")
