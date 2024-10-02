#JPG to PNG Pokedex Converter
import sys
import os
from PIL import Image

#grab first and second argument 
# using sys module
#first argument is current folder /Pokedex
image_folder = sys.argv[1]
#second argument is second folder new\
output_folder = sys.argv[2]
#check if \new exists. If not, create it. 
# Use os module.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through Pokedex folder 
#convert images to PNG using PIL
for filename in os.listdir(image_folder):
    #need to remove the .jpg from filename
    #to save it as png
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)
    #testing to see if it made a clean
    #name, delete before using
    print(clean_name)
    #save the file to a new folder
    img.save(f"{output_folder}{filename}.png", "png")
    print("All done!")




