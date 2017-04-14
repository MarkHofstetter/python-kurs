""" 
error handling in python
"""
try:
    b = 10
    a = None

    while a == None and a != 0:
        try:
            a = int(input("Zahl: "))
        except ValueError as e:    
            print("ungueltiger Wert")
        
    try:
        print(b/a)
    except ZeroDivisionError:
        print("geht nicht")    
        
except:
    print("something awful")    
    # write something to log
    # cry for help