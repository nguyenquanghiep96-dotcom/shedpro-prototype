import re

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/product/garden-shed/index.html', 'r') as f:
    index_html = f.read()

# 1. Extract all <link rel="stylesheet"> from index.html
stylesheets = re.findall(r'<link rel="stylesheet".*?>', index_html)

# Clean up paths for design-system.html (which is one level up from product/garden-shed/)
# In index.html, paths are like href="../../../configurator-cdn..."
# In design-system.html, they should be href="../../configurator-cdn..."
new_stylesheets = []
for link in stylesheets:
    new_link = link.replace('href="../../../', 'href="../../')
    new_stylesheets.append(new_link)

# 2. Extract <style id="custom-theme-overrides">
style_block_match = re.search(r'<style id="custom-theme-overrides">.*?</style>', index_html, re.DOTALL)
style_block = style_block_match.group(0) if style_block_match else ""

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'r') as f:
    ds_html = f.read()

# Remove existing <link rel="stylesheet"> tags from design-system.html
ds_html = re.sub(r'<link rel="stylesheet".*?>\n?', '', ds_html)

# Insert the new stylesheets before <style type="text/css">
style_insert_pos = ds_html.find('<style type="text/css">')
if style_insert_pos != -1:
    ds_html = ds_html[:style_insert_pos] + '\n'.join(new_stylesheets) + '\n\t' + ds_html[style_insert_pos:]

# Remove existing <style id="custom-theme-overrides"> if any
ds_html = re.sub(r'<style id="custom-theme-overrides">.*?</style>', '', ds_html, flags=re.DOTALL)

# Insert the style block before </head>
head_end_pos = ds_html.find('</head>')
if head_end_pos != -1:
    ds_html = ds_html[:head_end_pos] + '\n' + style_block + '\n' + ds_html[head_end_pos:]

# Also update the body classes to match index.html to ensure CSS scope matches
body_match = re.search(r'<body class="(.*?)">', index_html)
if body_match:
    index_body_classes = body_match.group(1)
    ds_html = re.sub(r'<body class=".*?">', f'<body class="{index_body_classes}">', ds_html)

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'w') as f:
    f.write(ds_html)

print("Styles synchronized.")
