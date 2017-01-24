UserInput = input('Bitte Zahl eingeben: ') 

try:
  UserInput = int(UserInput)  
except:
  print("keine Zahl")  
  exit()

if UserInput > 10:
  print("Zahl groesser 10")
elif UserInput < 10:
  print("Zahl kleiner 10")
else:
  print("Zahl ist 10")  
  


	
