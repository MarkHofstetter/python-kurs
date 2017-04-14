"""
das Programm soll 
+ 2 zufallszahlen zwischen 1-10 ausgeben
+ der Benutzer soll das Produkt eingeben
+ danach Ausagabe ob richtig oder falsch

+ show two random numbers between 1-10
+ the user shall input the product of those two numbers
+ the program says right or wrong

"""

import random

faktor1 = random.randint(1,10)
faktor2 = random.randint(1,10)

print("Wieviel ist " + str(faktor1) + " mal " + str(faktor2))
# achtung die variable eingabe ist ein string
eingabe = input('Gib bitte eine Zahl ein: ')
eingabe = int(eingabe)
if eingabe == faktor1 * faktor2:
    print('Richtig')
else:
    print('Falsch ' + str(faktor1 * faktor2) + ' ist richtig')
    print('Falsch', faktor1 * faktor2, 'ist richtig')
    
# dh man muss konvertieren dh int(eingabe)


