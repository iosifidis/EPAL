# -*- coding: utf-8 -*-

# Σταθερές
t20=0.2
t50=0.25
t100=0.3
t101=0.4
konsola=150


# Εισαγωγή δεδομένων
temaxia=int(input("Δώσε τεμάχια που πούλησε ο πωλητής: "))
print ""


# Επεξεργασία δεδομένων
if temaxia<=20:
    promitheia=temaxia*konsola*t20
elif temaxia<=50:
    promitheia=temaxia*konsola*t50
elif temaxia<=100:
    promitheia=temaxia*konsola*t100
elif temaxia>100:
    promitheia=temaxia*konsola*t101


# Εμφάνιση αποτελεσμάτων
print "Η προμήθεια του πωλητή είναι",promitheia,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
