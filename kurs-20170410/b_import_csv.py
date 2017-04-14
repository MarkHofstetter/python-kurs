import csv
import numpy
import matplotlib.pyplot as plt
import re

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

with open('Datenimport_bork.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ';')
    # print(data)
    data = list(data)
    for row in data[2:]:               
        # print(row)
        a = re.match(r'(.*?) (\d.+)', row[0])        
        if a:
            print(a.group(1))
            print(a.group(2))        
            energy_data[a.group(1)] = [a.group(2)] + row[1:4]
        
for l in energy_data:
    print(l, energy_data[l])

        