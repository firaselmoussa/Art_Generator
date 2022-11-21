from PIL import Image
import random


def generateArt():

    img = Image.new("RGB", (1200, 1000), "black")

    for i in range(img.width):
        for j in range(img.height):
            img.putpixel((i, j), (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255), random.randint(0, 255)))

    img.show()
    img = img.save("generated_art/img1.png")


generateArt()
