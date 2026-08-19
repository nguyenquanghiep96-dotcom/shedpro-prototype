import re
import os

# All available files
files = [
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/03/A-Frame-With-Front-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/03/Chalet.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/05/Hip-Roof.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/A-Frame-With-Side-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Teahouse-1.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/2-Story-Gable-1.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Alpine-Chalet.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Streamline-2.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Lofted-Livestock.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Victorian-Cabin-1.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Gambrel-With-Front-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/The-Eave.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/2-Story-Gambrel.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Country-Cottage-1.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Accu-Steel-Greenhouse-1.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2022/09/Dormer.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2025/11/Commercial-Dog-Kennel.png",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2024/09/rendering-demo.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2024/09/tinyhome-leanto.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2024/09/tinyhome-cottageblack.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/05/Box-Eave.png",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/05/Regular-Roof.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/02/carport-vertical.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/07/Chicken-Coop.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Aframe.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Loafing-Shed.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Studio.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Log-Cabin.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Chalet.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/08/Garage-.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/08/Rancher.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/08/Carport-Lean-To.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/01/A-Frame-With-Deluxe-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/01/Barn-Middle-Porch-1.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/01/Barn-With-Corner-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/01/A-Frame-With-Corner-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/01/A-Frame-With-Middle-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/01/Barn-With-Deluxe-Porch.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2026/03/Thumbnail-Garden-Shed-e1774972270853.png",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2026/03/Barn-with-L-shape-Porch-e1774955734611.png",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2026/03/A-frame-with-L-shape-porch.png",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2021/10/Lean-To.jpg",
    "public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2020/07/Windsor-2.jpg"
]

def format_name(filename):
    name = os.path.splitext(filename)[0]
    name = re.sub(r'-e\d+$', '', name)
    name = re.sub(r'-\d+$', '', name)
    name = name.replace('-', ' ')
    return name

top_4_explicit = [
    ("public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Chalet.jpg", "Chalet"),
    ("public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Aframe.jpg", "Aframe"),
    ("public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2026/03/Thumbnail-Garden-Shed-e1774972270853.png", "Premium Shed"),
    ("public/v1/dxm5q5264srx2.cloudfront.net/wp-content/uploads/sites/4/2023/09/Log-Cabin.jpg", "Log Cabin")
]

selected_images = []
for p, n in top_4_explicit:
    selected_images.append((p, n))

for f in files:
    if f not in [x[0] for x in selected_images] and len(selected_images) < 20:
        if "Chalet.jpg" in f and "2022" in f: continue # Skip the duplicate chalet
        selected_images.append((f, format_name(os.path.basename(f))))

html_items = []
html_items.append('<ul class="ssb-configurator-options ssb-configurator-style-sub-cat has-default">')

for i, (img, name) in enumerate(selected_images):
    rel_path = img.replace("public/", "../../../")
    active_class = " active" if name == "Premium Shed" else ""
    html_items.append(f"""<li class="ssb-option display-thumbnail{active_class}">
<div class="ssb-thumbnail">
<img alt="{name}" src="{rel_path}"/>
</div>
<span class="ssb-option-name">{name}</span>
</li>""")

html_items.append("</ul>")
new_block = "\n".join(html_items)

with open('public/v2/product/premium-shed/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<ul class="ssb-configurator-options ssb-configurator-style-sub-cat has-default">.*?</ul>', new_block, content, flags=re.DOTALL)

with open('public/v2/product/premium-shed/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added 20 items correctly.")
