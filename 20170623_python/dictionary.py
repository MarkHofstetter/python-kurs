teilnehmer = {
    'Eva': {'year': 1996, 'gender': 'f', 'education': ['VS', 'Gym', 'FH']},
    'Sascha': 1995,
    'Philip': 1994,
    'Reinhard': 1964,
    'Marcus': 1981,
    'Peter': 1980,
    'Leo': 1966,
    'Mark': 1975,    
}



'''
userinput = input('Name: ')
if userinput in teilnehmer:
    print(teilnehmer[userinput])
else:
    print('nixi')
'''    

print(teilnehmer['Eva']['education'][-1])

#for name in teilnehmer:
#    print(name, teilnehmer[name])