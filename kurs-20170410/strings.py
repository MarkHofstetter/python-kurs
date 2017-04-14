text = 'Python ist toll'

print(text + text)

print( (text + ' ') * 4 )
print( '*' * 40 )

length = len(text)
print(length)

print(text)
print( '*' * len(text) )

print(text.upper())
print(text.lower())

for l in text:
    print(l)

while True:
    search = input('text suche: ')
    if search == '0':
        break
    if search.lower() in text.lower():
        print("\"%s\" ist in \"%s\" %d mal enthalten" 
              % (search, text, text.lower().count(search)))
        print("wurde an pos %d gefunden" % text.lower().find(search))
        print("nicht gefunden")    
    else:

print(text.replace('Python', 'perl'))