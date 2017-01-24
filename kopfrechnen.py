# kopfrechen
# der benutzer bekommt 2 unterschiedliche zufallszahlen jeweils im Bereich 1 - 10
# die muss der Benutzer multiplizieren
# und es wird ueberprueft ob die aufgabe richtig geloest wurde

# zusatz
# 10 verschiedene Aufgaben stellen und sich merken 
# wieviel richtig und falsch waren
# funktion?

import random

def aufgabe(max):
  a1 = random.randint(1,10)
  a2 = random.randint(1,max)
  print("Wieviel ist %d * %d" % (a1, a2))  
  eingabe = int(input('Bitte Zahl eingeben: '))
  print(eingabe, a1*a2)
  t = False
  if eingabe == a1*a2:
    t = True
  return t
# ende funktion  
  
# main  
richtig = 0
falsch  = 0
for i in range(0,5):
  t = aufgabe(3) # evtl auch vom Benutzer lesen
  # if t: # ist gleichbedeutend mit
  # if t == True:
  if t is True:
    richtig += 1
  else:
    falsch += 1

print("Du hast %d Aufgaben richtig" % richtig)   # oder mit format 
print("Du hast " + str(falsch) +" Aufgaben falsch")   # so eher nicht 
  

	