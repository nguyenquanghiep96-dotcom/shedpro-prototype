import re

file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Add demo options to HTML
if 'value="14x20"' not in content:
    options_area = """<option disabled class="ssb-option display-text select size-area" value="14x20">14x20</option>
<option disabled class="ssb-option display-text select size-area" value="14x24">14x24</option>
<option disabled class="ssb-option display-text select size-area" value="14x28">14x28</option>
<option disabled class="ssb-option display-text select size-area" value="16x20">16x20</option>
<option disabled class="ssb-option display-text select size-area" value="16x24">16x24</option>
<option disabled class="ssb-option display-text select size-area" value="16x28">16x28</option>
"""
    idx = content.find('id="ssb-configurator-size-area"')
    if idx != -1:
        end_idx = content.find('</select>', idx)
        if end_idx != -1:
            content = content[:end_idx] + options_area + content[end_idx:]

if 'value="8.0"' not in content:
    options_height = """<option disabled class="ssb-option display-text select size-height" value="8.0">8.0</option>
<option disabled class="ssb-option display-text select size-height" value="8.5">8.5</option>
<option disabled class="ssb-option display-text select size-height" value="9.0">9.0</option>
"""
    idx = content.find('id="ssb-configurator-size-height"')
    if idx != -1:
        end_idx = content.find('</select>', idx)
        if end_idx != -1:
            content = content[:end_idx] + options_height + content[end_idx:]

# 2. Add fresh CSS and JS at the end before </body>
css_code = """
<style>
/* Fix ic-close for popups */
.center-item-popup .sheet-close-btn,
.mobile-customize-panel .icon-close,
.ui-dialog .ui-dialog-titlebar-close, 
.close-popup,
.close-custom-line-item,
#close-ar-popup-mobile,
span.icon-close {
    background-image: none !important;
    mask-image: url('../../assets/icons/raw/ic-close.svg') !important;
    -webkit-mask-image: url('../../assets/icons/raw/ic-close.svg') !important;
    mask-size: contain !important;
    -webkit-mask-size: contain !important;
    mask-repeat: no-repeat !important;
    -webkit-mask-repeat: no-repeat !important;
    mask-position: center !important;
    -webkit-mask-position: center !important;
    background-color: var(--gray-1) !important;
}

/* Mobile Size Buttons */
@media (max-width: 768px) {
    .ssb-configurator-size-selects {
        display: block !important;
    }
    #ssb-configurator-width-length, #ssb-configurator-height {
        width: 100% !important;
        max-width: 100% !important;
        display: block !important;
        margin-bottom: 20px;
    }
    .ssb-configurator-options .size-label {
        font-family: 'Proxima Nova', sans-serif;
        font-size: 14px;
        font-weight: 700;
        color: var(--gray-1);
        display: block;
        margin-bottom: 8px;
    }
    #ssb-configurator-width-length .ssb-custom-select,
    #ssb-configurator-height .ssb-custom-select {
        display: none !important;
    }
    .mobile-size-buttons {
        display: flex !important;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 16px;
    }
    .mobile-size-btn {
        box-sizing: border-box;
        width: calc((100% - 32px) / 3);
        font-family: 'Proxima Nova', sans-serif;
        font-size: 14px;
        font-weight: 700;
        color: var(--gray-1);
        padding: 8px 0;
        text-align: center;
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
    .mobile-size-btn:disabled {
        opacity: 0.4;
        cursor: not-allowed;
        background: #f5f5f5;
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
</style>
"""

