# -*- coding: utf-8 -*-

# Σταθερές
epitokio=0.035

# Εισαγωγή δεδομένων
k=float(input("Εισάγετε κεφάλαιο: "))
print ""


# Επεξεργασία
protos=k+k*epitokio
defteros=protos+protos*epitokio

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Πρώτος χρόνος",protos,"€"
print ""
print "Δεύτερος χρόνος",defteros,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
