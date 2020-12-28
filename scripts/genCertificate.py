from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import sys
import json

# TODO Validate certificate is present or not
# TODO Validate config file is present or not
# TODO Custom fonts access 
# TODO First Element is primary key
# TODO Certificate Naming Convention
# TODO Overflowing text shortening

generationType  =  sys.argv[1]
path = '/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/'

# Single or Bulk
if (generationType == "Single") :    
    certificateId = raw_input("Enter certificate Id: ")
    pathCertificate = path + 'certificates/' + certificateId + '.jpg'
    pathCertificateConfig = path + 'Configs/' + certificateId + '.json'
    certificateName = ''
    img = Image.open(pathCertificate)
    draw = ImageDraw.Draw(img)
    W, H = img.size
    i = 0
    with open(pathCertificateConfig) as json_file:
        data = json.load(json_file)
        for p in data['properties']:
            value = raw_input("Enter " + str(p['name']) + ": ")
            if (i == 0) :
                certificateName = value.replace(" ", "")
            x1 = int (p['x1'])
            x2 = int (p['x2'])
            y1 = int (p['y1'])
            y2 = int (p['y2'])
            fontSize = int(p['fontSize'])
            fontName = str(p['fontName'])
            font = ImageFont.truetype(fontName, fontSize)
            w, h = font.getsize(value)
            midXaxis = ((x2 -x1) / 2) + x1
            draw.text(xy=(midXaxis - w/2  ,y1 - h) ,text='{}'.format(value),fill=(0,0,0),font=font)
            i = i + 1
else :
    print ("Bulk")
    ### Get total values from CSV and draw them

certificateName  = certificateName + '_' + certificateId 
img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/pictures/{}.jpg'.format(certificateName))
