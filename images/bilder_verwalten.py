# das prg nimmt einen quellordner und einen zielordner
# (idealerweise aus eine configdatei)

# das prg iteriert über alle jpg - dateien des quellordners
# und speichert die dateien verkleinert 
# (auf welche groesse ebenfalls aus der configdatei) in den zielordner
# namen kann gleich gleich bleiben oder zb mit "klein_" vorangestellt werden

import os
import shutil
import configparser
from PIL import Image
from resizeimage import resizeimage

config = configparser.ConfigParser()
config.sections()
config.read('bilder.ini')
pfade = config['pfade']
zielwerte = config['zielwerte']

for filename in os.listdir(pfade['quellpfad']):
  if not filename.endswith(".jpg"):
    continue
    
  fullname = os.path.join(pfade['quellpfad'], filename)
  print(fullname)    
  quellbild = open(fullname, 'rb')
  img = Image.open(quellbild) 
  breite, hoehe = img.size
  zielname = "%s_%s_%s" \
      % (zielwerte['praefix'], zielwerte['breite'], filename)
  if breite > int(zielwerte['breite']):
    img = resizeimage.resize_width(img, int(zielwerte['breite']))       
  img.save(os.path.join(pfade['zielpfad'], zielname), img.format)
  img.close()