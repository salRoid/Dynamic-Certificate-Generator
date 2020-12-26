from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Interfaced customization
# Names and Texts to be picked up from text File
# Configurable Text fields from config_certificate_id
# create box to fill the text and value.
# If text size overflow from box size then reduce text size and name shortening.
# Datasheet pass on runtime

name = "Sajal Gupta"
font = ImageFont.truetype('GreatVibes-Regular.ttf', 96)
img = Image.open('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/certificates/4571.jpg')
W, H = img.size
draw = ImageDraw.Draw(img)
w, h = font.getsize(name)
draw.text(xy=((W - w)/2 ,500),text='{}'.format(name),fill=(0,0,0),font=font)
img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/pictures/{}.jpg'.format(name))
