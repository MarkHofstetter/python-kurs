import configparser

# wir initialisieren ein ConfigParser object
config = configparser.ConfigParser()
config.sections()

config.read('dict.ini')
en2de = config['translation']

""" 
+ benutzer eingabe englisches wort
+ falls vorhanden die deutsche uebersetzung 
+ anderenfalls sinnvolle Fehlermeldung
"""

en = input('Bitte ein englisches Wort eingeben: ')
if en in en2de:
    print(en2de[en])
else:
    print('leider %s nicht gefunden' % (en))

# for en in en2de:
#     print(en, en2de[en])