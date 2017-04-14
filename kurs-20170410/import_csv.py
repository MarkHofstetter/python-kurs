import csv
import numpy
import matplotlib.pyplot as plt

""" die daten in dictionary importieren
{'name des Energietraegers' : [1.1,2.2,3.0,4.7],
 'holz': [....]
}

+ durchschnittspreis
+ graph preis pro jahr
+ ...
+ daten abspeichern
"""

energy_data = {}

with open('Datenimport.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ';')
    # print(data)
    data = list(data)
    for row in data[2:]:               
        r = []
        # energy_data[row[0]] = []
        for e in row[1:]:
            k = e.replace(',', '.')
            r.append(float(k))
 # Diesel (komm. Einsatz)/l ;0,28;0,29;0,32;0,32;0,36;0,38;0,26;0,45;0,48;0,72;0,66;0,54;0,49            
        energy_data[row[0]] = r    
        # for e in row[1:]:
        #    energy_data[row[0]].append(e.replace(',', '.'))
            
        # print(row)
        # energy_data[row[0]] = list(map(c, row[1:]))
        # energy_data[row[0]] = list(
        #        map(lambda s: float(s.replace(',', '.')), row[1:]))
        
#print(energy_data[' Steinkohle (Industrie)/t '])
#print(numpy.mean(energy_data[' Steinkohle (Industrie)/t ']))

fileno = 0
for energy in energy_data:
    print("%-40s %.2f" %  (energy, numpy.mean(energy_data[energy])) )
    g = plt
    g.plot(data[1][1:], energy_data[energy], 'ro')
    g.title(energy)
    g.xlabel('Jahr')
    g.ylabel('Preis')
    # plt.axis([0, 6, 0, 20])
    g.savefig(str(fileno) + '.png', bbox_inches='tight')
    g.close()
    fileno += 1
    
with open('clean.csv', 'w', newline='') as writecsv:
    writer = csv.writer(writecsv, delimiter=';',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data[1])
    for energy in energy_data:
        writer.writerow([energy] + energy_data[energy])
    
    
    
    
    