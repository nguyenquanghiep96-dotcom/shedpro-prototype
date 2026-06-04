import re

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'r') as f:
    ds_html = f.read()

# Fix the CSS paths
ds_html = ds_html.replace('href="../../configurator-cdn.shedpro.co', 'href="../configurator-cdn.shedpro.co')

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'w') as f:
    f.write(ds_html)

print("CSS paths fixed.")
