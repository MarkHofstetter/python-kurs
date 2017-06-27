# der benutzer wird nach zahlen gefragt
# mit eingabe von 0 (null) wird die schleife 
# beendet, danach wird die hoechste Zahl ausgegeben
# 5, 34, 7, 9, 12 => Ausgabe 34

max = 0 # float("-inf")
user_input = None

while user_input != 0:
    user_input = int(input('bitte eine Zahl eingeben: '))
    if user_input > max:
        max = user_input

print('groeste Zahl ist', max)        