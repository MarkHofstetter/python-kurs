def fkt(a):
    print(a)
    a[0] = 23
    
def list_fkt(l):
    print(l)
    l.append(2)

def fkt(a,b):
    print(a,b)
    a = 23
    
def kwfkt(**kwargs):
    print(kwargs)
    print(kwargs['b'])
    
b = 12    
fkt(b,2)    
print(b)

c = [1,2,3]
list_fkt(list(c))
print(c)

kwfkt(a=1, b=3, c={'g':8})