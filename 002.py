from PIL import Image
from pylab import *

image = array(Image.open('panda.jpg'))
imshow(image)

x = [100,100,40,40]
y = [20,50,20,50]


#plot(x,y)
plot(x,y, 'r*')

#plot(x,y, 'go-')
#plot(x,y, 'ks:')

#plot(x[:2], y[:2]) #100,100,20,50

title('PANDA')

show()