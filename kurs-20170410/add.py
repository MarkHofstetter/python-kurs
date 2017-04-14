"""
+ progamm zur addition 2er Zahlen
"""

import wifi_input

# main
print("Hallo Willkommen zu additionsprogramm")
q = 'Erste Zahl: '    
a = wifi_input.input_and_validate_integer(question = 'Erste Zahl: ',
                               number_of_tries = 1)
b = wifi_input.input_and_validate_integer('Zweite Zahl: ')

print("Ergebnis: %d" % (a+b)) 


