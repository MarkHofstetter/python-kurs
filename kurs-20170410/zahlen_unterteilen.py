"""
+ die zahlen von 1-10 sollen unterteilt werden
+ in gerade und ungerade
+ und nur wenn ungerade soll auch angezeigt werden, 
  dass die Zahl groesser als 5 ist
"""

for i in range(1,11):    
    u = i/2    
    larger_than_5 = ''
    if u == int(u):       
        odd_or_even = 'gerade'
    else:        
        odd_or_even = 'ungerade'
    
    if i > 5 and u != int(u):            
        larger_than_5 = 'groesser als 5'                         
                
    print("%02d %s %s" % (i, odd_or_even, larger_than_5))        