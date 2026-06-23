import re
import os

file_path = 'public/v1/shedpro-design/product/chalet/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# --- Apply replace_index_icons3.py ---
content = content.replace(
    '<img src="../../assets/icons/ic-navigation.svg" style="width: 14px; height: 14px;" />',
    '<i class="icon ic-navigation" style="width: 14px; height: 14px;"></i>'
)

content = content.replace(
    '<span class="text">Types:</span>',
    '<span class="text"><i class="icon ic-types" style="width: 14px; height: 14px; margin-right: 6px;"></i>Types:</span>'
)

content = re.sub(
    r'\.shed-type-dropdown \.current::after \{[\s\S]*?\}',
    '.shed-type-dropdown .current::after {\n            content: "";\n            display: inline-block;\n            width: 24px;\n            height: 24px;\n            background-color: var(--gray-1, #5E6578) !important;\n            -webkit-mask: url("../../assets/icons/raw/ic-keyboard_arrow_down.svg") no-repeat center !important;\n            mask: url("../../assets/icons/raw/ic-keyboard_arrow_down.svg") no-repeat center !important;\n            -webkit-mask-size: contain !important;\n            mask-size: contain !important;\n        }',
    content
)

content = re.sub(
    r'\.ssb-configurator-shed-type \.text::before \{[\s\S]*?\}',
    '.ssb-configurator-shed-type .text::before {\n            display: none !important;\n        }',
    content
)

mask_more = 'data:image/svg+xml,%3Csvg width=\'24\' height=\'24\' viewBox=\'0 0 24 24\' fill=\'none\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M11.8496 0C18.3895 0 23.7 5.30979 23.7002 11.8496C23.7002 18.3896 18.3896 23.7002 11.8496 23.7002V23.6904C5.30979 23.6902 0 18.3795 0 11.8496C0.000211961 5.31992 5.30992 0.00021204 11.8496 0ZM11.8496 2C6.41992 2.00021 2.00021 6.41992 2 11.8496C2 17.2795 6.41979 21.7 11.8496 21.7002C17.2796 21.7002 21.7002 17.2796 21.7002 11.8496C21.7 6.41979 17.2795 2 11.8496 2ZM12 5.34375C12.5537 5.34375 13.0098 5.79983 13.0098 6.35352V10.9902H17.6465C18.2002 10.9902 18.6563 11.4463 18.6562 12C18.6562 12.5537 18.2002 13.0098 17.6465 13.0098H13.0098L12.998 12.998V17.6348C12.998 18.1885 12.542 18.6445 11.9883 18.6445C11.7117 18.6445 11.458 18.5291 11.2793 18.3506C11.1005 18.1718 10.9854 17.9175 10.9854 17.6406V13.0039H6.34766C6.07085 13.0039 5.81745 12.8878 5.63867 12.709C5.45991 12.5302 5.34375 12.2768 5.34375 12C5.34375 11.4463 5.79983 10.9902 6.35352 10.9902H10.9902V6.35352C10.9902 5.79983 11.4463 5.34375 12 5.34375Z\' fill=\'white\'/%3E%3C/svg%3E'
content = content.replace(f'url("{mask_more}")', 'url("../../assets/icons/raw/ic-show-more.svg")')

