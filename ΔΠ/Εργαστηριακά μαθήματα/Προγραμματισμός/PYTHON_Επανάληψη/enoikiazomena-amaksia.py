# -*- coding: utf-8 -*-

# Άσκηση όπου υπολογίζει το κόστος ενοικίασης αυτοκινήτου ανάλογα με τις ημέρες και χιλιόμετρα

# Αρχικοποίηση
total=0 # Αθροιστής
car=0 # Μετρητής για αμάξια πάνω από 6 ημέρες και έως 1500χλμ

# Εισαγωγή δεδομένων
arithmos_kikloforias=raw_input("Δώσε αριθμό κυκλοφορίας ή 0 για τερματισμό:")
print ''

#Έλεγχος-Επεξεργασία
while arithmos_kikloforias!="0":
    meres=int(input("Δώσε ημέρες που ενοικίασης του αυτοκινήτου:"))
    print ""
    km=float(input("Δώσε χιλιόμετρα που διήνυσε το αυτοκίνητο:"))
    if meres<=2:
        kostosm=meres*30
        if km<=1500:
            kostos=kostosm+km*0.03
        elif km>1500:
            kostos=kostosm+km*0.05
    elif meres>2 and meres <=6:
        kostosm=meres*25
        if km<=1500:
            kostos=kostosm+km*0.03
        elif km>1500:
            kostos=kostosm+km*0.05
    elif meres>6:
        kostosm=meres*20
        if km<=1500:
            kostos=kostosm+km*0.03
            car=car+1
        elif km>1500:
            kostos=kostosm+km*0.05
    total=total+kostos
    print ""
    print "Το αμάξι με αριθμό κυκλοφορίας",arithmos_kikloforias,"χρωστάει",kostos,"Ευρώ"
    print ""
    arithmos_kikloforias=raw_input("Δώσε νέο αριθμό κυκλοφορίας για συνέχεια ή 0 για τερματισμό:")
    print ""

# Εμφάνιση
if total!=0:
    print 'Η συνολοκή χρέωση είναι:,',total,'Ευρώ'
    print ""
    print 'Τα αμάξια με πάνω από 6 ημέρες ενοικίασης και έως 1500χλμ είναι',car
else:
    print "Δεν εισάγατε αμάξι."

# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
