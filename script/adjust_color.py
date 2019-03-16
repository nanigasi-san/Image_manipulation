from PIL import Image
image = Image.open("image/megane.jpg")

src = image.quantize(3)
src.save("image/magane_3color.png","PNG")

src = image.quantize(5)
src.save("image/magane_5color.png","PNG")
