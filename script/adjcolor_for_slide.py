from PIL import Image
image = Image.open("image/megane.jpg")

def make_image(color_n):
    src = image.quantize(color_n)
    src.save("image/magane_{0}color.png".format(color_n),"PNG")

"""
動きません
make_image(810)
make_image(666)
make_image(334)
make_image(512)
"""
make_image(72)
