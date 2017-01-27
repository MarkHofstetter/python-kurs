import time
import datetime
from dateutil.relativedelta import relativedelta

print(time.time())

lt = time.localtime()
print(lt)

jahr, monat, tag = lt[0:3]
stunde, minute, sekunde = lt[3:6]

print(jahr, monat, tag)
print(stunde, minute, sekunde)

print("%d-%02d-%02d" % (jahr, monat, tag))
print(time.strftime("%Y-%m-%d %H:%M:%S", lt))

#while True:
#  time.sleep(1)
#  print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

dp = 1975, 2, 23, 4, 0, 0, 0, 0, 0
#    y     m   d  H  m  s   
geburtstag = time.mktime(dp)

print(time.strftime("%Y-%m-%d %H:%M:%S %A %j", time.localtime(geburtstag)))

alter = time.time() - geburtstag
print('Alter ', alter/(365.2425*24*3600)) ## nicht richtig wg schaltjahren/sekunden

dtGeburtstag = datetime.date(1975, 2, 23)
dtHeute      = datetime.date.today()
dtGH         = datetime.date(2017, 2, 23)

diff = dtHeute - dtGeburtstag
print( diff.days )

from dateutil.relativedelta import relativedelta

print (relativedelta(dtHeute, dtGeburtstag).years)
print (relativedelta(dtGH, dtGeburtstag).years)

