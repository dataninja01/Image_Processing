# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 09:52:47 2022

@author: mnagaraj
"""
import sys
import os
from PIL import Image

# check if the new folder exists if not create one
image_folder = sys.argv[1]

output_folder = sys.argv[2]

print(image_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    image_name = clean_name[0]
    print(clean_name)
    print(image_name)
    img.save(f'{output_folder}{image_name}.png', 'png')
    print('all done')