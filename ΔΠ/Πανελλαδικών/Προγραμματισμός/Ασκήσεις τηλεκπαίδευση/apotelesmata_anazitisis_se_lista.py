'''
Δίνεται το παρακάτω πρόγραμμα το οποίο ελέγχει αν το στοιχείο key
βρίσκεται στη lista και επιστρέφει όλες τις θέσεις στις οποίες το συναντάμε.
Να γράψετε ό,τιχρειάζεται να συμπληρωθεί έτσι ώστε το πρόγραμμα
να λειτουργεί σωστά.
'''
# -*- coding: utf-8 -*-
def search(lista, key):
    done = False
    exist = False
    i = 0
    thesi=[]
    n= len(lista)-1
    while i <= n and done == False :
        if lista[ i ] == key :
            thesi.append(i)
            exist=True
            i=i+1
        else:
            i=i+1
        if i>n and exist == True:
            done = True     
    if done == True:
        return thesi
    else:
        return "Κανένα αποτέλεσμα"

lista=[3,4,5,6,4,2,1,7,9,4,6,8,5,4]
print search(lista,4)
