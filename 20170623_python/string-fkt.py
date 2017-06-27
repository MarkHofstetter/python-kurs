text = 'Python ist super'

print(text.count('s'))

print(text.lower().count('p'))

print(text.find('ist'))

text = text.replace('ist', 'wird')
print(text)

# for zeichen in text:
#    print(zeichen)

print(text[-5:])

words = text.split()
print(words)
    
    