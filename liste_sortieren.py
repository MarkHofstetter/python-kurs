# wir wollen eine liste "haendisch" sortieren

b = [3,6,2,3,6,4,5,8]

# die ganze Liste nach dem maximalen wert durchsuchen
# diesen wert rausschreiben und aus der Liste entfernen
# solange wiederholen bis die Liste leer ist
# dieser Algorithmus ist sehr ineffizient

def findMax(a):
  max = 0
  for z in a:
    if z > max:
      max = z
  print(max)
  a.remove(max)
  return a
  
while len(b) > 0:
   b = findMax(b)
