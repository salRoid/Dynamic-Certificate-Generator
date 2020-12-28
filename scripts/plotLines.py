from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys
import os 

# TODO Please don't remove the original certificate 

certificateName = sys.argv[1]
certificateId = certificateName.split('.')[0]

path = '/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/'
pathCertificate = path + "certificates/" 
originalCertificate = path + "certificates/" + certificateName
finalCerticate = path + "certificates/" + certificateId + ".jpg"

#converting file format to png
tempCertificateName = "/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/certificates/temp_" + certificateId + ".jpg"
img = Image.open(originalCertificate)
img.save(tempCertificateName)

# Remove Original Certificate and rename temp certificate
if os.path.exists(originalCertificate):
  os.remove(originalCertificate)
  os.rename(tempCertificateName,finalCerticate) 
else:
  print("The file does not exist")

# Work on final certificate
img = Image.open(finalCerticate)
draw = ImageDraw.Draw(img)
W, H = img.size
boxWidth = int(W / 32)
boxHeight = int(H / 32)

# Plot Horizontal and Vertical lines
for x in range(0, W, boxWidth):
  draw.line((x, 0, x, H), fill = "red", width = 2)
for x in range(0, H, boxHeight):
  draw.line((0, x, W, x), fill = "red", width = 2)

# Expand Image and plot numbers on XY axis
img = ImageOps.expand(img, border = boxWidth, fill = 128)
draw = ImageDraw.Draw(img)

for x in range(boxWidth , W, boxWidth):
    draw.text(xy=(x, boxHeight),text='{}'.format(x - boxWidth),fill=(0,0,0))
for x in range(boxHeight , H, boxHeight):
    draw.text(xy=(boxWidth - 30, x),text='{}'.format(x - boxHeight),fill=(0,0,0))

img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/plotCertificates/plot_{}.jpg'.format(certificateId))
