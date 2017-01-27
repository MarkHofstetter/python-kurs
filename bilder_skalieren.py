from PIL import Image
from resizeimage import resizeimage

quellbild = open('bilder/trump_wissenschaft_widerstand_2h_n.4735323.jpg', 'rb')
img = Image.open(quellbild) 
breite, hoehe = img.size
print(breite, hoehe)
img = resizeimage.resize_width(img, 100)
img.save("%dx%d_bla.jpg" % (breite, hoehe), img.format)
img.close()