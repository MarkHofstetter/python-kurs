steuerklassen = [
     [0    ,   0],
     [11000,   0.25],
     [18000,   0.35],
     [31000,   0.42], 
     [60000,   0.48],
     [90000,   0.50],
     [1000000, 0.55],
     ]

#steuerklassen.append([1000000, 0.55])     
#steuerstufen = [
#     0,
#     0.25,
#     0.35,
#     0.42,
#     0.48,
#     0.50,
#     0.55,
#]     

print(steuerklassen[2])

for steuerklasse in steuerklassen:
  print(steuerklasse[0], steuerklasse[1])
  
teilnehmer = [
              ['Adrian',   ['VS', 'Gym', 'Uni']],
              ['Daniel',   ['VS', 'HTL']],
              ['Michael',  ['VS', 'a', 'b', 'Uni']],
              ['Johannes', ['Uni']],
              ['Martin',   ['HS']],
              ['Herbert',  ['Gym']],
              ['Stefan',   ['LAP']],
              ['Mark',     ['VS', 'Tanzschule (abgebrochen)']],              
             ];

for tn in teilnehmer:
  print(tn[0], tn[1][-1])             

  
  