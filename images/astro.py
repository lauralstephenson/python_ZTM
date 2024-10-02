#change an astro image
#import PIL from pillow
from PIL import Image, ImageFilter

#open image
img = Image.open("./astro.jpg")
#find out image size

print(img.size)
#resize image
new_img = img.resize((400, 400))
#you'll lose the aspect ratio. 
#use the thumbnail command that alters
#the image itself
img.thumbnail((400, 400))
#must save it
img.save("thumbnail.jpg")