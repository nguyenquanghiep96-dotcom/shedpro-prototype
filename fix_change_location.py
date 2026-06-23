def fix_location(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Replace the wrong class '.canvas-container' with the correct one '.ssb-model-canvas-wrapper'
    content = content.replace("cl.appendTo('.canvas-container');", "cl.appendTo('.ssb-model-canvas-wrapper');")
    
    # Ensure ssb-model-canvas-wrapper has position relative
    if "jQuery('.ssb-model-canvas-wrapper').css('position', 'relative');" not in content:
        content = content.replace("cl.appendTo('.ssb-model-canvas-wrapper');", "jQuery('.ssb-model-canvas-wrapper').css('position', 'relative');\n            cl.appendTo('.ssb-model-canvas-wrapper');")
        
    with open(file_path, 'w') as f:
        f.write(content)

fix_location('public/v1/shedpro-design/product/garden-shed/index.html')
fix_location('public/v1/shedpro-design/product/chalet/index.html')
print("Change Location JS fixed!")
