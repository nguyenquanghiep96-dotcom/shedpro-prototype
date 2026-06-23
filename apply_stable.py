import re

file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

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
    #ssb-configurator-width-length {
        width: 100% !important;
        max-width: 100% !important;
    }
    #ssb-configurator-width-length .ssb-custom-select {
        display: none !important;
    }
    .mobile-size-buttons {
        display: flex !important;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 16px;
        margin-top: 10px;
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
    var select = document.getElementById('ssb-configurator-size-area');
    if (!select) return;

    var container = document.createElement('div');
    container.className = 'mobile-size-buttons';
    
    var parentBlock = document.getElementById('ssb-configurator-width-length');
    if (parentBlock) {
        parentBlock.appendChild(container);
    }
    
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

    function renderButtons() {
        container.innerHTML = '';
        Array.from(select.options).forEach(function(opt) {
            var btn = document.createElement('button');
            btn.className = 'mobile-size-btn';
            if (opt.selected || opt.value === select.value) {
                btn.classList.add('active');
                if (titleSpan) titleSpan.textContent = opt.text;
            }
            btn.textContent = opt.text;
            btn.dataset.value = opt.value;
            
            btn.onclick = function(e) {
                e.preventDefault();
                var val = this.dataset.value;
                var text = this.textContent;
                
                if (titleSpan) titleSpan.textContent = text;
                document.querySelectorAll('.mobile-size-btn').forEach(function(b) { b.classList.remove('active'); });
                this.classList.add('active');
                
                if (window.jQuery) {
                    var $parent = jQuery('#ssb-sizes');
                    // Try finding element with data-value first
                    var $customOpt = $parent.find('[data-value="' + val + '"]').not('select, option');
                    if ($customOpt.length) {
                        var ev = new MouseEvent('click', { bubbles: true, cancelable: true });
                        $customOpt[0].dispatchEvent(ev);
                    } else {
                        // Fallback: match text
                        var $textOpt = $parent.find('*').filter(function() {
                            return jQuery(this).text().trim() === text && jQuery(this).children().length === 0 && !jQuery(this).hasClass('mobile-size-btn');
                        });
                        if ($textOpt.length) {
                            var ev2 = new MouseEvent('click', { bubbles: true, cancelable: true });
                            $textOpt[0].dispatchEvent(ev2);
                        } else {
                            jQuery(select).val(val).trigger('change');
                            jQuery('#ssb-sizes').trigger('change');
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
    
    // The dropdown might be populated asynchronously. Use MutationObserver to update buttons.
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

content = content.replace('</body>', f'{css_code}\n{js_code}\n</body>')

with open(file_path, 'w') as f:
    f.write(content)

print("Applied stable fixes without dummy options.")
