""" 
+ ask user to input a positive number till he/she enters 0
+ after that output the highest number
"""

x = None
max = 0
while x != 0:
    x = int(input('bitte eine Zahl eingeben: '))
    # wenn die eingebene Zahl groesser als die bisherige
    # groesste Zahl ist, dann wird diese die neue "Hoechstzahl"
    if x > max:
        max = x    
    # hier endet der while-block    
        
    
print(max)