from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

name = "Sajal Gupta"
font = ImageFont.truetype('GreatVibes-Regular.ttf', 96)
img = Image.open('4571.jpg')
W, H = img.size
draw = ImageDraw.Draw(img)
w, h = font.getsize(name)
print (W - w)
draw.text(xy=((W - w)/2 ,500),text='{}'.format(name),fill=(0,0,0),font=font)
img.save('pictures/{}.jpg'.format(name))
