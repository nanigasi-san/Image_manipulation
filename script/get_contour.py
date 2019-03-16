from PIL import Image,ImageFilter

image = Image.open("image/megane.jpg")

src = image.filter(ImageFilter.CONTOUR)
src.save("image/megane_contour.png","PNG")
