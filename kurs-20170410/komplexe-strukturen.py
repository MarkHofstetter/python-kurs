teilnehmer = [
    ['Mark',    1975, 'blau'],      # 0
    ['Tanja',   1981, 'schwarz'],   # 1
    ['Martin',  1973, 'blau'],      # 2  
    ['Kevin',   1998, 'gelb'],
    ['Müslüm',  1984, 'grün'],
    ['Heinrich',1981, 'rot'],
    ]

# print(teilnehmer[0][2][1])
""" nach eingabe eines Namens
    geburtsjahr und Lieblingsfarbe ausgeben

    + über liste iterieren und wenn name gefunden dann 
      ausgeben
    
"""    

search = input("Namen eingeben: ")
for tn in teilnehmer:
    if tn[0] == search:
        print(tn[1:])
    