import re

with open('public/v2/product/premium-shed/index.html', 'r') as f:
    html = f.read()

# Replace the faulty window.jQuery.ajax override
old_script = """    window.jQuery.ajax = function(options) {
        if (options && typeof options.data === 'string' && options.data.includes('action=get_shareable_link_data')) {
            var d = window.jQuery.Deferred();
            // Simulate network delay to ensure UI loading states show up properly
            setTimeout(function() {
                d.resolve({
                    success: true,
                    data: {"""

new_script = """    window.jQuery.ajax = function(options) {
        var isShare = false;
        if (options && options.data) {
            if (typeof options.data === 'string' && options.data.includes('action=get_shareable_link_data')) {
                isShare = true;
            } else if (typeof options.data === 'object' && options.data.action === 'get_shareable_link_data') {
                isShare = true;
            }
        }
        if (isShare) {
            var d = window.jQuery.Deferred();
            // Simulate network delay to ensure UI loading states show up properly
            setTimeout(function() {
                d.resolve({
                    success: true,
                    data: {"""

if old_script in html:
    html = html.replace(old_script, new_script)
    with open('public/v2/product/premium-shed/index.html', 'w') as f:
        f.write(html)
    print("Fixed successfully.")
else:
    print("Could not find the old script to replace.")
