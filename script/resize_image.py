from PIL import Image

image = Image.open("image/megane.jpg")

src = image.resize((16,16))
src.save("image/megane_resize16.png","PNG")

src = image.resize((256,256))
src.save("image/megane_resize256.png","PNG")

src = image.resize((100,500))
src.save("image/megane_resize100x500.png","PNG")
