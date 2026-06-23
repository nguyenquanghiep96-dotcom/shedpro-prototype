from bs4 import BeautifulSoup

def perfect_clone():
    print("Reading files...")
    with open('public/v1/shedpro-design/product/garden-shed/index.html', 'r') as f:
        garden = BeautifulSoup(f.read(), 'html.parser')
        
    with open('public/v1/shedpro-design/product/chalet/original_chalet.html', 'r') as f:
        chalet_orig = BeautifulSoup(f.read(), 'html.parser')
        
    print("Cloning 3D data...")
    # 1. Swap js-shed-data
    garden_shed_data = garden.find(id='js-shed-data')
    orig_shed_data = chalet_orig.find(id='js-shed-data')
    if garden_shed_data and orig_shed_data:
        garden_shed_data.replace_with(orig_shed_data)
        
    # 2. Swap hidden inputs that configure the runner/door positions
    # They are usually right before <div class="overlay"> or at the bottom of the form
    # We will just find all <input type="hidden" id^="js-"> in original and append them
    # First, remove existing ones from garden
    for inp in garden.find_all('input', {'type': 'hidden', 'id': lambda x: x and x.startswith('js-')}):
        if inp.parent.get('id') != 'js-shed-data':
            inp.decompose()
            
    # Now find them in orig and copy them
    form = garden.find('form', class_='ssb-configurator-details-form')
    for inp in chalet_orig.find_all('input', {'type': 'hidden', 'id': lambda x: x and x.startswith('js-')}):
        if inp.parent.get('id') != 'js-shed-data':
            if form:
                form.append(inp)
                
    # 3. Swap accordion contents (Everything EXCEPT Style Tab)
    accordions_to_swap = [
        'ssb-configurator-accordion-layouts',
        'ssb-configurator-accordion-sizes',
        'ssb-configurator-accordion-appearance',
        'ssb-configurator-accordion-materials',
        'ssb-configurator-accordion-colors',
        'ssb-configurator-accordion-upgrades',
        'ssb-configurator-accordion-upgrades-new',
        'ssb-configurator-accordion-interior'
    ]
    
    for acc_id in accordions_to_swap:
        g_acc = garden.find(id=acc_id)
        c_acc = chalet_orig.find(id=acc_id)
        if g_acc and c_acc:
            g_acc.replace_with(c_acc)
        elif c_acc and not g_acc:
            # If chalet has an accordion garden doesn't, append it
            wrapper = garden.find(id='ssb-configurator-accordion')
            if wrapper:
                wrapper.append(c_acc)
                
    # 4. Update Style Tab Active State
    style_tab = garden.find('ul', class_='ssb-shed-options ssb-type-shedpro')
    if style_tab:
        for li in style_tab.find_all('li'):
            li['class'] = [c for c in li.get('class', []) if c != 'active']
            if 'Chalet' in li.text:
                li['class'] = li.get('class', []) + ['active']
                
    # 5. Fix titles
    if garden.title:
        garden.title.string = "Chalet - [Master] ShedPro Demo"
        
    product_title = garden.find('h1', class_='product_title')
    if product_title:
        product_title.string = "Chalet"

    print("Saving perfect clone...")
    with open('public/v1/shedpro-design/product/chalet/index.html', 'w') as f:
        f.write(str(garden))
        
    print("Perfect clone created successfully!")

perfect_clone()
