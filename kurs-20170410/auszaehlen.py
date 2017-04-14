b = [3,6,2,3,6,4,5,8]

from collections import Counter

""" auszaehlen

3: 2
6: 2
2: 1
...

+ loesung mit dictonary

"""

stat = {}

for z in b:
    if z in stat:
        stat[z] += 1
    else:
        stat[z] = 1

print(stat)    

print(Counter(b))
c = Counter(b)
for s in Counter(b):
    print(s, c[s])

for s in sorted(stat, key=stat.get, reverse=True):
    print("%d: %d" % (s, stat[s]))

