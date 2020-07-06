# -*- coding: utf-8 -*-

# Να διαβάζει τιμές βιβλίων μέχρι να δοθεί τιμή το 0. Να υπολογίζει και να εκτυπώνει το ποσοστό των βιβλίων με τιμή πάνω από 20Ε.

# Αρχικοποίηση
sum=0 # Μετρητής
sum20=0 # Μετρητής

# Εισαγωγή δεδομένων
timi=float(input("Δώστε τιμή βιβλίου ή 0 για έξοδο:"))

# Έλεγχος-Επεξεργασία
while timi!=0:
    if timi>=20:
        sum20=sum20+1
    sum=sum+1
    timi=float(input("Δώστε τιμή βιβλίου ή 0 για έξοδο:"))

# Εμφάνιση
if sum!=0:
    pososto=sum20/float(sum)*100
    print 'Το ποσοστό των βιβλίων πάνω από 20Ε είναι',pososto,"%"
else:
    print "Δεν εισάγατε βιβλία."


# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
