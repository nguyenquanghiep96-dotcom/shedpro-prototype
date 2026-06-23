file_path = 'public/v1/shedpro-design/product/garden-shed/index.html'

with open(file_path, 'r') as f:
    content = f.read()

content = content.replace('ic-saved', 'ic-favorite')
content = content.replace('ic-reset', 'ic-refresh')
content = content.replace('ic-plus-circle', 'ic-add')

with open(file_path, 'w') as f:
    f.write(content)

print("Icons replaced in index.html!")
