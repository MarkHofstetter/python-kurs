text = 'Python ist super'
k = 7

print(text + text)
print(text, k)

print((text + ' ') * k)

print(text.upper() + text.lower())
print(len(text))

print('daß'.upper())
    
# wir fragen usereingabe ab
# und wollen UNABHAENGIG von der gross/kleinschreibung
# "wissen" ob die Usereingabe in text enthalten ist

#userinput = input('String eingeben: ')

#if userinput.lower() in text.lower(): # in operator verhaellt wie ein contains
#    print('string ist enthalten')
    
# maskierung 

t = "Ein String ohne \"Anfuehrungszeichen\" - 'gelogen'"
print(t)

a = 13
b = 7

print(str(a) + ' geteilt durch ' + str(b) + ' ergibt ' + str(a/b))

print("%d geteilt durch %d ergibt %010.3f" % (a, b, a/b) )

print("{0:d} geteilt durch {1:d} ergibt {2:10.3f}".format(a, b, a/b))

