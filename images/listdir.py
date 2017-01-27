import os

for filename in os.listdir('orig'):
  #  if filename.endswith(".asm") or filename.endswith(".py"): 
  print(os.path.join('orig', filename))
