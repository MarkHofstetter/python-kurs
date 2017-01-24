# zusatz
# der benutzer wird nach Woertern gefragt, und am Ende wird das 
# laengste Wort ausgegeben abbruch durch eingabe von "ende"

# wort.rstrip() # entfernt letztes Zeichen, ist nicht notwendig
import re

wortmax = None
wortmaxlen = 0

wort = ''
while wort.lower() != 'ende':
  wort = input('Bitte Wort eingeben: ')
  m = re.search(r'\d', wort)
  if m:
    print("enthaelt Zahlen")       
    continue
  if len(wort) > wortmaxlen:
    wortmaxlen = len(wort)
    wortmax = wort
  

print(wortmax, wortmaxlen)    
  
# try:
#    z = float(wort)
#    zahl = True
#  except TypeError:
#    zahl = False
#  if zahl:
#    print("kein Wort")
#  
#  