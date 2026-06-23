import re

file_path = 'public/v1/shedpro-design/design-system.html'

with open(file_path, 'r') as f:
    content = f.read()

css_buttons = """
        .ds-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            border-radius: 6px;
            font-family: 'Proxima Nova', sans-serif;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            box-sizing: border-box;
            border: none;
        }
        .ds-btn .icon {
            width: 16px;
            height: 16px;
            background-color: currentColor;
            flex-shrink: 0;
        }

        /* Sizes */
        .ds-btn-32 {
            height: 32px;
            padding: 0 16px;
            font-size: 14px;
        }
        .ds-btn-36 {
            height: 36px;
            padding: 0 20px;
            font-size: 14px;
        }
        .ds-btn-44 {
            height: 44px;
            padding: 0 20px;
            font-size: 14px;
        }
        .ds-btn-48 {
            height: 48px;
            padding: 0 24px;
            font-size: 16px;
        }

        /* Styles */
        .ds-btn-primary {
            background-color: #ff7048; /* primary */
            color: #ffffff;
        }
        .ds-btn-primary:hover {
            background-color: #ff8765;
        }

        .ds-btn-secondary {
            background-color: #EDEDED;
            color: #5E6578;
        }
        .ds-btn-secondary:hover {
            background-color: #E2E2E2;
        }

        .ds-btn-outline {
            background-color: transparent;
            color: #5E6578;
            border: 1px solid #E0E0E0;
        }
        .ds-btn-outline:hover {
            background-color: #F8F9FA;
        }
"""

content = re.sub(
    r'\.ds-btn-primary \{[\s\S]*?\.ds-btn-primary \.icon \{[\s\S]*?\}',
    css_buttons.strip(),
    content
)

def build_size_row(size_class, size_label):
    html = f'''
                        <div style="margin-bottom: 24px;">
                            <h3 style="font-size: 14px; color: var(--gray-2); margin-bottom: 12px; font-weight: 700;">{size_label}</h3>
                            <div style="display: flex; gap: 40px; flex-wrap: wrap;">'''
    
    styles = [
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('outline', 'Outline')
    ]
    
    for style_class, style_name in styles:
        html += f'''
                                <div style="display: flex; flex-direction: column; gap: 12px;">
                                    <span style="font-size: 12px; color: var(--gray-3);">{style_name}</span>
                                    <div style="display: flex; gap: 16px; align-items: center;">
                                        <button class="ds-btn ds-btn-{size_class} ds-btn-{style_class}">
                                            Button
                                        </button>
                                        <button class="ds-btn ds-btn-{size_class} ds-btn-{style_class}">
                                            <i class="icon ic-add"></i>
                                            Button
                                        </button>
                                        <button class="ds-btn ds-btn-{size_class} ds-btn-{style_class}">
                                            Button
                                            <i class="icon ic-arrow_forward"></i>
                                        </button>
                                    </div>
                                </div>
'''
    html += '''
                            </div>
                        </div>'''
    return html

buttons_html = f'''                <div id="tab-buttons" class="page">
                    <h1 class="page-header">Buttons</h1>
                    
                    <div style="display: flex; flex-direction: column; gap: 32px; margin-top: 32px;">
                        {build_size_row('32', 'Size 32 (Height 32px, Font 14px, Padding 16px)')}
                        {build_size_row('36', 'Size 36 (Height 36px, Font 14px, Padding 20px)')}
                        {build_size_row('44', 'Size 44 (Height 44px, Font 14px, Padding 20px)')}
                        {build_size_row('48', 'Size 48 (Height 48px, Font 16px, Padding 24px)')}
                    </div>
                </div>'''

content = re.sub(
    r'<div id="tab-buttons" class="page">[\s\S]*?</div>\s*</div>\s*</main>',
    buttons_html + '\n            </div>\n        </main>',
    content
)

with open(file_path, 'w') as f:
    f.write(content)

print("Updated design-system.html with button variations")
