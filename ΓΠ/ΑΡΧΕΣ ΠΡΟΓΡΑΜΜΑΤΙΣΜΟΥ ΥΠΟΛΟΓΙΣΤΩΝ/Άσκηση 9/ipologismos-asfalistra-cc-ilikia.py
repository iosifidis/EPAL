# -*- coding: cp1253 -*-
# -*- coding: utf8 -*-

print 'ΕΡΩΤΗΣΗ ΗΛΙΚΙΑΣ'
print ''
print 'Το πρόγραμμα αυτό ζητάει από τον χρήστη να εισάγει την ηλικία του.'
print 'Ζητάει κυβισμό αυτοκινήτου'
print 'Θα εμφανίσει μήνυμα που να ενημερώνει τι πληρώνει ασφάλιστρα.'
print ''

# Εισαγωγή δεδομένων
cc=int(input('Δώσε κυβισμό:'))# Εισαγωγή κυβισμού
age=int(input('Δώσε ηλικία:'))# Εισαγωγή ηλικίας
fpa=1.24
print ''

# Εμφάνιση αποτελεσμάτων
if cc<=1000 :
    asf=150
elif cc>=1001 and cc<=2000:
    asf=200
else:
    asf=300

if age<=23:
    add=40
else:
    add=0

total=(asf+add)*fpa

print 'Θα πλερώ',total,'?'

print ''
print ''
print ''
print 'Εάν άλλες ηλικίες και κυβικά, εκτελέστε ξανά το πρόγραμμα. '
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'Copyleft 2018, Efstathios Iosifidis'
