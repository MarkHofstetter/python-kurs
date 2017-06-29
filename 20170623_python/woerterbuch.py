import configparser
import pprint

config = configparser.ConfigParser()
config.read('woerterbuch.ini')
config.sections()
eng2ger = config['words']
game = config['game']


# print(list(eng2ger.items()))
# print(list(eng2ger.keys()))
# print(list(eng2ger.values()))


'''
for k,v in words.items():
    print(k,v)
    deu2eng[v] = k
'''
# ger2eng = dict((v,k) for k,v in eng2ger.items())

ger2eng = dict( zip(eng2ger.values(), eng2ger.keys()) )

# print(deu2eng)    
userinput = input('bitte wort eingeben: ')
if userinput in eng2ger:
    print(eng2ger[userinput])
elif userinput in ger2eng:
    print(ger2eng[userinput])
else:
    print('wort unbekannt')    

'''

print(dict(words))


+ usereingabe englische wort
+ ausgabe deutsches wort

++ auch die umgekehrte uebersetzung deu => eng
++ testbaren form

'''

