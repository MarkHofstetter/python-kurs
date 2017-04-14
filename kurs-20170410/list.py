"""
+ listen, felder, arrays, ...
"""

# list
#    0 1 2 3 4 5  6  7
f = [1,1,2,3,5,8,13,21]

mixed_list = [0.2, 'Haus', 42, True]

print(f)
print(mixed_list)

print(sum(f)) # summe über liste

print(f[7])

length = len(f) # zahl der elemente in der Liste
print(length)
#f[length] = f[length-2] + f[length-1] # neues Element erstellen geht so nicht
f.append(f[length-2] + f[length-1])    # ein neues Element am Ende anhaengen

print(f[-1]) # negative indices von recht nach links

f.append(f[-2] + f[-1]) 
print(f)

print(f[0:5]) # liefert alle elemente vom 0ten bis inkl des 4ten

f.append(sum(f[-2:])) # leer bedeuted vom Anfang oder bis zum Ende
print(f)

for element in f:
    print(element)
    
    
