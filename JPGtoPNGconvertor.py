# Udemy exercise (231)
import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check is folder(new/) exists, if not create it
# loop through dir(Pokedex),
# convert jpg to png
# save to the new folder
if not os.path.exists(output_folder): '''when we write if os.path.exists(output_folder) it gives false, so to get opposite write if not'''
os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!') 

