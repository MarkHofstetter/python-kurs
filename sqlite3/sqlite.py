import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

cursor = conn.execute('SELECT id, data FROM test WHERE data=?', ('bla'))
print(conn.fetchall())
for row in cursor:
  print(row)

conn.close()
