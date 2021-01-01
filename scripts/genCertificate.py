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
    certificateId = input("Enter certificate Id: ")
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
            value = input("Enter " + str(p['name']) + ": ")
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
    certificateName  = certificateName + '_' + str(certificateId) 
    img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/pictures/{}.jpg'.format(certificateName))

else :
    ### Get total values from CSV and draw them
    df = pd.read_csv('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/DataSheet/dataSheet.csv')
    for index,j in df.iterrows():
        certificateId = j['id']
        pathCertificateConfig = path + 'Configs/' + str(certificateId) + '.json'
        pathCertificate = path + 'certificates/' + str(certificateId) + '.jpg'
        certificateName = ''
        img = Image.open(pathCertificate)
        draw = ImageDraw.Draw(img)
        W, H = img.size
        i = 0
        with open(pathCertificateConfig) as json_file:
            data = json.load(json_file)
            for p in data['properties']:
                index = 'item' + str(i+1)
                value = j[index]
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
        certificateName  = certificateName + '_' + str(certificateId) 
        img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/pictures/{}.jpg'.format(certificateName))
