'''
+ zufallszahl zw 0-100 ermitteln
+ maximal x zb 6 Versuche
+ user rät und bekommt entweder
    + richtig 
    + zu hoch/niedrig
+ lt auftraggeber zaehlen fehleingaben nicht zu den versuchen    
'''    

import random

random_number = random.randint(0,100)

i = 1
while i <= 10:
    try:
        user_input = int( input(str(i) + ' bitte eine Zahl eingeben: ') )
    except ValueError:
        print("das war keine zahl du dolm")
        continue
        
    if user_input == random_number:
        print('Super nach',i,'Versuchen')
        break
    elif user_input > random_number:
        print('zu hoch') 
    else:    
        print('zu niedrig')
    i += 1
else:
    print('leider nix',random_number,'waere richtig gewesen')

print('danke fürs spielen')
    