import sys
import os
from PIL import Image

# grab first and second argument
path = sys.argv[1]
new_directory = sys.argv[2]


# check if the new folder exists, if not create it
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# loop through pokedex
# convert into png
for file in os.listdir(path):
    name = os.path.splitext(file)[0]
    # it splits the text, the filename and the image format or extension
    img = Image.open(f'{path}{file}')
    img.save(f'{new_directory}/{name}.png', 'png')

# save into new folder
print('Yay! Done!')