# -*- coding: utf-8 -*-

# Να διαβάζει αριθμούς. Να υπολογίζει μέγιστο-ελάχιστο-μέσο όρο. Με 0 να τερματίζει

# Εισαγωγή δεδομένων
arithmos=int(input("Δώστε ακέραιο αριθμό ή 0 για έξοδο:"))
print ""


# Αρχικοποίηση
sum=0.0 # Αθροιστής. Το δηλώνω ως δεκαδικό για να βγει η διαίρεση ως δεκαδικό
plithos=0
max=arithmos # Αλλιώς μπορεί να δηλωθεί ως ο μικρότερος αριθμός (πχ σε βαθμολογία το 0)
min=arithmos # Αλλιώς μπορεί να δηλωθεί ως ο μεγαλύτερος αριθμός (πχ σε βαθμολογία το 20)


# Έλεγχος-Επεξεργασία
while arithmos!=0:
    sum=sum+arithmos
    plithos=plithos+1    
    if arithmos>=max:
        max=arithmos
    if arithmos>=min:
        min=arithmos
    arithmos=int(input("Δώστε ακέραιο αριθμό ή 0 για έξοδο:"))
    print ""

# Εμφάνιση
print "Ο μέγιστος αριθμός είναι",max,"ενώ ο ελάχιστος είναι",min
print ""
if plithos!=0:
    mo=sum/plithos
    print 'Ο μέσος όρος είναι',mo
else:
    print "Δεν εισάγατε αριθμούς."


# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
