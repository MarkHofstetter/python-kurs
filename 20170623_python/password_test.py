'''
+ user soll einen Satz eingeben   / ++ mindenstens 8 woerter 
+ aus den anfangsbuchstaben soll ein passwort generiert werden 
  / ++ zwischen jedem buchstaben eine Zufallszahl, ohne letzte Ziffer
+ bsp Ich huepfe Ueber Stock und Stein => IhUSuS
'''

import wifi_password
# from wifi_password import generate_password
        
# main
  
input_sentence = 'Ich huepfe Ueber Stock und Stein'
password = wifi_password.generate_password( 
        sentence = input_sentence, 
        randomness = False 
        )

if password == 'IhUSuS':
    print('Alles OK')
else:
    print('Fehler')
    
input_sentence = 'Ich huepfe Ueber Stock und Stein'
try:
    password = wifi_password.generate_password(sentence = input_sentence, min_length = 7, randomness = False )
except ValueError as err:
    print('OK', err)
# ist das password = 'IhUSuS'
