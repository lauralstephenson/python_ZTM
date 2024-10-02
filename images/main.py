#JPG to PNG Pokedex Converter
from PIL import Image, ImageFilter

#this opens the pic
img = Image.open("./Pokedex/pikachu.jpg")

#this finds the image
print(img)
#this finds the image format
print(img.format)

#img.convert() converts the image 
#to different formats--PNG is best for filters
#show the image
filtered_img.show()
filtered_img = img.convert("JPG, PNG")
