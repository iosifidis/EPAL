# -*- coding: utf-8 -*-

# Εισαγωγή δεδομένων
atoma=0 # Μετρητής
maxvaros=350
varos=0 # Μεταβλητή ελέγχου (αθροιστής)
print ''

#Έλεγχος-Επεξεργασία
while varos<=maxvaros: 
  weight=float(input('Δώσε βάρος ατόμου που θα εισέλθει στον ανελκηστήρα:'))
  atoma=atoma+1 # Προθήκη ενός ατόμου
  varos=varos+weight # Προσθήκη βαρών

# Εμφάνιση
print 'Ο τελευταίος που τα κατάφερε να μπει είναι ο:',atoma-1,'ος'
print''
print 'Ο',atoma,'ος να βγει από το ασανσέρ.'


# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
