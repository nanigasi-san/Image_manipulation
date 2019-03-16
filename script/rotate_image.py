from PIL import Image

image = Image.open("image/megane.jpg")
src = image.rotate(45)
src.save("image/rotate_megane.jpg","JPEG")
