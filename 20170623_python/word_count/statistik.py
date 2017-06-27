'''
+ benutzer gibt woerter ein solange bis zur eingabe von 'ENDE'
+ wir fuehren mit wie oft welches Wort eingeben wurde
+ ausgabe der statistik
+ a b c b c a a a ENDE => 
a: 4
b: 2
c: 2

++ testbar!!!
'''

from pprint import pprint

word_count = dict()

while True:
    userinput = input('Bitte gib mir nur ein Wort: ')
    if userinput.lower() == 'ende':
        break
    if userinput in word_count:
        word_count[userinput] += 1
    else:
        word_count[userinput] = 1

# del(word_count['ende'])
pprint(word_count)        