def fix_ids(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Replace Garden Shed product ID with Chalet product ID
    content = content.replace('6857', '3353')
    
    with open(file_path, 'w') as f:
        f.write(content)

fix_ids('public/v1/shedpro-design/product/chalet/index.html')
print("Fixed IDs in Chalet!")
