import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

cursor = conn.execute('SELECT id, data FROM test')
# print(cursor.fetchall())
for row in cursor:
  print(row[0], row[1])
  
conn.execute('insert into test(id, data) values (?,?)', (42, 'meintext'))
conn.commit()    
  
conn.close()