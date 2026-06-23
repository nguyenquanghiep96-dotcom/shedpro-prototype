import os
import re

html_path = 'public/v1/shedpro-design/design-system.html'
icons_dir = 'public/v1/shedpro-design/assets/icons/raw'

with open(html_path, 'r') as f:
    content = f.read()

# 1. Inject icons.css
if 'assets/icons/icons.css' not in content:
    content = content.replace('</head>', '    <link rel="stylesheet" href="assets/icons/icons.css">\n</head>')

# 2. Generate new icons grid HTML
files = [f for f in os.listdir(icons_dir) if f.endswith('.svg')]
files.sort()

icons_html = ""
for file in files:
    name = file.replace('.svg', '')
    display_name = name.replace('ic-', '').replace('-', ' ').replace('_', ' ').title()
    snippet = f'<i class="icon {name}"></i>'
    snippet_encoded = snippet.replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    
    icons_html += f'''
<button class="icon-card" data-name="{name}" data-snippet="{snippet_encoded}" onclick="copyToClipboard(this.getAttribute('data-snippet'), this)">
  {snippet}
  <span class="icon-label">{display_name}</span>
</button>'''

# Replace the content inside <div class="icons-grid" id="icons-grid"> ... </div>
import re
pattern = r'(<div class="icons-grid" id="icons-grid">)(.*?)(</div>)'
content = re.sub(pattern, rf'\1{icons_html}\n                    \3', content, flags=re.DOTALL)

with open(html_path, 'w') as f:
    f.write(content)

print("design-system.html updated!")
