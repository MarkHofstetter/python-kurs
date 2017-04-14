import re

# gueltig
a = [
      'a1234',
      'A1234',
      'A-2134',
      'a    2134',
      'a2134',
      '1234',
      '    1234   ',
      '  A1234',
    ]

c = { 
       'a1234': True,
       '123'  : False,
    }    
    
# nicht gueltig    
b = [ 
      '123',
      '12345',
      '12a12',
      '11 32',
      'B1234',
    ]    

plz = '   1113'

m = re.search(r'^[Aa]{0,1}[-\s]{0,1}\d{4}$', plz)
if m:
    print('ist eine PLZ')
else:
    print('*** ist KEINE PLZ')



