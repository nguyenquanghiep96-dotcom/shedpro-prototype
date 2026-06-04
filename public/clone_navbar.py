import re

# Read index.html
with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/product/garden-shed/index.html', 'r') as f:
    index_html = f.read()

# Extract navbar from index.html
navbar_match = re.search(r'<!-- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* The Navbar Area \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* -->(.*?)<!-- #wrapper-navbar end -->', index_html, re.DOTALL)
if not navbar_match:
    print("Navbar not found in index.html")
    exit(1)

exact_navbar = '<!-- ******************* The Navbar Area ******************* -->' + navbar_match.group(1) + '<!-- #wrapper-navbar end -->'

# Read design-system.html
with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'r') as f:
    ds_html = f.read()

# Replace the existing navbar in design-system.html
# In design-system.html, the navbar starts with <!-- ******************* The Navbar Area ******************* --> and ends with <!-- #wrapper-navbar end -->
ds_html = re.sub(r'<!-- \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* The Navbar Area \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* -->.*?<!-- #wrapper-navbar end -->', exact_navbar, ds_html, flags=re.DOTALL)

# Write back to design-system.html
with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'w') as f:
    f.write(ds_html)

print("Navbar cloned exactly.")
