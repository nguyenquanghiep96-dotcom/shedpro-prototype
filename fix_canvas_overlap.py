import re

file_path = '/Users/hiep/Sites/shedpro-static-clone/public/v1/shedpro-design/product/garden-shed/index.html'
with open(file_path, 'r') as f:
    html = f.read()

# Add overflow: hidden to .ssb-model-inner
html = html.replace('background-color: #f4f6f9 !important;', 'background-color: #f4f6f9 !important;\n                overflow: hidden !important;')

# Force canvas to match its container's height instead of window height
canvas_css = """
            #ssb-builder .ssb-model-canvas-wrapper,
            #ssb-builder canvas {
                height: 100% !important;
                max-height: 40vh !important;
                width: 100% !important;
                object-fit: contain !important;
            }
"""

if "/* 2. Fix Panel to bottom 60% */" in html:
    html = html.replace("/* 2. Fix Panel to bottom 60% */", canvas_css + "\n            /* 2. Fix Panel to bottom 60% */")

with open(file_path, 'w') as f:
    f.write(html)
print("Fixed canvas overlap issue.")
