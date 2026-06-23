import re

file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Change Location
content = content.replace(
    '<img src="../../assets/icons/ic-navigation.svg" style="width: 14px; height: 14px;" />',
    '<i class="icon ic-navigation" style="width: 14px; height: 14px;"></i>'
)

# 2. Types
content = content.replace(
    '<span class="text">Types:</span>',
    '<span class="text"><i class="icon ic-types" style="width: 14px; height: 14px; margin-right: 6px;"></i>Types:</span>'
)

# 3. Type Dropdown
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

# 4. Accordions show more / less
mask_more = 'data:image/svg+xml,%3Csvg width=\'24\' height=\'24\' viewBox=\'0 0 24 24\' fill=\'none\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M11.8496 0C18.3895 0 23.7 5.30979 23.7002 11.8496C23.7002 18.3896 18.3896 23.7002 11.8496 23.7002V23.6904C5.30979 23.6902 0 18.3795 0 11.8496C0.000211961 5.31992 5.30992 0.00021204 11.8496 0ZM11.8496 2C6.41992 2.00021 2.00021 6.41992 2 11.8496C2 17.2795 6.41979 21.7 11.8496 21.7002C17.2796 21.7002 21.7002 17.2796 21.7002 11.8496C21.7 6.41979 17.2795 2 11.8496 2ZM12 5.34375C12.5537 5.34375 13.0098 5.79983 13.0098 6.35352V10.9902H17.6465C18.2002 10.9902 18.6563 11.4463 18.6562 12C18.6562 12.5537 18.2002 13.0098 17.6465 13.0098H13.0098L12.998 12.998V17.6348C12.998 18.1885 12.542 18.6445 11.9883 18.6445C11.7117 18.6445 11.458 18.5291 11.2793 18.3506C11.1005 18.1718 10.9854 17.9175 10.9854 17.6406V13.0039H6.34766C6.07085 13.0039 5.81745 12.8878 5.63867 12.709C5.45991 12.5302 5.34375 12.2768 5.34375 12C5.34375 11.4463 5.79983 10.9902 6.35352 10.9902H10.9902V6.35352C10.9902 5.79983 11.4463 5.34375 12 5.34375Z\' fill=\'white\'/%3E%3C/svg%3E'
content = content.replace(f'url("{mask_more}")', 'url("../../assets/icons/raw/ic-show-more.svg")')

mask_less = 'data:image/svg+xml,%3Csvg width=\'24\' height=\'24\' viewBox=\'0 0 24 24\' fill=\'none\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M11.8496 0C18.3895 0 23.7 5.30979 23.7002 11.8496C23.7002 18.3896 18.3896 23.7002 11.8496 23.7002V23.6904C5.30979 23.6902 0 18.3795 0 11.8496C0.000211961 5.31992 5.30992 0.00021204 11.8496 0ZM11.8496 2C6.41992 2.00021 2.00021 6.41992 2 11.8496C2 17.2795 6.41979 21.7 11.8496 21.7002C17.2796 21.7002 21.7002 17.2796 21.7002 11.8496C21.7 6.41979 17.2795 2 11.8496 2ZM15.2793 7.29395C15.6708 6.90245 16.3145 6.90243 16.7061 7.29395C17.0976 7.68546 17.0976 8.32918 16.7061 8.7207L13.4277 12H13.4111L16.6904 15.2793C17.0815 15.6707 17.0815 16.3146 16.6904 16.7061C16.4947 16.9018 16.2333 17 15.9805 17C15.7276 17 15.4663 16.9018 15.2705 16.7061L11.9922 13.4277L8.71289 16.7061C8.51713 16.9018 8.25578 17 8.00293 17C7.75018 16.9999 7.48962 16.9017 7.29395 16.7061C6.90243 16.3145 6.90245 15.6708 7.29395 15.2793L10.5723 12L7.29395 8.7207C6.90244 8.32918 6.90243 7.68546 7.29395 7.29395C7.68546 6.90243 8.32918 6.90244 8.7207 7.29395L12 10.5723L15.2793 7.29395Z\' fill=\'white\'/%3E%3C/svg%3E'
content = content.replace(f'url("{mask_less}")', 'url("../../assets/icons/raw/ic-show-less.svg")')

# 5. Share Button
content = content.replace(
    '<button class="button ssb-save-btn ssb-share-model not_login" data-copy-on-click="Copied Text">Share</button>',
    '<button class="button ssb-save-btn ssb-share-model not_login" data-copy-on-click="Copied Text"><i class="icon ic-duplicate" style="margin-right: 6px;"></i>Share</button>'
)

# 6. Full View
content = re.sub(
    r'<div id="fullscreen">\s*<svg id="Layer_1"[\s\S]*?</svg>\s*</div>',
    '<div id="fullscreen">\n\t\t\t\t\t<i class="icon ic-zoom-out"></i>\n\t\t\t\t</div>',
    content
)

with open(file_path, 'w') as f:
    f.write(content)

print("Updated 3D Configurator index.html")
