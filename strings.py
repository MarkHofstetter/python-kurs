text = 'Python ist super'

print(text + text)

print( (text + ' ') * 4 )

print( len(text) )

print( text.upper() )
print( text.lower() )

if 'PYTHON'.lower() in text.lower():  ## 'in' operator entspricht einem enthaelt/contains
  print('enthalten')
else:
  print('NICHT enthalten')
  
t2 = "Hier sind 'gaense' ""so"" enthalten"
print(t2)

print("Hier sind 'gaense' \"so\" %d%% enthalten" % 23.2) 

print(text[5:])

pos = text.find('s', 9)
print(pos)