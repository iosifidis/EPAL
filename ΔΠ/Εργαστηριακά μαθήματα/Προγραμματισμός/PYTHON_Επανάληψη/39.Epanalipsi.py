# -*- coding: utf-8 -*-

# Να αναπτύξετε πρόγραμμα που θα διαβάζει άγνωστο πλήθος αριθμών μέχρι το άθροισμά τους να ξεπερνά την τιμή 500. Θα εκτυπώνεται το πλήθος των αριθμών που διαβάστηκαν.

# Εισαγωγή δεδομένων
arithmos=float(input("Δώστε αριθμό:"))
print ""

# Αρχικοποίηση
sum=arithmos # Αθροιστής
plithos=1 # Μετρητής

# Έλεγχος-Επεξεργασία
while sum<500:
    plithos=plithos+1
    arithmos=float(input("Δώστε αριθμό:"))
    sum=sum+arithmos
    print ''

# Εμφάνιση
print 'Το πλήθος των αριθμών που εισήχθησαν ήταν',plithos



# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
