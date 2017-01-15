import configparser
config = configparser.ConfigParser()
config.sections()

config.read('dict.ini')
config.sections()
dictonary = config['translation']
dictonary['hair'] = 'Haar'
for key in dictonary:
  print(key, dictonary[key])

wort = input("Uebersetze: ") 
if wort in dictonary:
  print(dictonary[wort])
