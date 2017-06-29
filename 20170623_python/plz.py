import re

# plz = input('bitte plz eingeben: ')

'''
A-1234
A1232
A 1234
a2134
'''
# gueltig
a = [
      'a1234',
      'A1234',
      'A-2134',
      'a    2134',
      'a2134',      
      '  A1234  ',
    ]
    
# nicht gueltig    
b = [ 
      '123',
      '1234',
      '    1234   ',
      '12345',
      '12a12',
      '11 32',
      'B1234',
    ]    


for plz in a + b:  
    plz = plz.strip()
    plz = re.sub(r'\s+', ' ', plz)
    matches = re.search(r'^[Aa][- ]{0,1}\d{4}$', plz)
    if matches:
        print(plz, 'ist eine Postleitzahl')
    else:
        print(plz, 'ist KEINE Postleitzahl')

