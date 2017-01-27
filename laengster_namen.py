## mit Hilfe einer for loop (Schleife) ueber die Listen
## iterieren und den laengsten Namen ermitteln und ausgeben


teilnehmer = ['Michael',
              'Herbert', 
              'Adrian', 
              'Daniel',              
              'Johannes',
              'Martin',              
              'Stefan',              
             ]
             
def getLongestElement(liste):
  maxLength = 0
  maxLengthElement = ''
  for element in liste:
    if len(element) > maxLength:
      maxLength = len(element)        
      maxLengthElement = element
  return (maxLength, maxLengthElement)

# Loesung fuer mehrere gleichlange kuerzeste Namen
def getShortestElements(liste):
  minLength = float('inf')
  minLengthElements = []
  for element in liste:
    if len(element) < minLength:
      minLengthElements = [element]
      minLength = len(element)
    elif len(element) == minLength:
      minLengthElements.append(element)
  return (minLength, minLengthElements)      
  
## main  
  
(maxLength, maxLengthName)  = getLongestElement(teilnehmer)
(minLength, minLengthNames) = getShortestElements(teilnehmer)

print("Der laengste Name lautet %s mit einer Laenge von %d" 
   % (maxLengthName, maxLength) )
   
print("Die kuerzesten Namen lauten %s mit einer Laenge von %d" 
   % (minLengthNames, minLength) )   
   
   