#Code by Chase Gilbert, 2020
import sys
import random
import os, os.path
import time
import PIL
import textwrap
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps

#Set the font (replace path with correct path on your machine)
font = ImageFont.truetype("/path/to/fonts/DejaVuSansMono.ttf",30)

#Get a random caption 
#Replace path with correct path on your machine
#Each caption should be its own line in a txt file called 'captions.txt'
caption = (random.choice(open("/path/to/captions.txt").readlines())).rstrip('\n')

#Get the number of images in the image folder
#Replace path with correct path on your machine
#The images should all be jpg, with names 1 .. n
#For example, 1.jpg, 2.jpg, 3.jpg, etc
path, dirs, files = os.walk("/path/to/images").next()
file_count = len(files)

#Get a random image number
imageNumber = random.randint(1,file_count)

#Set the img variable to a random image
#Replace path with correct path on your machine
img = Image.open('/path/to/images/' + str(imageNumber) + '.jpg')

#Grab the dimensions of the image
size = img.size

#Set the wrap width
wrap = (size[0] / 19)

#Wrap if the string is too long
lines = textwrap.wrap(caption, width=wrap)

#Find the number of wrapped strings
line_count = 0
for line in lines:
	line_count = line_count + 1

#Set the whitespace scale factor
border_scale = line_count * 37

#Add a border to the image, and then crop it
img = ImageOps.expand(img,border=(0,border_scale),fill='white').crop((0,0,img.size[0],(img.size[1] + border_scale)))
draw = ImageDraw.Draw(img)

#Draw the wrapped text on the image
y_text = 0
for line in lines:
	width, height = font.getsize(line)
	draw.text((5,y_text), line,(0,0,0), font=font)
	y_text += height
draw = ImageDraw.Draw(img)

#Save the image
#Replace path with correct path on your machine
img.save('/desired/path/here/final_image_name.png')

#Short delay
time.sleep(2)


