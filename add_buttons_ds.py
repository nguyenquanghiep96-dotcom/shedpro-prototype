import re

file_path = 'public/v1/shedpro-design/design-system.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Font Family
content = content.replace("font-family: monospace;", "font-family: 'Proxima Nova', sans-serif;")

# 2. Add Buttons CSS
css_buttons = """
        .ds-btn-primary {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background-color: #ff7048; /* bg-primary-500 */
            color: #ffffff;
            border: none;
            border-radius: 6px;
            padding: 10px 16px;
            font-size: 14px;
            font-weight: 700;
            font-family: 'Proxima Nova', sans-serif;
            cursor: pointer;
            transition: background-color 0.2s ease;
        }
        .ds-btn-primary:hover {
            background-color: #ff8765; /* bg-primary-400 */
        }
        .ds-btn-primary .icon {
            width: 16px;
            height: 16px;
            background-color: currentColor;
        }
"""
if ".ds-btn-primary" not in content:
    content = content.replace("    </style>", css_buttons + "    </style>")

# 3. Update switchTab function to be generic
new_switchTab = """
        function switchTab(tabId, btn) {
            // Deactivate all menu items
            const menuItems = document.querySelectorAll('.menu-item');
            menuItems.forEach(item => item.classList.remove('active'));
            
            // Activate clicked
            btn.classList.add('active');

            // Hide all tabs
            const tabs = document.querySelectorAll('.content-area .page');
            tabs.forEach(tab => {
                if(tab.id.startsWith('tab-')) {
                    tab.classList.remove('active');
                }
            });

            // Show target
            document.getElementById('tab-' + tabId).classList.add('active');
        }
"""
content = re.sub(
    r'function switchTab\(tabId, btn\) \{[\s\S]*?\}\n',
    new_switchTab.strip() + '\n',
    content
)

# 4. Update the Buttons menu item
content = content.replace(
    '<button class="menu-item">Buttons</button>',
    '<button class="menu-item" onclick="switchTab(\'buttons\', this)">Buttons</button>'
)

# 5. Add the Buttons Tab Content
buttons_tab_html = """
                <div id="tab-buttons" class="page">
                    <h1 class="page-header">Buttons</h1>
                    
                    <div style="display: flex; gap: 40px; flex-wrap: wrap; align-items: flex-start; margin-top: 32px;">
                        
                        <!-- Primary: Right Icon -->
                        <div style="display: flex; flex-direction: column; gap: 16px;">
                            <span style="font-size: 14px; color: var(--gray-2); font-weight: 600;">Primary: Right Icon</span>
                            <button class="ds-btn-primary">
                                Button Text
                                <i class="icon ic-arrow_forward"></i>
                            </button>
                        </div>

                        <!-- Primary: Left Icon -->
                        <div style="display: flex; flex-direction: column; gap: 16px;">
                            <span style="font-size: 14px; color: var(--gray-2); font-weight: 600;">Primary: Left Icon</span>
                            <button class="ds-btn-primary">
                                <i class="icon ic-add"></i>
                                Button Text
                            </button>
                        </div>

                        <!-- Primary: No Icon -->
                        <div style="display: flex; flex-direction: column; gap: 16px;">
                            <span style="font-size: 14px; color: var(--gray-2); font-weight: 600;">Primary: No Icon</span>
                            <button class="ds-btn-primary">
                                Button Text
                            </button>
                        </div>

                    </div>
                </div>
"""
if 'id="tab-buttons"' not in content:
    # Insert right before the end of the content area
    content = content.replace(
        '            </div>\n        </main>',
        buttons_tab_html + '            </div>\n        </main>'
    )

with open(file_path, 'w') as f:
    f.write(content)

print("Updated design-system.html")
