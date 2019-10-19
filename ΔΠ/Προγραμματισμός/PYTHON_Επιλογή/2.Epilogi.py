# -*- coding: utf-8 -*-

# Σταθερές
kerdos=0.3
fpa=0.23
timi50=3.5
timi100=3.20
timi200=2.8
timi200k=2.4

# Εισαγωγή δεδομένων
temaxia=int(input("Δώσε τεμάχια: "))
print ""

# Επεξεργασία
if temaxia>=1 and temaxia<50:
    timi=timi50*kerdos*fpa
elif temaxia<=100:
    timi=timi100*kerdos*fpa
elif temaxia<=200:
    timi=timi200*kerdos*fpa
else:
    timi=timi200k*kerdos*fpa

# Εμφάνιση αποτελεσμάτων
print "Η τελική τιμή του προϊόντος ανά τεμάχιο για τον καταναλωτή είναι ",timi,"€"

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
