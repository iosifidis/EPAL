# -*- coding: cp1253 -*-

# Επεξήγηση
print "Η άσκηση ζητάει από τον χρήστη να εισάγει ακέραιο (αρνητικό ή θετικό)."
print "Υπολογίζει πόσους αρνητικούς και πόσους θετικούς έδωσε ο χρήστης."
print "Όταν εισάγει 0, θα εμφανίσει πόσους αρνητικούς και πόσους θετικούς αριθμούς έδωσε ο χρήστης."
print ""

#Εισαγωγή δεδομένων
thetikoi=0
arnitikoi=0
control=1

while control!=0:
        number=input ("Δώσε αριθμό (αρνητικό, θετικό ή 0 για έξοδο): ")
        if number>0:
                thetikoi=thetikoi+1
        elif number<0:
                arnitikoi=arnitikoi+1
        else:
                control=0


# Εκτύπωση αποτελεσμάτων
print "Οι θετικοί αριθμοί είναι:",thetikoi
print ""
print "Οι αρνητικοί αριθμοί είναι:",arnitikoi

# Footer
print ''
print 'Μην παραχαράσετε την ιστορία.'
print 'Ευχαριστούμε για την προτίμησή σας.'
print ''
print 'Copyleft 2019, Efstathios Iosifidis'

