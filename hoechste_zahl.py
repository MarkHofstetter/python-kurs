# der benutzer wird nach zahlen gefragt
# mit eingabe von 0 (null) wird die schleife 
# beendet, danach wird die hoechste Zahl ausgegeben
# 5, 34, 7, 9, 12 => Ausgabe 34

max = 0
eingabe = None
while eingabe != 0:
  eingabe = int(input('Bitte Zahl eingeben: '))	
  if eingabe > max:
    max = eingabe

print(max)    
