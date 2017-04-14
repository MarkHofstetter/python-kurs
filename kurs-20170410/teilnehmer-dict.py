"""
teilnehmer = [
    ['Mark',    1975, 'blau'],      # 0
    ['Tanja',   1981, 'schwarz'],   # 1
    ['Martin',  1973, 'blau'],      # 2  
    ['Kevin',   1998, 'gelb'],
    ['Müslüm',  1984, 'grün'],
    ['Heinrich',1981, 'rot'],
    ]
"""

# python: dictonary - hash oder assoziatives array
#    key       value
teilnehmer = {
    'Tanja':   1981,
    'Martin':  1973,
    'Kevin':   1998,
    'Müslüm':  1984,
    'Heinrich': { 'geburtsjahr': 1981, 'groesse': 185, 
                  'emails': ['a@bla.com', 'b@g.at']},
}

teilnehmer['Mark'] = 1975
# del teilnehmer['Martin'] 
print(teilnehmer['Heinrich']['geburtsjahr'])

for name in teilnehmer:
    print(name, teilnehmer[name])


search = 'bla'
# ueberpruefen ob ein wert im dictonary ist
if search in teilnehmer: 
    print(teilnehmer[search])
else:
    print(search, 'gibt es nicht')
    
    