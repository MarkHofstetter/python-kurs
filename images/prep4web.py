import shutil
from PIL import Image
from resizeimage import resizeimage

fd_img = open('orig/IMG_4769.jpg', 'rb')
img = Image.open(fd_img)
img = resizeimage.resize_width(img, 200)
img.save('resize/test-image-width.jpeg', img.format)
img.close()
