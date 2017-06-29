'''
+ alle bilder aus dem verzeichnis 'originals' resizen /
+ und in ein verzeichnis 'resized' abspeichern /

++ alle veränderlichen parameter, wie zb das Verzeichnis die bildergröße etc aus einem configfile holen /
++ den bildernamen von xxxx.jpg > xxxx_small.jpg aendern
(++ testbar?!)
'''

import configparser
import os
from PIL import Image
from resizeimage import resizeimage

config = configparser.ConfigParser()
config.read('automate-resize.ini')
config.sections()
directories = config['directories']
imageparam = config['imageparam']

for filename in os.listdir(directories['source']):
    image_file = open(os.path.join(directories['source'], filename), 'rb')
    # image_file = open( directories['source'] + '/' + filename, 'rb') # funktioniert
    img = Image.open(image_file)
    img_small = resizeimage.resize_width(img, int(imageparam['width']))
    name, ext = os.path.splitext(filename)    
    img_small.save(os.path.join(directories['destination'], name+'_small'+ext), img_small.format)    
    img_small.close()
