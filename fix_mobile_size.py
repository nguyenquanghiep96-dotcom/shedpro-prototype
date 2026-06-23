import re

file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# Fix the CSS for mobile-size-buttons to NOT have wrap constraint if it's too tight, wait...
# User: "Layout là dạng nằm ngang thay vì dọc, cứ rớt dòng nếu nhiều và quá khung."
# `flex-wrap: wrap;` does exactly this! But wait, previously I had `display: flex !important; flex-wrap: wrap;`. That is correct.
# Let's ensure it's `flex-direction: row`.

css_updates = """
/* Mobile Size Buttons */
@media (max-width: 768px) {
    #ssb-configurator-width-length .ssb-custom-select {
        display: none !important;
    }
    .mobile-size-buttons {
        display: flex !important;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
    }
    .mobile-size-btn {
        font-family: 'Proxima Nova', sans-serif;
        font-size: 14px;
        font-weight: 700;
        color: var(--gray-1);
        padding: 8px 20px;
        border-radius: 6px;
        border: 1px solid var(--gray-3);
        background: transparent;
        cursor: pointer;
        transition: all 0.2s;
    }
    .mobile-size-btn.active {
        border-color: var(--primary);
        color: var(--primary);
    }
    
    .mobile-customize-panel {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .mobile-customize-panel .mobile-panel-title {
        font-weight: 700;
        color: var(--primary);
        font-size: 14px;
    }
}
@media (min-width: 769px) {
    .mobile-size-buttons {
        display: none !important;
    }
}
"""

js_code = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    var select = document.getElementById('ssb-configurator-size-area');
    if (!select) return;
    
    // Remove existing if any
    var existing = document.querySelector('.mobile-size-buttons');
    if (existing) existing.remove();

    var container = document.createElement('div');
    container.className = 'mobile-size-buttons';
    
    var parentBlock = document.getElementById('ssb-configurator-width-length');
    if (parentBlock) {
        parentBlock.appendChild(container);
    }
    
    // Setup the header title element
    var mobilePanel = document.querySelector('.mobile-customize-panel');
    var titleSpan = null;
    if (mobilePanel) {
        // Clear text node "Customize Panel"
        mobilePanel.childNodes.forEach(function(node) {
            if (node.nodeType === 3 && node.nodeValue.trim().length > 0) {
                node.nodeValue = '';
            }
        });
        titleSpan = document.createElement('span');
        titleSpan.className = 'mobile-panel-title';
        var iconClose = mobilePanel.querySelector('.icon-close');
        if (iconClose) {
            mobilePanel.insertBefore(titleSpan, iconClose);
        } else {
            mobilePanel.appendChild(titleSpan);
        }
    }

    function renderButtons() {
        container.innerHTML = '';
        Array.from(select.options).forEach(function(opt) {
            var btn = document.createElement('button');
            btn.className = 'mobile-size-btn';
            if (opt.selected) {
                btn.classList.add('active');
                if (titleSpan) titleSpan.textContent = opt.text;
            }
            btn.textContent = opt.text;
            btn.dataset.value = opt.value;
            
            btn.onclick = function(e) {
                e.preventDefault();
                var val = this.dataset.value;
                var text = this.textContent;
                
                // 1. Update our UI
                if (titleSpan) titleSpan.textContent = text;
                document.querySelectorAll('.mobile-size-btn').forEach(function(b) { b.classList.remove('active'); });
                this.classList.add('active');
                
                // 2. Try to click the custom dropdown option if it exists (Select2 or custom)
                if (window.jQuery) {
                    var $parent = jQuery('#ssb-sizes');
                    // Find any element inside ssb-sizes that has the matching text and click it
                    var $option = $parent.find('*').filter(function() {
                        // match text precisely to avoid matching "12x20" when looking for "12x2"
                        return jQuery(this).text().trim() === text && jQuery(this).children().length === 0;
                    });
                    if ($option.length) {
                        $option.first().click();
                    } else {
                        // Fallback: update select natively
                        jQuery(select).val(val).trigger('change');
                    }
                } else {
                    select.value = val;
                    select.dispatchEvent(new Event('change', { bubbles: true }));
                }
            };
            container.appendChild(btn);
        });
    }
    
    renderButtons();

    // Re-render if select changes from somewhere else
    if (window.jQuery) {
        jQuery(select).on('change', function() {
            var val = jQuery(this).val();
            document.querySelectorAll('.mobile-size-btn').forEach(function(b) { 
                if (b.dataset.value === val) {
                    b.classList.add('active');
                    if (titleSpan) titleSpan.textContent = b.textContent;
                } else {
                    b.classList.remove('active');
                }
            });
        });
    }
});
</script>
"""

# Remove old injected CSS and JS to avoid duplicates
content = re.sub(r'/\* Mobile Size Buttons \*/[\s\S]*?@media \(min-width: 769px\) \{[\s\S]*?\}', '', content)
content = re.sub(r'<script>\s*document.addEventListener\("DOMContentLoaded", function\(\) \{\s*var select = document.getElementById\(\'ssb-configurator-size-area\'\);[\s\S]*?</script>', '', content)

content = content.replace('</style>', css_updates + '\n</style>')
content = content.replace('</body>', f'{js_code}\n</body>')

with open(file_path, 'w') as f:
    f.write(content)

print("Applied fixes for mobile sizing and model trigger.")
