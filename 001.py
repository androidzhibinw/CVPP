from PIL import Image

img = Image.open('panda.jpg')
print img.format, img.size, img.mode
img = img.convert('L')
img = img.rotate(90)
img.thumbnail((64,64))
img = img.resize((1000,1000))
img.show()
#img.save('001.png')