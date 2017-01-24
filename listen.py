teilnehmer = ['Adrian', 
              'Daniel',
              'Michael',
              'Johannes',
              'Martin',
              'Herbert',
              'Stefan',              
             ]

teilnehmer.sort()
teilnehmer.reverse()
print(teilnehmer)
print(len(teilnehmer))

try:
  print(teilnehmer[9])
except IndexError:
  print("Fehler kein solcher Index")
  
letzteReihe = teilnehmer[0:2]
print(letzteReihe + teilnehmer)
print(teilnehmer[5:])

i = 0;

teilnehmer_formatiert = []
for tn in teilnehmer:
  print("%d: Der Name des Teilnehmers lautet %s" % (i, tn))
  teilnehmer_formatiert.append("%d: %s" % (i, tn))
  i += 1

  
print(teilnehmer_formatiert)
  