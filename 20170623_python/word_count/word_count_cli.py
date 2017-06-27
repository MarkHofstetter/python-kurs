import word_count


word_list = list()
while True:
    userinput = input('Bitte gib mir nur ein Wort: ')
    if userinput.lower() == 'ende':
        break
    word_list.append(userinput)

print(word_count.count_words(word_list))
    