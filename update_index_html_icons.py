import re

file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Add link to head
if 'assets/icons/icons.css' not in content:
    content = content.replace('</title>', '</title>\n    <link rel="stylesheet" href="../../assets/icons/icons.css">')

# 2. Replace Save and Reset buttons innerHTML
content = re.sub(r'(<button[^>]*class="[^"]*ssb-save-model[^"]*"[^>]*>).*?(</button>)', r'\1<i class="icon ic-saved" style="margin-right: 6px;"></i>Save\2', content)
content = re.sub(r'(<button[^>]*class="[^"]*ssb-reset-btn[^"]*"[^>]*>).*?(</button>)', r'\1<i class="icon ic-reset" style="margin-right: 6px;"></i>Reset\2', content)

# 3. Replace inline SVGs
# Center items
center_item_svg = r'<svg[^>]*class="shedpro-icon"[^>]*>.*?<\/svg>'
content = re.sub(center_item_svg, '<i class="icon ic-center-items"></i>', content, flags=re.DOTALL)

# Center items in button
content = re.sub(r'<svg width="16" height="16" viewBox="0 0 24 24" fill="none"[^>]*>.*?<\/svg>', '<i class="icon ic-center-items"></i>', content, flags=re.DOTALL)

# Edit Shed
content = re.sub(r'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"[^>]*>.*?<\/svg>', '<i class="icon ic-edit-shed"></i>', content, flags=re.DOTALL)

# Cart
content = re.sub(r'<svg[^>]*class="lucide lucide-shopping-cart"[^>]*>.*?<\/svg>', '<i class="icon ic-cart"></i>', content, flags=re.DOTALL)

# Plus circle
content = re.sub(r'<svg[^>]*class="lucide lucide-plus-circle"[^>]*>.*?<\/svg>', '<i class="icon ic-plus-circle"></i>', content, flags=re.DOTALL)

# Close (lucide-x)
content = re.sub(r'<svg[^>]*class="lucide lucide-x"[^>]*>.*?<\/svg>', '<i class="icon ic-close"></i>', content, flags=re.DOTALL)

# Eye (lucide-eye)
content = re.sub(r'<svg[^>]*class="lucide lucide-eye"[^>]*>.*?<\/svg>', '<i class="icon ic-center-items"></i>', content, flags=re.DOTALL)


with open(file_path, 'w') as f:
    f.write(content)

print("Updated index.html!")
