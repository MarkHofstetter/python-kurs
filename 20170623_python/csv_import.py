'''
+ datei öffnen und csv parsen
+ daten in eine verarbeitbare struktur bringen 

+ Graphen mit dem zeitlichen Preisverlauf jedes Energieträgers
+ durchschnittspreis
+ min/max Preis
+ ....

++ usereingabe Jahr, ausgabe aller Preise in diesem Jahr
++ ....

{
 Heiz�l schwer (Industrie)/t: {2003: 162.38, 2004: 154, ..},
 Heiz�l schwer (Kraftwerke)/t: {2003: 121.88, 2004: 115,74, ...}
}

oder 

jahre [2003, 2004, ...]
{
 Heiz�l schwer (Industrie)/t: [162.38, 154 ],
 Heiz�l schwer (Kraftwerke)/t: [121.88, 115.74, ]
}

Replace
e = '123,232'
f = e.replace(',', '.')
'''

import csv
import pprint
import matplotlib.pyplot as plt

with open('Datenimport.csv') as csvfile:
    # data = list( csv.reader(csvfile, delimiter=';', skipinitialspace=True) )
    data = list( csv.reader(csvfile, delimiter=';',) )    
    # data = list(data)
    
years = data[1][1:]

prices = dict() # {}

for row in data[2:]:          
    '''
    prices[row[0]] = []
    for e in row[1:]:        
        prices[row[0]].append(e.replace(',', '.'))
    '''
    
    prices[str(row[0]).strip()] = list(float(e.replace(',', '.')) for e in row[1:])
    #prices[row[0]] = list(map(lambda s: float(s.replace(',', '.')), row[1:]))       
    
# pprint.pprint (prices)        

import numpy 

for name in prices:
    print("%-40s %10.3f" % 
     (name, numpy.mean(prices[name]))
     )

     
with open('clean.csv', 'w', newline='') as writecsv:
    writer = csv.writer(writecsv, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)    
    for name in prices:
        writer.writerow([name] + prices[name])     
     
# graphen zeichen     
for product in prices.keys():
    plt.plot(years,prices[product], label=product)
    plt.ylabel('Preise')
    plt.xlabel('Jahre')
 
    ax = plt.subplot(111)
    box = ax.get_position()
 
    ax.set_position([box.x0, box.y0, box.width * 0.96, box.height])
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.savefig('energy.png', bbox_inches='tight')    
# plt.show()    