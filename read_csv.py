import csv
import sqlite3

werte = {}
with open('Datenimport.csv') as csvfile:
  daten = csv.reader(csvfile, delimiter = ';')
  daten_as_list = list(daten)
  for line in daten_as_list[2:]:
  #for line in list(daten)[2:]:  ## entspricht den beiden oberen Zeilen
   # print(line)
    a = []
    for v in line[1:]:
      a.append( float(v.replace(',','.')) )
    k = line[0].strip(' ')      
    werte[ k ] = a
#  Heizöl schwer (Industrie)/t ;162,38;154;224,92;267,54;278,98;392,05;283,68;386,12;504,2;573,75;511,77;472,79;332,34    

# print(werte['Steinkohle (Industrie)/t'])
# print(werte['Heizöl schwer (Industrie)/t'])

#for brennstoff in werte:
#  maxPreis = max(werte[brennstoff])
#  pos = werte[brennstoff].index(maxPreis)
#  print(brennstoff, max(werte[brennstoff]), pos + 2003 )

# zuerst in der shell db anlegen + tabelle
# sqlite3 preise.db
# sqlite> create table preise (jahr integer, preis number);
# select * from preise;

conn = sqlite3.connect('preise.db')

jahr = 2003
for preis in werte['Steinkohle (Industrie)/t']:
  print(jahr, preis)
  conn.execute('insert into preise(jahr, preis) values (?,?)', (jahr, preis))
  jahr += 1

conn.commit()  