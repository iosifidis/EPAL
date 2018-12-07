# -*- coding: cp1253 -*-

import math

# Ερώτηση για X
x=int(input('Δώστε την τιμή του x:'))

# Βρόγχος υπολογισμών
if x<=0:
    print 3*(x**2)+1
elif 0<x and x<=3:
    print 2*x+1
else:
    print math.sqrt(46+x)

print ''
print ''
print 'Εάν θέλετε εκτελέστε το πρόγραμμα ξανά για άλλη τιμή του .'
print 'Ευχαριστούμε για την προτίμησή σας.'
print ''
print 'Copyleft 2018, Efstathios Iosifidis'
