import re

file_path = 'public/v1/shedpro-design/design-system.html'

with open(file_path, 'r') as f:
    content = f.read()

if "--gray-0" not in content:
    root_vars = """            --gray-0: #2E323D;
            --gray-1: #5E6578;
            --gray-2: #959DB1;
            --gray-3: #BCBFC8;
            --gray-4: #EAECF0;
            --gray-5: #E0E0E0;
            --gray-6: #EDEDED;
            --gray-7: #F5F5F5;
            --white: #FFFFFF;
"""
    content = content.replace(':root {', ':root {\n' + root_vars)

def get_gray_html(number, hex_code):
    is_light = number == 'White' or (isinstance(number, int) and number >= 3)
    text_color = "#2E323D" if is_light else "#FFFFFF"
    
    if number == 'White':
        return f'''    <button class="color-tile" style="background-color: {hex_code}; border: 1px solid #E0E0E0;" onclick="copyToClipboard('.bg-white', this)" title="Copy .bg-white">
      <div class="color-tile-content">
        <span class="color-name" style="color: {text_color};">White</span>
        <span class="color-class-label" style="color: {text_color}; opacity: 0.8;">.bg-white</span>
      </div>
    </button>'''
    return f'''    <button class="color-tile" style="background-color: {hex_code};" onclick="copyToClipboard('.bg-gray-{number}', this)" title="Copy .bg-gray-{number}">
      <div class="color-tile-content">
        <span class="color-name" style="color: {text_color};">Gray {number}</span>
        <span class="color-class-label" style="color: {text_color}; opacity: 0.8;">.bg-gray-{number}</span>
      </div>
    </button>'''

neutral_html = f'''<div class="color-group">
  <p class="color-group-title">Neutral (Grays)</p>
  <div class="color-tiles">
{get_gray_html(0, '#2E323D')}
{get_gray_html(1, '#5E6578')}
{get_gray_html(2, '#959DB1')}
{get_gray_html(3, '#BCBFC8')}
{get_gray_html(4, '#EAECF0')}
{get_gray_html(5, '#E0E0E0')}
{get_gray_html(6, '#EDEDED')}
{get_gray_html(7, '#F5F5F5')}
{get_gray_html('White', '#FFFFFF')}
  </div>
</div>'''

content = re.sub(
    r'<div class="color-group">\s*<p class="color-group-title">Neutral</p>\s*<div class="color-tiles">[\s\S]*?</div>\s*</div>\s*<div class="color-group">',
    neutral_html + '\n<div class="color-group">',
    content
)

with open(file_path, 'w') as f:
    f.write(content)

print("Updated Neutral colors")
