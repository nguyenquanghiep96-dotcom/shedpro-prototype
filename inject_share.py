import re

with open('custom_items.txt', 'r') as f:
    b64 = f.read().strip()

js_code = f"""
<script>
// Force the share parameter
if (!window.location.search.includes('share=')) {{
    var newUrl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?share=1c8ec01832f87d5b412d11fea3c3afcc02e5116537';
    window.history.replaceState({{path:newUrl}}, '', newUrl);
}}

// Override jQuery AJAX to bypass CORS and return the shared model directly
if (window.jQuery) {{
    var originalAjax = window.jQuery.ajax;
    window.jQuery.ajax = function(options) {{
        if (options && typeof options.data === 'string' && options.data.includes('action=get_shareable_link_data')) {{
            var d = window.jQuery.Deferred();
            // Simulate network delay to ensure UI loading states show up properly
            setTimeout(function() {{
                d.resolve({{
                    success: true,
                    data: {{
                        id: "1c8ec01832f87d5b412d11fea3c3afcc02e5116537",
                        base64Data: "{b64}"
                    }}
                }});
            }}, 100);
            return d.promise();
        }}
        return originalAjax.apply(this, arguments);
    }};
}}
</script>
"""

with open('public/v2/product/premium-shed/index.html', 'r') as f:
    html = f.read()

# Insert right after jquery-migrate
target = '<script id="jquery-migrate-js" src="../../../configurator-cdn.shedpro.co/production/wp-includes/js/jquery/jquery-migrate_ver%3D3.4.1.js" type="text/javascript"></script>'
if target in html:
    html = html.replace(target, target + '\n' + js_code)
    with open('public/v2/product/premium-shed/index.html', 'w') as f:
        f.write(html)
    print("Injected successfully.")
else:
    print("Could not find target script.")
