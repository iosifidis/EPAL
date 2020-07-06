# -*- coding: utf-8 -*-

# Σταθερές
eso=0.3
ekso=0.5

# Εισαγωγή δεδομένων
a_eso=int(input("Δώσε αριθμό επιστολών εσωτερικού: "))
print ""
a_ekso=int(input("Δώσε αριθμό επιστολών εξωτερικού: "))
print ""

# Επεξεργασία
kostos=a_eso*eso+a_ekso*ekso

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Το ποσό πληρωμής στο ταχυδρομείο είναι",kostos,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
