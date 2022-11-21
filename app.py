from PIL import Image
import random
import os
import os.path
######################################################################

# ALGORITHM


def generateArt():

    img = Image.new("RGB", (1200, 1000), "black")

    # creating collor pallette
    colors_num = random.randint(3, 6)
    colors = []
    for i in range(0, colors_num):
        colors.append((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255), random.randint(200, 255)))

    # implementing pixels into art
    for i in range(img.width):
        for j in range(img.height):
            img.putpixel((i, j), random.choice(colors))

    # display img
    img.show()

    # saving the image
    folder_name = "generated_art"
    folder_length = len([folder_name for folder_name in os.listdir(
        '.') if os.path.isfile(folder_name)])
    img = img.save(
        f"generated_art/art{folder_length*random.randint(1, 1000)}.png")


# call function
generateArt()
