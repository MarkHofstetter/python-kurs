try:
    user_input = int( input('bitte eine Zahl eingeben: ') )
except ValueError:
    print("das war keine zahl du dolm")        
    exit()


if user_input > 10:
    print('zahl groesser 10')
elif user_input == 10:
    print('zahl ist 10')
    print('wirklich 10!!!')    
else:
    print('zahl ist kleiner 10')

    
print('Ende')      

