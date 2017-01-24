def getIntInput():
   try:    
     a = int(input('Bitte Zahl eingeben: '))	
     return a
   except:
     print("Falscher Wert")
     return False