# -*- coding: utf-8 -*-

# Σταθερές
misthos=55
asfalia=0.11
foros=0.085

# Εισαγωγή δεδομένων
onoma=raw_input("Δώσε όνομα υπαλλήλου: ")
print ""
meres=int(input("Δώσε ημέρες απασχόλησης: "))
print ""

# Επεξεργασία
mikta=misthos*meres
kratisis=mikta*asfalia+mikta*foros
kathara=mikta-kratisis

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Ο",onoma,"έχει καθαρές αποδοχές",kathara,"€, ενώ έχει κρατήσεις",kratisis,"€."

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
