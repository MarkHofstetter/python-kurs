eingabe = None
statistik = {}
while eingabe != 0:
  eingabe = int(input('Bitte Zahl eingeben: '))
  if eingabe in statistik:
    statistik[eingabe] += 1
  else:
    statistik[eingabe] = 1
  
print(statistik)