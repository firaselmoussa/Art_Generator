from PIL import Image
import random
import os
import os.path


def generateArt():

    img = Image.new("RGB", (1200, 1000), "black")

    # creating collor pallette
    colors_num = random.randint(3, 6)
    colors = []
    for i in range(0, colors_num):
        colors.append((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255), random.randint(200, 255)))

    for i in range(img.width):
        for j in range(img.height):
            img.putpixel((i, j), random.choice(colors))

    img.show()


generateArt()
