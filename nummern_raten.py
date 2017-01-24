# spiel:
# programm ermittelt eine Zufallszahl die der Spieler erraten muss
# das Programm liefert Hinweise ob die Zahl greosser oder kleiner 
# ist als die gesuchte Zahl
# wenn die Zahl erraten wurde wird dies angezeigt und das Programm beendet
# nach spätestens 10 (oder 5) Versuchen wird das Programm beendet

import random
import MyInput

zz = random.randint(1,100)
print(zz)

for i in range(0,5):
   a = MyInput.getIntInput() 
   if a == False:      ## geht zurueck an den Schleifenbeginn, 0 Werte extra abhandeln!!
     continue          
   if a < zz:
     print("zu klein")
   elif a > zz:
     print("zu gross")
   else:
     print("Gewonnen! nach " + str(i)+ " Versuchen")
     print("Gewonnen! nach {0:d} Versuchen".format(i))
     exit()

print("verloren!")     
   
   
