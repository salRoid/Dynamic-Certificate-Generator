from PIL import Image, ImageDraw, ImageFont, ImageOps

## Should be Interfaced for easy customization
# File Name to picked from certificate name || Can run for all certificates in folder
# plot_certificate_id for naming convention
# environment variables for path
# plot line color
# plot line width
# plot pixel size
# plot generation called at run time

name = "4571"
img = Image.open('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/certificates/4571.jpg')
W, H = img.size
draw = ImageDraw.Draw(img)
for x in range(0, W, 30):
  draw.line((x, 0, x, H), fill = "red", width = 2)
for x in range(0, H, 30):
  draw.line((0, x, W, x), fill = "red", width = 2)
img = ImageOps.expand(img, border = 30, fill = 128)
draw = ImageDraw.Draw(img)
for x in range(30 , W, 30):
    draw.text(xy=(x, 18),text='{}'.format(x - 30),fill=(0,0,0))
for x in range(30 , H, 30):
    draw.text(xy=(10, x),text='{}'.format(x - 30),fill=(0,0,0))
img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/plotCertificates/{}.jpg'.format(name))
