#for i in range(10,0,-2):
#    print(i)

j = 0
while j < 10:    
    print(j)
    j += 1

    
while True: 
    print(j)   
    j -= 1
    if j <= 0:
        break
else:
    print('else', j)   