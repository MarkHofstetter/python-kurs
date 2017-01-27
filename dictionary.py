teilnehmer = [ 
               ['Adrian', 180, 'blau'],
               ['Daniel', 177, 'blau'],
               ['Eva'   , 168, 'rot'],
             ]

             
suche = 'Daniel'             
for tn in teilnehmer:
  if tn[0] == suche:
    print("Teilnehmer %s hat Lieblingsfarbe %s" % (tn[0], tn[2]) )
    

## dictionary, hash, assoziativer array    

dict_teilnehmer = {
#   schluessel  wert
#      key      value
      'Adrian': 180,
      'Daniel': 177,
      'Eva'   : 168,
      'Daniel': 176,
   }

dict_vortragender = {
      'Mark': 175,
      'Daniel': 178,
   }
   
dict_teilnehmer['Adrian'] = 181

try:
  #print(b)
  print( dict_teilnehmer['Mark'] )     
except KeyError:
  print("kein tn unter diesem key")

if "Mark" in teilnehmer:
  print( dict_teilnehmer['Mark'] )     
else:
  print('gibt es nicht')

dict_teilnehmer.update(dict_vortragender)
print(dict_teilnehmer)
  
print( dict_teilnehmer['Daniel'] )   
print( dict_teilnehmer['Adrian'] )   

exit()

dict_teilnehmer_komplex = {
#   schluessel  wert
#      key      value
      'Adrian': { 'groesse': 180, 'alter': 32, 'emails': ['a@b', 'c@d'] },
      'Daniel': 177,
      'Eva'   : 168,
      'Daniel': 176,
   }

print(dict_teilnehmer_komplex)
print( dict_teilnehmer_komplex['Adrian']['emails'] )   


luefter = {  
  12: {75: False, 60: True},
  10: {70: False, 60: True},
   2: {50: True},
  -2: {80: True}
 }
   
# tdiff 10.45 => 10 
# lf = 71.2   => 70
a = 12
b = 75
c = luefter[a][b]
print(c)
print(luefter[12][60])