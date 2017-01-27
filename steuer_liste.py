#Tarifstufen Einkommen in Euro	Grenzsteuersatz2) ab 2016
#     11.000 und darunter	0 Prozent
#über 11.000 bis 18.000	25 Prozent3)
#über 18.000 bis 25.000	35 Prozent3)
#über 25.000 bis 31.000	35 Prozent
#über 31.000 bis 60.000	42 Prozent
#über 60.000 bis 90.000	48 Prozent
#über 90.000 bis 1.000.000	50 Prozent
#über 1.000.000	55 Prozent4)

# bsp 32000
# -11000 und 0% versteuert, bleiben 21000
# 18000-11000 => 7000, 25%, bleiben 14000
# 25000-18000 => 7000, 35%, bleiben 7000
# 31000-25000 => 6000, 35%, bleiben 1000
# 60000-31000 => 29000, 42%, bleibt 0

# 11000 * 0
# 7000 * 0.25
# 7000 * 0.35
# 6000 * 0.35
# 1000 * 0.42

def SteuerGehaltsstufe(steuersatz, untergrenze, obergrenze):
  rest = einkommen - untergrenze
  if rest <= 0:
    rest = 0
  elif rest > (obergrenze - untergrenze):
    rest = (obergrenze - untergrenze)
  steuer = rest * steuersatz
  return steuer

einkommen = int(input('Bitte Einkommen eingeben: '))
# einkommen = 40000  # Steuer: 10080
steuer = 0

steuerklassen = [
     [0    ,        0   ],
     [11000,        0   ],
     [18000,        0.25],
     [25000,        0.35],
     [31000,        0.35], 
     [60000,        0.42],
     [90000,        0.48],
     [1000000,      0.50],
     [float('inf'), 0.55]
     ]

untergrenze = 0     
for steuerklasse in steuerklassen:
  ## print(steuerklasse[0], steuerklasse[1])
  steuer += SteuerGehaltsstufe(steuerklasse[1], untergrenze, steuerklasse[0])
  untergrenze = steuerklasse[0]

  # print("Die Steuer ist {0:8.2f}".format(steuer))
print("Die Steuer betraegt %8.2f" % steuer)
