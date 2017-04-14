# wir wollen eine liste "haendisch" sortieren

b = [3,6,2,3,6,4,5,8]

"""
+ die groesste Zahl raussuchen
+ diese entfernen, ausgeben
+ wiederholen bis die ursprungsliste leer ist
"""

r = []
m = None

while len(b) != 0:
    max = 0
    for m in b:
        if m > max:
            max = m    
    print(max)
    r.append(max)
    b.remove(max)

print(r)