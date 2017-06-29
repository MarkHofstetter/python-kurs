import sqlite3
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('dbconf.ini')
dbconf = config['db']

# config.read('secretconf.ini')

conn = sqlite3.connect(dbconf['dbname'])
cursor = conn.execute('select * from preise')
rows = cursor.fetchall()
d = {}
for row in rows:
  print(row[0], row[1])
  d[ row[0] ] = row[1]
  
conn.close()

print("der Preis im Jahr 2005 war ", d[2005])