mask_less = 'data:image/svg+xml,%3Csvg width=\'24\' height=\'24\' viewBox=\'0 0 24 24\' fill=\'none\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M11.8496 0C18.3895 0 23.7 5.30979 23.7002 11.8496C23.7002 18.3896 18.3896 23.7002 11.8496 23.7002V23.6904C5.30979 23.6902 0 18.3795 0 11.8496C0.000211961 5.31992 5.30992 0.00021204 11.8496 0ZM11.8496 2C6.41992 2.00021 2.00021 6.41992 2 11.8496C2 17.2795 6.41979 21.7 11.8496 21.7002C17.2796 21.7002 21.7002 17.2796 21.7002 11.8496C21.7 6.41979 17.2795 2 11.8496 2ZM15.2793 7.29395C15.6708 6.90245 16.3145 6.90243 16.7061 7.29395C17.0976 7.68546 17.0976 8.32918 16.7061 8.7207L13.4277 12H13.4111L16.6904 15.2793C17.0815 15.6707 17.0815 16.3146 16.6904 16.7061C16.4947 16.9018 16.2333 17 15.9805 17C15.7276 17 15.4663 16.9018 15.2705 16.7061L11.9922 13.4277L8.71289 16.7061C8.51713 16.9018 8.25578 17 8.00293 17C7.75018 16.9999 7.48962 16.9017 7.29395 16.7061C6.90243 16.3145 6.90245 15.6708 7.29395 15.2793L10.5723 12L7.29395 8.7207C6.90244 8.32918 6.90243 7.68546 7.29395 7.29395C7.68546 6.90243 8.32918 6.90244 8.7207 7.29395L12 10.5723L15.2793 7.29395Z\' fill=\'white\'/%3E%3C/svg%3E'
content = content.replace(f'url("{mask_less}")', 'url("../../assets/icons/raw/ic-show-less.svg")')

content = content.replace(
    '<button class="button ssb-save-btn ssb-share-model not_login" data-copy-on-click="Copied Text">Share</button>',
    '<button class="button ssb-save-btn ssb-share-model not_login" data-copy-on-click="Copied Text"><i class="icon ic-duplicate" style="margin-right: 6px;"></i>Share</button>'
)

content = re.sub(
    r'<div id="fullscreen">\s*<svg id="Layer_1"[\s\S]*?</svg>\s*</div>',
    '<div id="fullscreen">\n\t\t\t\t\t<i class="icon ic-zoom-out"></i>\n\t\t\t\t</div>',
    content
)

# --- Apply replace_index_icons4.py ---
content = content.replace(
    '<span class="ssb-color-indicator"></span>',
    '<i class="icon ic-dropdown ssb-color-indicator" style="background-color: var(--gray-4); width: 12px; height: 12px; position: absolute; right: 10px; top: 50%; transform: translateY(-50%);"></i>'
)

# --- Apply apply_mvp_fixes.py ---
svg_logo = """<svg xmlns="http://www.w3.org/2000/svg" width="auto" height="16" viewBox="0 0 870 273" fill="none" class="img-fluid" aria-label="ShedPro">
<path d="M553.578 206.138H580.708V169.763H606.26C629.92 169.763 642.854 153.829 642.854 134.515C642.854 115.04 629.92 98.7839 606.26 98.7839H553.578V206.138ZM615.251 134.354C615.251 141.597 609.888 146.264 602.633 146.264H580.708V122.122H602.633C609.888 122.122 615.251 126.95 615.251 134.354Z" fill="#FF7048"></path>
<path d="M715.187 206.138H746.26L724.809 166.705C734.588 163.164 745.787 153.185 745.787 134.515C745.787 114.557 732.538 98.7839 709.193 98.7839H656.511V206.138H683.641V169.763H697.521L715.187 206.138ZM718.184 134.193C718.184 141.597 712.19 146.264 705.092 146.264H683.641V122.122H705.092C712.19 122.122 718.184 126.789 718.184 134.193Z" fill="#FF7048"></path>
<path d="M757.007 152.542C757.007 185.215 781.14 208.07 813.318 208.07C845.495 208.07 869.471 185.215 869.471 152.542C869.471 119.868 845.495 97.0134 813.318 97.0134C781.14 97.0134 757.007 119.868 757.007 152.542ZM841.867 152.542C841.867 169.924 830.668 183.605 813.318 183.605C795.81 183.605 784.61 169.924 784.61 152.542C784.61 134.998 795.81 121.478 813.318 121.478C830.668 121.478 841.867 134.998 841.867 152.542Z" fill="#FF7048"></path>
<path fill-rule="evenodd" clip-rule="evenodd" d="M130.412 0.764648L220.409 43.9817L212.95 59.4064L130.412 19.7709L50.1844 58.2968L17.9462 111.711V255.113H218.97V272.235H0.764648V106.959L38.1047 45.0913L130.412 0.764648Z" fill="#FF7048"></path>
<path d="M101.949 190.984C112.535 201.3 127.386 208.07 148.714 208.07C176.994 208.07 192.635 193.724 192.635 172.125C192.635 147.787 168.621 142.629 151.242 138.921C139.551 136.665 133.073 134.731 133.073 129.089C133.073 124.415 136.549 120.708 145.555 120.708C154.876 120.708 166.409 124.415 175.257 131.829L190.108 112.004C178.89 102.171 164.197 97.0134 147.292 97.0134C120.276 97.0134 105.267 112.648 105.267 130.701C105.267 156.168 129.598 160.681 146.976 164.227C158.194 166.645 164.987 169.063 164.987 175.188C164.987 180.346 159.3 184.375 149.978 184.375C135.601 184.375 123.91 177.928 116.326 170.191L101.949 190.984Z" fill="#2B3B63"></path>
<path d="M277.862 206.135H305.037V98.6253H277.862V138.76H234.099V98.6253H206.925V206.135H234.099V162.938H277.862V206.135Z" fill="#2B3B63"></path>
<path d="M325.609 206.135H402.865V182.764H352.783V163.421H401.76V139.889H352.783V121.997H402.865V98.6253H325.609V206.135Z" fill="#2B3B63"></path>
<path d="M420.223 206.135H464.618C497.638 206.135 521.495 185.665 521.495 152.3C521.495 118.935 497.638 98.6253 464.46 98.6253H420.223V206.135ZM447.398 181.958V122.803H464.618C483.893 122.803 493.689 135.698 493.689 152.3C493.689 168.257 482.945 181.958 464.46 181.958H447.398Z" fill="#2B3B63"></path>
</svg>"""

