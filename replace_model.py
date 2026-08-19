import re
from bs4 import BeautifulSoup

v2_path = "public/v2/product/premium-shed/index.html"
src_path = "temp_aframe.html"

with open(v2_path, "r", encoding="utf-8") as f:
    v2_html = f.read()

with open(src_path, "r", encoding="utf-8") as f:
    src_html = f.read()

# We don't want to use BS4 to write out the whole file because it might reformat or break our carefully placed V2 inline scripts/CSS.
# Instead, we can use string replacement or regex for the specific blocks.
# But regex for huge blocks of HTML is dangerous. 
# Better to use BS4 just to extract the new HTML strings, then use string replacement on the raw HTML.

src_soup = BeautifulSoup(src_html, "html.parser")
new_canvas_html = str(src_soup.find("canvas", id="ssb-canvas"))
new_config_html = str(src_soup.find(id="ssb-configurator"))

v2_soup = BeautifulSoup(v2_html, "html.parser")
old_canvas_html = str(v2_soup.find("canvas", id="ssb-canvas"))
old_config_html = str(v2_soup.find(id="ssb-configurator"))

if old_canvas_html in v2_html:
    v2_html = v2_html.replace(old_canvas_html, new_canvas_html)
    print("Replaced canvas")
else:
    print("Could not find exact old canvas string")

if old_config_html in v2_html:
    v2_html = v2_html.replace(old_config_html, new_config_html)
    print("Replaced config")
else:
    print("Could not find exact old config string")

with open(v2_path, "w", encoding="utf-8") as f:
    f.write(v2_html)
