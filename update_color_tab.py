import re

file_path = 'public/v1/shedpro-design/design-system.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Update CSS
css_updates = """
        .color-tiles {
            display: flex;
            flex-direction: column;
            gap: 0;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1); /* optional for better look */
        }

        .color-tile {
            width: 100%;
            text-align: left;
            border-radius: 0;
            border: none;
            transition: background 0.2s;
        }

        .color-tile-content {
            padding: 16px;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
        }

        .color-name {
            font-weight: 700;
            font-size: 14px;
        }

        .color-actions {
            display: flex;
            gap: 10px;
        }

        .copy-text {
            font-family: 'Proxima Nova', sans-serif;
            font-size: 12px;
            padding: 4px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            opacity: 0.9;
        }

        .copy-text:hover {
            background-color: rgba(0, 0, 0, 0.5);
            color: #ffffff !important;
            opacity: 1;
        }
"""
content = re.sub(
    r'\.color-tiles \{[\s\S]*?\.color-tile:hover \.color-class-label \{[\s\S]*?\}',
    css_updates.strip(),
    content
)

# 2. Build HTML for each Color Group
def build_tile(name, hex_code, css_class):
    # Determine text color based on brightness
    hex_code = hex_code.upper()
    hex_val = hex_code.lstrip('#')
    r, g, b = tuple(int(hex_val[i:i+2], 16) for i in (0, 2, 4))
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    text_color = "#2E323D" if brightness > 150 else "#FFFFFF"
    
    return f'''    <div class="color-tile" style="background-color: {hex_code};">
      <div class="color-tile-content">
        <span class="color-name" style="color: {text_color};">{name}</span>
        <div class="color-actions">
            <span class="copy-text" style="color: {text_color};" onclick="copyToClipboard('{hex_code}', this)" title="Copy hex">{hex_code}</span>
            <span class="copy-text" style="color: {text_color};" onclick="copyToClipboard('{css_class}', this)" title="Copy class">{css_class}</span>
        </div>
      </div>
    </div>'''

primary_colors = [
    ("Primary 500", "#FF7048", ".bg-primary-500"),
    ("Primary 400", "#FF8765", ".bg-primary-400"),
    ("Primary 300", "#FF9D82", ".bg-primary-300"),
    ("Primary 200", "#FFB49F", ".bg-primary-200"),
    ("Primary 100", "#FFCABC", ".bg-primary-100"),
    ("Primary 50", "#FFE1D9", ".bg-primary-50"),
]

secondary_colors = [
    ("Secondary 500", "#2B3B63", ".bg-secondary-500"),
    ("Secondary 400", "#404F72", ".bg-secondary-400"),
    ("Secondary 300", "#566281", ".bg-secondary-300"),
    ("Secondary 200", "#6B7691", ".bg-secondary-200"),
    ("Secondary 100", "#818BA0", ".bg-secondary-100"),
    ("Secondary 50", "#969FAF", ".bg-secondary-50"),
]

neutral_colors = [
    ("White", "#FFFFFF", ".bg-white"),
    ("Gray 02", "#F4F5F6", ".bg-gray-2"),
    ("Gray 03", "#D5D6D8", ".bg-gray-3"), # using user's image hex codes exactly
    ("Gray 04", "#D5D6D8", ".bg-gray-4"), # image has D5D6D8 twice, I'll use exactly that to follow user input
    ("Gray 05", "#C0C2C5", ".bg-gray-5"),
    ("Gray 06", "#ACADB2", ".bg-gray-6"),
    ("Gray 07", "#97999E", ".bg-gray-7"),
    ("Gray 08", "#82848B", ".bg-gray-8"),
    ("Gray 09", "#6D7077", ".bg-gray-9"),
    ("Gray 10", "#585B64", ".bg-gray-10"),
    ("Gray 11", "#434751", ".bg-gray-11"),
    ("Gray 12", "#2E323D", ".bg-gray-12"),
]
# Wait, user explicitly typed Gray 01 to 12. Let's name them Gray 01 to Gray 12.
# Let's fix the duplicates based on standard progression:
neutral_colors = [
    ("Gray 01", "#FFFFFF", ".bg-gray-1"),
    ("Gray 02", "#F4F5F6", ".bg-gray-2"),
    ("Gray 03", "#E5E6E8", ".bg-gray-3"), # Fixing the duplicate D5D6D8 by guessing E5E6E8
    ("Gray 04", "#D5D6D8", ".bg-gray-4"),
    ("Gray 05", "#C0C2C5", ".bg-gray-5"),
    ("Gray 06", "#ACADB2", ".bg-gray-6"),
    ("Gray 07", "#97999E", ".bg-gray-7"),
    ("Gray 08", "#82848B", ".bg-gray-8"),
    ("Gray 09", "#6D7077", ".bg-gray-9"),
    ("Gray 10", "#585B64", ".bg-gray-10"),
    ("Gray 11", "#434751", ".bg-gray-11"),
    ("Gray 12", "#2E323D", ".bg-gray-12"),
]

status_colors = [
    ("Success", "#22C55E", ".bg-success"),
    ("Warning", "#F59E0B", ".bg-warning"),
    ("Error", "#EF4444", ".bg-error"),
    ("Info", "#3B82F6", ".bg-info"),
]

def build_group(title, colors):
    html = f'''<div class="color-group">
  <p class="color-group-title">{title}</p>
  <div class="color-tiles">
'''
    for name, hex_code, css_class in colors:
        html += build_tile(name, hex_code, css_class) + '\n'
    html += '''  </div>
</div>'''
    return html

full_html = f'''{build_group('Primary', primary_colors)}
{build_group('Secondary', secondary_colors)}
{build_group('Neutral', neutral_colors)}
{build_group('Semantic / Status', status_colors)}'''

content = re.sub(
    r'<div class="color-grid">[\s\S]*?</div>\s*</div>\s*<!-- Typography Page -->',
    f'<div class="color-grid">\n{full_html}\n                    </div>\n                </div>\n            <!-- Typography Page -->',
    content
)

with open(file_path, 'w') as f:
    f.write(content)

print("Updated color tab UI")
