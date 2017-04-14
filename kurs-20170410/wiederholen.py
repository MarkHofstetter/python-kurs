k = 10
t = 'Hallo'
tz = '5'

# print(i)

u = k + int(tz)
print(u)

i = 0
i += 1 # entspricht i = i + 1

if i >= 1:
    print('i ist 1')
elif i > 0:
    print('i ist 2')
    
while True:
    i += 1
    print(i)
    if i > 10:
        break
        
for i in range(1,12):
    print(i)