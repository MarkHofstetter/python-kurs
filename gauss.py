## usereingabe einer zahl
## aufsummieren aller zahlen bis dahin

## zb 3 => 1+2+3 = 6
## 4 => 10
## 5 => 15
## 7 1+2+...+5+6+7 

a = int(input('Bitte Zahl eingeben: '))	
summe = 0

for i in range(1, a+1):
  summe += i

print(summe)  