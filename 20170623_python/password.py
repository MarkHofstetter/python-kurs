'''
+ user soll einen Satz eingeben   / ++ mindenstens 8 woerter 
+ aus den anfangsbuchstaben soll ein passwort generiert werden 
  / ++ zwischen jedem buchstaben eine Zufallszahl, ohne letzte Ziffer
+ bsp Ich huepfe Ueber Stock und Stein => IhUSuS
'''

import wifi_password
# from wifi_password import generate_password
        
# main
  
input_sentence = input('bitte einen Satz eingeben: ')
password = wifi_password.generate_password(sentence = input_sentence)
# password = generate_password(sentence)
print(password)


