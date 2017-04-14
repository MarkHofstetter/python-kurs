teilnehmer = [
    'Tanja',
    'Martin',
    'Kevin',
    'Müslüm',
    'Heinrich',    
    ]
    
trainer = 'Mark'

alle = teilnehmer + [trainer]

# alle_original = alle       ## keine kopie sondern nur neuer Name fuer Referenz
alle_original = list(alle)   ## kopie von der Liste


alle.sort()
print(alle)
alle.reverse()    
alle.insert(0, 'Max') # fügt VOR Index n ein
print(alle)
print(alle_original)



search = input('Name :')
try:
    print("Der Name wurde %d mal, an position %d gefunden" % 
        (alle.count(search), alle.index(search)) )  
except ValueError:
    print('Wert nicht gefunden')
