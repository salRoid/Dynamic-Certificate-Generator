from PIL import Image, ImageDraw, ImageFont, ImageOps

name = "4571"
img = Image.open('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/certificates/4571.jpg')
W, H = img.size
draw = ImageDraw.Draw(img)
for x in range(0, W, 30):
  draw.line((x, 0, x, H), fill = "red", width = 2)
for x in range(0, H, 30):
  draw.line((0, x, W, x), fill = "red", width = 2)

#old_size = img.size
#new_size = (W + 50, H + 50)
#new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
#new_im.paste(img, ((new_size[0]-old_size[0])/2,
#                      (new_size[1]-old_size[1])/2))

#img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/plotCertificates/{}.jpg'.format(name))
#new_im.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/plotCertificates/{}.jpg'.format(name))

new_img = ImageOps.expand(img, border = 30, fill = 128)

font = ImageFont.truetype('GreatVibes-Regular.ttf', 10)
draw1 = ImageDraw.Draw(new_img)


for x in range(30 , W, 30):
    draw1.text(xy=(x, 18),text='{}'.format(x - 30),fill=(0,0,0))

for x in range(30 , H, 30):
    draw1.text(xy=(10, x),text='{}'.format(x - 30),fill=(0,0,0))

#img_with_border = ImageOps.expand(img, border = 50, fill = (255, 255, 255))
new_img.save('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/plotCertificates/{}.jpg'.format(name))
