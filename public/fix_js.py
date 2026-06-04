with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'r') as f:
    ds_html = f.read()

scripts = """
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
"""

if "bootstrap.bundle.min.js" not in ds_html:
    ds_html = ds_html.replace('</body>', scripts)

with open('/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/design-system.html', 'w') as f:
    f.write(ds_html)

print("JS added.")
