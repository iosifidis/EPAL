# -*- coding: utf-8 -*-

# Αρχικοποίηση
nikes1=0
nikes2=0

# Εισαγωγή δεδομένων
player1=raw_input("Δώσε όνομα παίκτη 1: ")
print ""
player2=raw_input("Δώσε όνομα παίκτη 2: ")
print ""
print "Π για Πέτρα, Ψ για Ψαλίδι, Χ για Χαρτί, Τ για Τέλος"
print ""
epilogi1=raw_input("Δώσε επιλογή παίκτη 1: ")
print ""
epilogi2=raw_input("Δώσε επιλογή παίκτη 2: ")

#Έλεγχος
while epilogi1!="Τ" and epilogi2!="Τ":
    if epilogi1=="Π":
        if epilogi2=="Ψ":
            nikes1=nikes1+1
        elif epilogi2=="Χ":
            nikes2=nikes2+1
    elif epilogi1=="Ψ":
        if epilogi2=="Χ":
            nikes1=nikes1+1
        elif epilogi2=="Π":
            nikes2=nikes2+1
    elif epilogi1=="Χ":
        if epilogi2=="Π":
            nikes1=nikes1+1
        elif epilogi2=="Ψ":
            nikes2=nikes2+1
    print ""
    print "Για να ξαναπαίξετε: Π για Πέτρα, Ψ για Ψαλίδι, Χ για Χαρτί, Τ για Τέλος"
    print ""
    epilogi1=raw_input("Δώσε επιλογή παίκτη 1: ")
    print ""
    epilogi2=raw_input("Δώσε επιλογή παίκτη 2: ")
    

# Επεξεργασία-Αποτελέσματα
print ""
if nikes1>nikes2:
    print "Νίκησε ο ",player1
elif nikes1<nikes2:
    print "Νίκησε ο ",player2
else:
    print "ΤΟ ΠΑΙΧΝΙΔΙ ΕΛΗΞΕ ΙΣΟΠΑΛΟ"



# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
