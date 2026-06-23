from bs4 import BeautifulSoup
import re

def set_default_colors(file_path):
    with open(file_path, 'r') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Update hidden inputs in js-shed-data
    shed_data = soup.find(id='js-shed-data')
    if shed_data:
        siding = shed_data.find('input', {'name': 'ssb-option-siding-color'})
        if siding: siding['value'] = 'Red'
        
        trim = shed_data.find('input', {'name': 'ssb-option-trim-color'})
        if trim: trim['value'] = 'Clay'
        
        roof = shed_data.find('input', {'name': 'ssb-option-roof-color'})
        if roof: roof['value'] = 'Red'
        
    # 2. Update the color picker UI selections (remove active from old, add to new)
    def update_picker(group_name, color_val):
        group = soup.find('div', id=f"ssb-configurator-accordion-{group_name}")
        if not group: return
        
        # Remove active
        for active in group.find_all('span', class_='active'):
            active['class'] = [c for c in active.get('class', []) if c != 'active']
            
        # Add active
        target = group.find('span', {'data-option-value': color_val})
        if target:
            target['class'] = target.get('class', []) + ['active']
            
    update_picker('colors', 'Red') # Siding is first usually
    # For Trim and Roof, they are in the same accordion, but different groups.
    # We can just search globally for the spans that match the data-option-key
    for key, val in [('ssb-option-siding-color', 'Red'), ('ssb-option-trim-color', 'Clay'), ('ssb-option-roof-color', 'Red')]:
        spans = soup.find_all('span', {'data-option-key': key})
        for span in spans:
            span['class'] = [c for c in span.get('class', []) if c != 'active']
            if span.get('data-option-value') == val:
                span['class'] = span.get('class', []) + ['active']
                # Also update the selected text in the header of the accordion item
                wrapper = span.find_parent('div', class_='ssb-configurator-options')
                if wrapper:
                    selected_span = wrapper.find('span', class_='ssb-configurator-selected')
                    if selected_span:
                        selected_span.string = val
                        
    with open(file_path, 'w') as f:
        f.write(str(soup))

set_default_colors('public/v1/shedpro-design/product/garden-shed/index.html')
print("Default colors set successfully!")
