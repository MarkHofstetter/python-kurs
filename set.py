set1 = { 'a', 'b', 'c'}
set2 = { 'b', 'c', 'd'}
set1.add('d')
# remove() fehler wenn wenn nicht da
# discard  kein fehler wenn nicht da
# pop entfernt irgendein element 
# clear

print(set1)
# alle nicht vorhandenen elemente von set2 set1 hinzufuegen
set1 |= set2
print(set1)

# intersection/schnittmenge 
set1 &= set2
print(set1)

# minus/except
# set1 -= set2

# schnittmenge NUR die in beiden menge da sind 
set1 ^= set2 
