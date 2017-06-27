'''
+ Lotto 6 aus 45 (zahlen 6 zahlen aus dem raum 1-45)
+ Problem keine Zahl darf doppelt vorkommen
'''

import random
import matplotlib.pyplot as plt

def lotto():
    number_list = list(range(1,46))
    numbers_selected = []
    for i in range(0,6):
        numbers_selected.append( number_list.pop(random.randint(0,len(number_list)-1)) )
    return numbers_selected

histogram = [0] * 45
for i in range(0,45):
    histogram[i] = 0
    
for i in range(0,10000):
    for number in lotto():
        histogram[number-1] += 1

c = 1        
for e in histogram:
    print(c, e)
    c += 1
    
plt.plot(histogram)
plt.ylim([0,max(histogram)*1.1])
# plt.ylabel('some numbers')
plt.show()    
    

