from skimage import io,color,filters
image = io.imread("image/megane.jpg")
gray = color.rgb2gray(image)
io.imshow(gray)
io.show()
ggray = filters.gaussian(gray,sigma=4)
io.imshow(ggray)
io.show()
bin = ggray<0.5
io.imshow(bin)
io.show()

bin2 = gray < filters.threshold_otsu(ggray)
io.imshow(bin2)
io.show()
