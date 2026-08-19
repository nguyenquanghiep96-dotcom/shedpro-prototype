import re

with open('public/v2/product/premium-shed/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the 51 items block with the 4 items
old_block = """<ul class="ssb-configurator-options ssb-configurator-style-sub-cat has-default">
<li class="ssb-option display-thumbnail">
<div class="ssb-thumbnail">
<img alt="" src="../../../dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Chalet.jpg"/>
</div>
<span class="ssb-option-name">Chalet</span>
</li>
<li class="ssb-option display-thumbnail">
<div class="ssb-thumbnail">
<img alt="" src="../../../dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Aframe.jpg"/>
</div>
<span class="ssb-option-name">Aframe</span>
</li>
<li class="ssb-option display-thumbnail active">
<div class="ssb-thumbnail">
<img alt="" src="../../../dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2026/03/Thumbnail-Garden-Shed-e1774972270853.png"/>
</div>
<span class="ssb-option-name">Premium Shed</span>
</li>
<li class="ssb-option display-thumbnail">
<div class="ssb-thumbnail">
<img alt="" src="../../../dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Log-Cabin.jpg"/>
</div>
<span class="ssb-option-name">Log Cabin</span>
</li>
</ul>"""

content = re.sub(r'<ul class="ssb-configurator-options ssb-configurator-style-sub-cat has-default">.*?</ul>', old_block, content, flags=re.DOTALL)

# Replace the JS
js_regex = r"\$\('#v2-tab-Style'\)\.on\('click', '\.v2-mobile-filter-pill', function\(\) \{.*?\n        \}"

original_js = """$('#v2-tab-Style').on('click', '.v2-mobile-filter-pill', function() {
                $('#v2-tab-Style .v2-mobile-filter-pill').removeClass('active');
                $(this).addClass('active');
                var typeId = $(this).data('type-id');
                $('#shed-type-dropdown .dropdown-shed[data-id="' + typeId + '"]').trigger('click');
                setTimeout(populateStyleGrid, 300);
            });

            $('#v2-tab-Style').on('click', '.v2-mobile-style-card', function() {
                var idx = $(this).data('index');
                var $opt = $('#ssb-configurator-accordion-style .ssb-option.display-thumbnail').eq(idx);
                $opt.find('a, span, img').first().trigger('click');
                $('.v2-mobile-style-card').removeClass('active');
                $(this).addClass('active');
            });
        }

        function populateStyleGrid() {
            var gridHtml = '';
            $('#ssb-configurator-accordion-style .ssb-option.display-thumbnail').each(function(index) {
                var name = $(this).find('.ssb-option-name').text();
                var imgSrc = $(this).find('img').attr('src');
                var isActive = $(this).hasClass('active');
                gridHtml += '<div class="v2-mobile-style-card ' + (isActive ? 'active' : '') + '" data-index="' + index + '">' +
                    '<img src="' + imgSrc + '" alt="' + name + '">' +
                    '<span>' + name + '</span>' +
                '</div>';
            });
            $('#v2-tab-Style .v2-style-grid').html(gridHtml);
        }"""

content = re.sub(js_regex, original_js, content, flags=re.DOTALL)

with open('public/v2/product/premium-shed/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored 4 items and removed data-href successfully.")
