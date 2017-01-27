import os
import shutil

i = 1
pfad = 'bilder'
for filename in os.listdir(pfad):
  if filename.endswith(".jpg"):
    print("is jpg")
  fullname = os.path.join(pfad, filename) ## macht im Prinzip pfad + '/' + filename
  print(fullname)
  # shutil.copy(fullname, str(i)+'.jpg')  
  try:
    shutil.copy(fullname, filename.upper())  
  except OSError:
    print("fehler beim kopieren")
  i += 1
  