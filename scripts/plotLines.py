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

# Plot Horizontal and Vertical lines
for x in range(0, W, 30):
  draw.line((x, 0, x, H), fill = "red", width = 2)
for x in range(0, H, 30):
  draw.line((0, x, W, x), fill = "red", width = 2)

# Expand Image and plot numbers on XY axis
img = ImageOps.expand(img, border = 30, fill = 128)
draw = ImageDraw.Draw(img)

for x in range(30 , W, 30):
    draw.text(xy=(x, 18),text='{}'.format(x - 30),fill=(0,0,0))
for x in range(30 , H, 30):
    draw.text(xy=(10, x),text='{}'.format(x - 30),fill=(0,0,0))

img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/plotCertificates/plot_{}.jpg'.format(certificateId))
