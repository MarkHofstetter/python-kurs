def fkt(a):
    print(a)
    a = 23
    
def list_fkt(l):
    print(l)
    l.append(2)

def fkt(a,b):
    print(a,b)
    a = 23
    return (a,b)
    
def kwfkt(z, **kwargs):
    print(z)
    print(kwargs)
    print(kwargs['b'])
    
b = 12    
e,f = fkt(b,2)    
print(b)
print('2 param', e, f)

c = [1,2,3]
list_fkt(list(c))
print(c)

kwfkt(42, a=1, b=3, c={'g':8})