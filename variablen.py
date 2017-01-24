a = 2
z = "2"
b = "Hallo Welt"
# a = "Zwei"
c = str(a)
print(a, b) ## einfache Ausgabe OHNE Verkettung
# print(a + b) ## operand auf unterschiedliche Typen funktioniert nicht
print(str(a) + b) # oder
print(c + b)

# t = "Falsch"
t = False
t1 = None
t2 = None

t1 = ""
t2 = 0

if t1 == None:
  print("t ist gleich")
else:
  print("t ist NICHT gleich")  