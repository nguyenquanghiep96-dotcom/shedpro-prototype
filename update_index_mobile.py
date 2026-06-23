import re

file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. CSS Injection
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
    #ssb-configurator-width-length .ssb-custom-select {
        display: none !important;
    }
    .mobile-size-buttons {
        display: flex !important;
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
}
@media (min-width: 769px) {
    .mobile-size-buttons {
        display: none !important;
    }
}
</style>
"""

# 2. JS Injection
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

    function renderButtons() {
        container.innerHTML = '';
        Array.from(select.options).forEach(function(opt) {
            var btn = document.createElement('button');
            btn.className = 'mobile-size-btn';
            if (opt.selected) btn.classList.add('active');
            btn.textContent = opt.text;
            btn.dataset.value = opt.value;
            btn.onclick = function(e) {
                e.preventDefault();
                select.value = this.dataset.value;
                if (window.jQuery) {
                    jQuery(select).trigger('change');
                } else {
                    select.dispatchEvent(new Event('change', { bubbles: true }));
                }
                renderButtons();
            };
            container.appendChild(btn);
        });
    }
    
    renderButtons();

    if (window.jQuery) {
        jQuery(select).on('change', renderButtons);
    } else {
        select.addEventListener('change', renderButtons);
    }
    
    var observer = new MutationObserver(function(mutations) {
        renderButtons();
    });
    observer.observe(select, { childList: true, subtree: true });
});
</script>
"""

if 'mobile-size-buttons' not in content:
    content = content.replace('</body>', f'{css_code}\n{js_code}\n</body>')

with open(file_path, 'w') as f:
    f.write(content)

print("Injected fixes to index.html")
