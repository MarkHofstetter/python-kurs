""" eine for schleife in python geht IMMER
ueber die elemente einer "Liste"
"""
for i in range(1,10,2):
    print(i)
    
""" while loop
mache etwas solange eine Bedingung gilt """

x = 0
while x < 100:
    # x = x + 10
    x += 10
    print(x)

x = None    
while x != 0:
    x = int(input('bitte eine Zahl eingeben: '))
    print(x)
    
print('Ende')    