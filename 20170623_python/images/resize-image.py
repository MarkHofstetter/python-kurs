from PIL import Image
from resizeimage import resizeimage

image_file = open('originals/persian-cats-and-kittens-1.jpg', 'rb')
img = Image.open(image_file)

img_small = resizeimage.resize_width(img, 200)
img_small.save('small_persian.jpg', img_small.format)
# img_small.show()
img_small.close()