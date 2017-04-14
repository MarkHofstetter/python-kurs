import re

a = 'Schulgasse 234, 1090 gars am kamp, Stiege 27'

data = re.search(r'.*(\d{4})\s+([\w\s]+),', a)
## data[0] enthaelt den kompletten match 
print(data.group(1))
print(data.group(2))