'''
Δίνεται το παρακάτω πρόγραμμα το οποίο ελέγχει αν το στοιχείο key
βρίσκεται στη lista τουλάχιστον τρείς (3) φορές και εμφανίζει
τη θέση στην οποία βρίσκεται την τρίτη φορά.
Να γράψετε ό,τιχρειάζεται να συμπληρωθεί έτσι ώστε το πρόγραμμα
να λειτουργεί σωστά.
'''
# -*- coding: utf-8 -*-
def search(lista, key):
    done = False
    position = 0
    i = 0
    count = 0
    n = len(lista)-1
    while i <= n and done == False :
        if lista[ i ] == key :
            count = count + 1
        if count == 3 :
            done = True
            position = i
        else:
            i = i + 1
    if done :
        print "To", key, "υπάρχει τουλάχιστον 3 φορές."
        print "Για τρίτη φορά εμφανίζεται στη θέση ", position, "."
    else:
        print "To", key, "δεν υπάρχει τουλάχιστον 3 φορές."

lista=[3,4,5,6,4,2,1,7,9,4,6,8,5,4]
print search(lista,4)
