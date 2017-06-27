teilnehmer = [
    ['Eva', 1996],
    ['Sascha', 1995],
    ['Philip', 1994],
    ['Reinhard', 1964],
    ['Marcus', 1981],
    ['Peter', 1980],
    ['Leo', 1966],
    ['Mark', 1975],
]

# print(teilnehmer[5][1])

''' 
+ benutzereingabe Name eines Teilnehmers
+ Ausgabe des Geburtsjahres
++ den jüngesten Teilnehmer (möglichst elegant - zip?)
'''

userinput = input('Name: ')

for row in teilnehmer:
    if row[0] == userinput:
        print(row[1])
        break
else:
    print('nixi')


names, years = zip(*teilnehmer)
j = names.index(userinput)
print(years[j])

max_year = max(years)
i = years.index(max_year)
print(names[i])



