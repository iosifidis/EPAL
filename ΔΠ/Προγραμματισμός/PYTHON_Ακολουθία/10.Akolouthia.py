# -*- coding: utf-8 -*-

# Σταθερές

# Εισαγωγή δεδομένων
a=int(input("Δώσε ψήφους πρώτου υποψηφίου: "))
print ""
b=int(input("Δώσε ψήφους δεύτερου υποψηφίου: "))
print ""
c=int(input("Δώσε ψήφους τρίτου υποψηφίου: "))
print ""

# Επεξεργασία
psifoi=a+b+c
posostoa=(a*100.0)/psifoi
posostob=(b*100.0)/psifoi
posostoc=(c*100.0)/psifoi

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Ο πρώτος έλαβε",posostoa,"%"
print ''
print "Ο δεύτερος έλαβε",posostob,"%"
print ''
print "Ο τρίτος έλαβε",posostoc,"%"

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
