from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import sys
import json

# Interfaced customization
# Names and Texts to be picked up from text File
# Configurable Text fields from config_certificate_id
# create box to fill the text and value.
# If text size overflow from box size then reduce text size and name shortening.
# Datasheet pass on runtime

generationType  =  sys.argv[1]
path = '/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/'

#### Single or Bulk
if (generationType == "Single") :
    # Use Certificate Id to get config.
    # Check certificate.json is present or not
    certificateId = raw_input("Enter certificate Id: ")
    pathCertificateConfig = path + 'Configs/' + certificateId + '.json'
    with open(pathCertificateConfig) as json_file:
        data = json.load(json_file)
        img = Image.open('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/certificates/4572.png')
        W, H = img.size
        draw = ImageDraw.Draw(img)
        for p in data['properties']:
            value = raw_input("Enter " + str(p['name']) + ": ")
            x1 = int (p['x1'])
            x2 = int (p['x2'])
            y1 = int (p['y1'])
            y2 = int (p['y2'])
            fontSize = p['fontSize']
            fontName = int(p['fontSize'])
            font = ImageFont.truetype('GreatVibes-Regular.ttf', 96)
            w, h = font.getsize(value)
            midXaxis = ((x2 -x1) / 2) + x1
            draw.text(xy=(midXaxis - w/2  ,y1 - h),text='{}'.format(value),fill=(0,0,0),font=font)
    
else :
    print ("Bulk")
    ### Get total values from CSV and draw them



img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/pictures/{}.jpg'.format(value))
