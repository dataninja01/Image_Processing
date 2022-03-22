# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 09:24:57 2022

@author: mnagaraj
"""
from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
print(img)
print(img.format)
print(img.mode)
print(img.size)
print (dir(img.format))
#####the images in png support image filters jpg does not

filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.save("./pokedex/blur.png", 'png')

filtered_img = img.filter(ImageFilter.SMOOTH)

filtered_img.save("./pokedex/smooth.png", 'png')

filtered_img = img.filter(ImageFilter.SHARPEN())

filtered_img.save("./pokedex/sharpen.png", 'png')

filtered_img = img.filter(ImageFilter.SMOOTH)

filtered_img.save("./pokedex/smooth.png", 'png')

filtered_img = img.convert('L')

filtered_img.save("./pokedex/grey.png", 'png')

filtered_img.show()

crooked = filtered_img.rotate(180)
crooked.save("./pokedex/grey_crooked.png", 'png')

resize = filtered_img.resize((300, 300))
resize.save("./pokedex/grey_crooked_RESIZED.png", 'png')

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.show()

astro = Image.open('./astro.jpg')

print(astro.size)

new_img = astro.resize((300, 300))
new_img.show()

####to keep the aspect ratio of the image we use thumbnail

astro.thumbnail((400, 400))
astro.save('thumbnail.jpg')

