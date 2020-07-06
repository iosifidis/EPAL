# -*- coding: utf-8 -*-

# Σταθερές
poso3000=1.2
poso6000=2
poso6000k=3


# Εισαγωγή δεδομένων
pontoi=int(input("Δώσε πόντους: "))
print ""


# Επεξεργασία δεδομένων
if pontoi<1000:
    epistrofi=0
elif pontoi>=1000 and pontoi<3000:
    epistrofi=pontoi*poso3000
elif pontoi<=6000:
    epistrofi=3000*poso3000+(pontoi-3000)*poso6000
elif pontoi>6000:
    epistrofi=3000*poso3000+3000*poso6000+(pontoi-6000)*poso6000k


# Εμφάνιση αποτελεσμάτων
print "Η επιστροφή είναι",epistrofi,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
