#Program that processes images

#First, import an image processing library
from PIL import Image, ImageFilter

#this opens the pic
img = Image.open("./Pokedex/pikachu.jpg")

#this finds the image
print(img)
#this finds the image format
print(img.format)
#this finds the size
print(img.size)
#this finds the coloring, like RGB
print(img.mode)
#this allows you to find out all the 
#things you can do to the img
#in this library (so much stuff) 
#or read the documetation
print(dir(img)) 
#filter blur and convert to PNG
#PNG accepts filters
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

#filter smooth--opposite of blur
#works better with landscape images
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img2.save("smooth.png", "png") 

#filtered sharpen
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img3.save("sharp.png", "png")

#img.convert() converts the image 
#to different formats--PNG is best for filters
#show the image
filtered_img.show()
#img.convert("L") is greyscale
filtered_img = img.convert("L")
#rotate image
crooked = filtered_img.rotate(90)
crooked.save("grey.png", "png")
#resize images
resize = filtered_img.resize((300, 300))
resize.save("grey.png", "png")
#cropping an image
#need a 4 tuple for the size
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", "png")

img = Image.open("./Pokedex/astro.jpg")
print img.size
new_img = img.resize((400, 400))
resize.save("astro_small.png", "png")