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
    ar_timi=timi50 * temaxia
elif temaxia<=100:
    ar_timi=timi100 * temaxia
elif temaxia<=200:
    ar_timi=timi200 * temaxia
elif temaxia>200:
    ar_timi=timi200k * temaxia

timi_pro_fpa = ar_timi + ar_timi * kerdos
timi = timi_pro_fpa + timi_pro_fpa * fpa

# Εμφάνιση αποτελεσμάτων
print "Η τελική τιμή του προϊόντος ανά τεμάχιο για τον καταναλωτή είναι ",timi,"€"

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
