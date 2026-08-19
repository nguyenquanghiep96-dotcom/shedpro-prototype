from bs4 import BeautifulSoup

with open("public/v2/product/premium-shed/index.html", "r", encoding="utf-8") as f:
    v2_soup = BeautifulSoup(f.read(), "html.parser")

with open("temp_aframe.html", "r", encoding="utf-8") as f:
    src_soup = BeautifulSoup(f.read(), "html.parser")

v2_canvas = v2_soup.find("canvas", id="ssb-canvas")
src_canvas = src_soup.find("canvas", id="ssb-canvas")

v2_config = v2_soup.find(id="ssb-configurator")
src_config = src_soup.find(id="ssb-configurator")

v2_cart = v2_soup.find("form", class_="cart ssb-builder-options")
src_cart = src_soup.find("form", class_="cart")

print("V2 canvas exists:", v2_canvas is not None)
print("Src canvas exists:", src_canvas is not None)

print("V2 config exists:", v2_config is not None)
print("Src config exists:", src_config is not None)

print("V2 cart exists:", v2_cart is not None)
print("Src cart exists:", src_cart is not None)

if v2_cart and src_cart:
    print("V2 config inside cart:", v2_cart.find(id="ssb-configurator") is not None)
    print("Src config inside cart:", src_cart.find(id="ssb-configurator") is not None)
