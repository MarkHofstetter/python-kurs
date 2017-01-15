# call by value
# default value
# by name
# 


def add(a, b):
  "addiere a und b und retourniere die Summe"
  c = a + b
  b = 23
  return c


k = 4
print(add(2,k))
print(k)
k = 5
print(k)