new_panel = f"""<div class="mobile-customize-panel d-none d-lg-block" style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px;">
		<div class="mobile-panel-logo" style="display: flex; align-items: center;">
			{svg_logo}
		</div>
		<span class="mobile-panel-size-text" style="font-family: 'Proxima Nova', sans-serif; font-size: 12px; font-weight: 700; flex: 1; text-align: center; color: var(--gray-1);">12x16</span>
		<span class="icon-close"></span>
	</div>"""
	
content = re.sub(r'<div class="mobile-customize-panel d-none d-lg-block">\s*Customize\s*<span class="icon-close"></span>\s*</div>', new_panel, content)

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
</style>
"""

js_mvp = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    // Move Change Location to Canvas
    if (window.jQuery) {
        var cl = jQuery('#change-location-trigger');
        if (cl.length) {
            cl.appendTo('.canvas-container');
            cl.css({
                'position': 'absolute',
                'bottom': '20px',
                'left': '20px',
                'z-index': '100',
                'background': 'rgba(255,255,255,0.8)',
                'padding': '8px 12px',
                'border-radius': '6px',
                'box-shadow': '0 2px 4px rgba(0,0,0,0.1)'
            });
        }
        
        // Update Size text dynamically
        jQuery('#ssb-configurator-size-area').on('change', function() {
            var text = jQuery(this).find('option:selected').text();
            jQuery('.mobile-panel-size-text').text(text);
        });
        
        // Initial setup
        var initialText = jQuery('#ssb-configurator-size-area').find('option:selected').text();
        if(initialText) jQuery('.mobile-panel-size-text').text(initialText);
    }
});
</script>
"""
content = content.replace('</body>', f'{css_code}\n{js_mvp}\n</body>')

# 4. Disable other Styles and update Garden Shed URL
# In Chalet, we need "Premium Shed" to point to garden-shed
content = content.replace('data-href="https://demo.shedpro.co/product/garden-shed/"', 'data-href="../garden-shed/index.html"')
for style in ['tiny-home', 'lean-to', 'a-frame', 'log-cabin', 'alpine-chalet']:
    content = content.replace(f'data-href="https://demo.shedpro.co/product/{style}/"', f'data-href="#" style="opacity:0.4; cursor:not-allowed;"')

with open(file_path, 'w') as f:
    f.write(content)

print("Applied Chalet setup successfully!")
