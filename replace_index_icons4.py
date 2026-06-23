import re

file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Types
content = content.replace(
    '<i class="icon ic-types" style="width: 14px; height: 14px; margin-right: 6px;"></i>Types:',
    '<i class="icon ic-types" style="width: 24px; height: 24px; margin-right: 10px;"></i>Types:'
)

# 2. Change Location
content = content.replace(
    '<i class="icon ic-navigation" style="width: 14px; height: 14px;"></i>',
    '<i class="icon ic-navigation" style="width: 16px; height: 16px;"></i>'
)

# 3. Selected plus/minus CSS
content = re.sub(
    r'\.ssb-configurator-panel-heading \.ssb-configurator-selected::after \{[\s\S]*?\}',
    '.ssb-configurator-panel-heading .ssb-configurator-selected::after {\n            content: "";\n            display: inline-block;\n            width: 24px;\n            height: 24px;\n            margin-left: 10px;\n            background-color: var(--gray-1, #5E6578);\n            -webkit-mask: url("../../assets/icons/raw/ic-show-more.svg") no-repeat center;\n            mask: url("../../assets/icons/raw/ic-show-more.svg") no-repeat center;\n            -webkit-mask-size: contain;\n            mask-size: contain;\n        }',
    content
)

content = re.sub(
    r'\.ssb-configurator-panel-heading\.ui-accordion-header-active \.ssb-configurator-selected::after \{[\s\S]*?\}',
    '.ssb-configurator-panel-heading.ui-accordion-header-active .ssb-configurator-selected::after {\n            -webkit-mask: url("../../assets/icons/raw/ic-show-less.svg") no-repeat center;\n            mask: url("../../assets/icons/raw/ic-show-less.svg") no-repeat center;\n        }',
    content
)

# 4. Hide old CSS icons and responsive text
css_to_add = """
        button.ssb-save-model::before,
        button.ssb-share-model::before,
        button.ssb-reset-btn::before {
            display: none !important;
            background-image: none !important;
            content: none !important;
        }

        @media (max-width: 768px) {
            button.ssb-save-model .btn-text-full,
            button.ssb-reset-btn .btn-text-full {
                display: none;
            }
        }
"""
if "button.ssb-save-model::before" not in content:
    content = content.replace('/* 18. Hide Canvas Loader */', css_to_add + '\n        /* 18. Hide Canvas Loader */')

# 5. Buttons Texts and Icon Sizes
content = content.replace(
    '<button class="button ssb-save-btn ssb-share-model not_login" data-copy-on-click="Copied Text"><i class="icon ic-duplicate" style="margin-right: 6px;"></i>Share</button>',
    '<button class="button ssb-save-btn ssb-share-model not_login" data-copy-on-click="Copied Text"><i class="icon ic-duplicate" style="width: 16px; height: 16px; margin-right: 6px;"></i>Share</button>'
)

content = content.replace(
    '<button data-ajax_url="https://demo.shedpro.co/wp-admin/admin-ajax.php" data-title="Garden Shed" class="button ssb-save-model not_login"><i class="icon ic-favorite" style="margin-right: 6px;"></i>Save</button>',
    '<button data-ajax_url="https://demo.shedpro.co/wp-admin/admin-ajax.php" data-title="Garden Shed" class="button ssb-save-model not_login"><i class="icon ic-favorite" style="width: 16px; height: 16px; margin-right: 6px;"></i>Save<span class="btn-text-full">&nbsp;for later</span></button>'
)

content = content.replace(
    '<button class="button ssb-reset-btn"><i class="icon ic-refresh" style="margin-right: 6px;"></i>Reset</button>',
    '<button class="button ssb-reset-btn"><i class="icon ic-refresh" style="width: 16px; height: 16px; margin-right: 6px;"></i>Reset<span class="btn-text-full">&nbsp;model</span></button>'
)

with open(file_path, 'w') as f:
    f.write(content)

print("Updated buttons and icons CSS in index.html")
