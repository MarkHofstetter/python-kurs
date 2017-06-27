import random

def generate_password(sentence, min_length = 3, randomness = True ):  
    words = sentence.split()
    password = ''
    sentence = ''
    if len(words) < min_length:
        raise ValueError('Too few words')
        
    for word in words:
        password += word[0] 
        if randomness == True:
            password += str(random.randint(0,9))
    return password
# end generate_password
