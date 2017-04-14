# spiel: 
# programm ermittelt eine Zufallszahl (0-100) die der Spieler erraten muss 
# das Programm liefert Hinweise ob die Zahl groesser oder kleiner  
# ist als die gesuchte Zahl 
# wenn die Zahl erraten wurde wird dies angezeigt und das Programm beendet 
# nach spätestens 10 (oder 5) Versuchen wird das Programm beendet 

import random

zielzahl = random.randint(1,100)

print(zielzahl)

gewonnen = False

for i in range(1,6):
    eingabe = int(input("bitte raten: "))
    if eingabe == zielzahl:
        # print("Gewonnen nach",i,"Versuchen")
        print("Gewonnen nach %d Versuchen" % (i))
        gewonnen = True
        break
    elif eingabe > zielzahl:
        print("eingabe zu gross")
    elif eingabe < zielzahl:
        print("eingabe zu klein")
else:        
    print("Verloren richtige Zahl ", zielzahl)        

print("now for something ...")    
#if not gewonnen: 
#    print("Verloren richtige Zahl ", zielzahl)        

""" 
zz = 78

spieler rät 50
programm sagt zz ist groesser

spieler rät 80
programm sagt zz ist kleiner


"""

