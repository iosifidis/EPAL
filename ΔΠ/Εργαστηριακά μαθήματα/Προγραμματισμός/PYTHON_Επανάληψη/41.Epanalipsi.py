# -*- coding: utf-8 -*-

# Οι καταθέσεις σας στην τράπεζα είναι 6500€ και το επιτόκιο κατάθεσης είναι 5.4%. Να αναπτύξετε πρόγραμμα που θα υπολογίζει σε πόσα έτη το κεφάλαιο θα ξεπεράσει τα 11000€.

# Αρχικοποίηση
arxiko=6500
teliko=11000
epitokio=0.054
eti=0

# Έλεγχος-Επεξεργασία
while arxiko<teliko:
    tokos=arxiko*epitokio
    arxiko=arxiko+tokos
    eti=eti+1
    print arxiko,eti


# Εμφάνιση
print ""
print 'Το κεφάλαιο ξεπέρασε τα 11000 τον',eti,"ο χρόνο"



# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
