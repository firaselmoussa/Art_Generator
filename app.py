from PIL import Image


def flag(c, w=100, h=100):
    c1, c2, c3 = c.split()
    img = Image.new("RGB", (w*3, h), c1)
    lay1 = Image.new("RGB", (w, h), c2)
    lay2 = Image.new("RGB", (w, h), c3)
    img.paste(lay1, (w, 0))
    img.paste(lay2, (w*2, 0))
    img.show()
    img = img.save("generated_art/img.png")


flag("gold blue pink", 200, 350)
