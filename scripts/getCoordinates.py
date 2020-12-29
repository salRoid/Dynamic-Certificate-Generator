import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def onclick(event): 
    print("button=%d, x=%d, y=%d, xdata=%f, ydata=%f" % ( 
         event.button, event.x, event.y, event.xdata, event.ydata)) 

certificateName = sys.argv[1]
certificateId = certificateName.split('.')[0]
path = '/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/'
pathCertificate = path + 'certificates/' + certificateId + '.jpg'

img = mpimg.imread(pathCertificate)
fig, dx = plt.subplots()
dx.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax = plt.imshow(img)
fig = ax.get_figure()

cid = fig.canvas.mpl_connect('button_press_event', onclick) 
plt.show()