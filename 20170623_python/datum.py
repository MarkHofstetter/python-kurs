import time
import datetime
from dateutil.relativedelta import relativedelta

print(time.time())

print(time.localtime())

lt = time.localtime()

print(lt[3:6])

print(time.strftime("%Y-%m-%dT%H:%M:%S"))

geburtstagd = 1975,2,23,4,0,0,0,0,0
geburtstag = time.mktime(geburtstagd)

alter = time.time() - geburtstag
print(alter/(365.25 * 24 * 3600))


dt_geburtstag = datetime.date(1975,2,23)
dt_heute = datetime.date.today()

diff = dt_heute - dt_geburtstag
print(diff.days)
rd_age = relativedelta(dt_heute, dt_geburtstag)
print(rd_age.years, rd_age.months, rd_age.days)

d = datetime.date(1582,10,5)
print(d + datetime.timedelta(days = 1) ) 