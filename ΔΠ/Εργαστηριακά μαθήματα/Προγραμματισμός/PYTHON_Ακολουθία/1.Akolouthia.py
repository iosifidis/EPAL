# -*- coding: utf-8 -*-

# Σταθερές
fpa=0.23

# Εισαγωγή δεδομένων
timi=float(input("Δώσε τιμή προϊόντος: "))
print ""

# Επεξεργασία
teliki_timi=timi+timi*fpa

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Η τιμή του προϊόντος είναι",teliki_timi,"€"
print ""
poso=float(input("Πόσα χρήματα έδωσε ο πελάτης; "))
print ""
print "Τα ρέστα του πελάτη είναι",poso-teliki_timi,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
