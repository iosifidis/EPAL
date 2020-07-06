# -*- coding: utf-8 -*-

# Σταθερές
foros=0.37

# Εισαγωγή δεδομένων
esoda=float(input("Δώσε τα έσοδα της εταιρίας: "))
print ""
eksoda=float(input("Δώσε τα έξοδα της εταιρίας: "))
print ""

# Επεξεργασία
poso_forou=esoda*foros
kathara=esoda-eksoda-poso_forou #Για καθαρά κέρδη, πρέπει από τα έσοδα να αφαιρέσω έξοδα και ποσό φόρου;

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Το ποσό του φόρου είναι",poso_forou,"€, ενώ τα καθαρά κέρδη είναι",kathara,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