js_code = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    // Setup Top Title for Mobile Panel
    var mobilePanel = document.querySelector('.mobile-customize-panel');
    var titleSpan = null;
    if (mobilePanel) {
        mobilePanel.childNodes.forEach(function(node) {
            if (node.nodeType === 3 && node.nodeValue.trim().length > 0) {
                node.nodeValue = '';
            }
        });
        titleSpan = mobilePanel.querySelector('.mobile-panel-title');
        if (!titleSpan) {
            titleSpan = document.createElement('span');
            titleSpan.className = 'mobile-panel-title';
            var iconClose = mobilePanel.querySelector('.icon-close');
            if (iconClose) {
                mobilePanel.insertBefore(titleSpan, iconClose);
            } else {
                mobilePanel.appendChild(titleSpan);
            }
        }
    }

    var selects = [
        { id: 'ssb-configurator-size-area', parentId: 'ssb-configurator-width-length', wrapperId: 'ssb-sizes', updateTitle: true },
        { id: 'ssb-configurator-size-height', parentId: 'ssb-configurator-height', wrapperId: 'ssb-height', updateTitle: false }
    ];

    selects.forEach(function(cfg) {
        var select = document.getElementById(cfg.id);
        var parentBlock = document.getElementById(cfg.parentId);
        if (!select || !parentBlock) return;

        var existing = parentBlock.querySelector('.mobile-size-buttons');
        if (existing) existing.remove();

        var container = document.createElement('div');
        container.className = 'mobile-size-buttons';
        parentBlock.appendChild(container);

        function renderButtons() {
            container.innerHTML = '';
            Array.from(select.options).forEach(function(opt) {
                var btn = document.createElement('button');
                btn.className = 'mobile-size-btn';
                if (opt.selected || opt.value === select.value) {
                    btn.classList.add('active');
                    if (cfg.updateTitle && titleSpan && !opt.disabled) {
                        titleSpan.textContent = opt.text;
                    }
                }
                btn.textContent = opt.text;
                btn.dataset.value = opt.value;
                if (opt.disabled) {
                    btn.disabled = true;
                }
                
                btn.onclick = function(e) {
                    e.preventDefault();
                    if (this.disabled) return;
                    
                    var val = this.dataset.value;
                    var text = this.textContent;
                    
                    if (cfg.updateTitle && titleSpan) titleSpan.textContent = text;
                    container.querySelectorAll('.mobile-size-btn').forEach(function(b) { b.classList.remove('active'); });
                    this.classList.add('active');
                    
                    if (window.jQuery) {
                        var $parent = jQuery('#' + cfg.wrapperId);
                        var $customOpt = $parent.find('[data-value="' + val + '"]').not('select, option');
                        if ($customOpt.length) {
                            var ev = new MouseEvent('click', { bubbles: true, cancelable: true });
                            $customOpt[0].dispatchEvent(ev);
                        } else {
                            var $textOpt = $parent.find('*').filter(function() {
                                return jQuery(this).text().trim() === text && jQuery(this).children().length === 0 && !jQuery(this).hasClass('mobile-size-btn');
                            });
                            if ($textOpt.length) {
                                var ev2 = new MouseEvent('click', { bubbles: true, cancelable: true });
                                $textOpt[0].dispatchEvent(ev2);
                            } else {
                                jQuery(select).val(val).trigger('change');
                                jQuery('#' + cfg.wrapperId).trigger('change');
                            }
                        }
                    } else {
                        select.value = val;
                        select.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                };
                container.appendChild(btn);
            });
        }
        
        var observer = new MutationObserver(function(mutations) {
            var needsRender = false;
            mutations.forEach(function(m) {
                if (m.type === 'childList') needsRender = true;
            });
            if (needsRender) renderButtons();
        });
        observer.observe(select, { childList: true });

        renderButtons();

        if (window.jQuery) {
            jQuery(select).on('change', function() {
                var val = jQuery(this).val();
                container.querySelectorAll('.mobile-size-btn').forEach(function(b) { 
                    if (b.dataset.value === val) {
                        b.classList.add('active');
                        if (cfg.updateTitle && titleSpan) titleSpan.textContent = b.textContent;
                    } else {
                        b.classList.remove('active');
                    }
                });
            });
        }
    });
});
</script>
"""

content = content.replace('</body>', f'{css_code}\n{js_code}\n</body>')

with open(file_path, 'w') as f:
    f.write(content)

print("Applied clean fixes.")
