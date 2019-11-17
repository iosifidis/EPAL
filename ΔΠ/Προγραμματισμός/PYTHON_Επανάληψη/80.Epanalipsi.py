# -*- coding: utf-8 -*-

total=0

# Εισαγωγή δεδομένων
psonia=float(input("Δώσε κόστος προϊόντος:"))
print ''

#Έλεγχος-Επεξεργασία
while total<=500: 
    total=total+psonia
    psonia=float(input("Δώσε κόστος άλλου προϊόντος:"))

# Εμφάνιση
if total>500:
   total=total-psonia
print 'Ξοδέψαμε',total,'Ευρώ'


# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
