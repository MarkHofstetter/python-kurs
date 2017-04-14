"""
+ vom benutzer zahlen einlesen solange bis
der benutzer 0 eingibt
+ die eingaben aufsummieren
+ die 0 eingabe die beendet, wird in durchschnittsbildung nicht mit einbezogen
+ wenn die Summe 50 ueberschreitet ebenfalls beenden
+ am ende die Summe und den durchschnitt der Zahlen ausgeben
"""

# sum = sum + x 

sum     = 0 
max_sum = 50
i       = 0
x       = None

while sum <= max_sum: # and x != 0:
    x = None
    j = 0
    try:
        x = int(input('bitte Zahl (max %d) eingeben: ' % (max_sum)))  
    except ValueError:
        print('Ungueltiger Wert')
        continue
           
    """
    while x == None:
        try:
            x = int(input('bitte Zahl (max %d) eingeben: ' % (max_sum)))  
            if x > max_sum:
                print('zu hoher Wert')
                x = None
        except ValueError:
            j += 1    
            print('Ungueltiger Wert ', j)
            if j > 3:
                exit()
    """            
    if x == 0:
        break
    sum += x # sum = sum + x
    i += 1   # i = i + 1         

#if x == 0:
#    i -= 1

if i == 0:
    durchschnitt = 0
else:
    durchschnitt = sum/i
    
print("Summe %d Durchschnitt %.2f" % (sum, durchschnitt))

""" perl(ohne strict) [php]

$sum = 0;
while ($sum <= 50) {
    $x = <STDIN>;
    chomp($x);
    [$x = fgets(STDIN);]
    if ($x == 0) {
        break;
    }
    $sum += $x;
    $i++; # $i += 1 works also
}
printf("Summe %s Durchschnitt %.2f",(sum, sum/i));

"""
