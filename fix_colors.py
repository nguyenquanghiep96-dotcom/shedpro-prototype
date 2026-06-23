import re

file_path = 'public/v1/shedpro-design/design-system.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Update CSS
css_updates = """
        .color-tiles {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .color-tile {
            width: 100%;
            text-align: left;
            border-radius: 0;
            border: none;
            transition: background 0.2s;
        }

        .color-tiles .color-tile:first-child {
            border-radius: 10px 10px 0 0;
        }

        .color-tiles .color-tile:last-child {
            border-radius: 0 0 10px 10px;
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
            font-family: 'Proxima Nova', 'Montserrat', sans-serif;
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
    r'\.color-tiles \{[\s\S]*?\.copy-text:hover \{[\s\S]*?\}',
    css_updates.strip(),
    content
)

# 2. Add Font Fallback
if "fonts.googleapis.com" not in content:
    content = content.replace('<style>', '<style>\n        @import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap");')

content = content.replace("'Proxima Nova', sans-serif", "'Proxima Nova', 'Montserrat', sans-serif")

# 3. Rebuild HTML
def build_tile(name, hex_code, css_class):
    hex_code = hex_code.upper()
    hex_val = hex_code.lstrip('#')
    r, g, b = tuple(int(hex_val[i:i+2], 16) for i in (0, 2, 4))
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    text_color = "#2E323D" if brightness > 150 else "#FFFFFF"
    
    border_style = ' border: 1px solid #E0E0E0;' if hex_code == '#FFFFFF' else ''
    
    return f'''    <div class="color-tile" style="background-color: {hex_code};{border_style}">
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
    ("Gray 01", "#FFFFFF", ".bg-gray-1"),
    ("Gray 02", "#F4F5F6", ".bg-gray-2"),
    ("Gray 03", "#E5E6E8", ".bg-gray-3"),
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
{build_group('Neutral (Grays)', neutral_colors)}
{build_group('Semantic / Status', status_colors)}'''

start_marker = '<div class="color-grid">'
end_marker = '<div id="tab-typography" class="page">'

idx_start = content.find(start_marker)
idx_end = content.find(end_marker)

if idx_start != -1 and idx_end != -1:
    new_html = f'''<div class="color-grid">
{full_html}
                    </div>
                </div>
                {end_marker}'''
    content = content[:idx_start] + new_html + content[idx_end + len(end_marker):]

with open(file_path, 'w') as f:
    f.write(content)

print("Updated HTML and CSS for colors")
