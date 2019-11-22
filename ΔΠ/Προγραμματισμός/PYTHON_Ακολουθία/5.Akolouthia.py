# -*- coding: utf-8 -*-

# Σταθερές
fpa=0.23

# Εισαγωγή δεδομένων
onoma=raw_input("Δώσε ονοματεπώνυμο πελάτη: ")
print ""
kodikos=raw_input("Δώσε τον κωδικό του προϊόντος: ")
print ""
posoagoras=float(input("Δώσε ποσό αγοράς σε €: "))
print ""
pososto=float(input("Δώσε ποσοστό έκπτωσης σε %: "))
print ""

# Επεξεργασία
ekptosi=posoagoras*pososto/100
aksiametaekptosi=posoagoras-ekptosi
aksiafpa=aksiametaekptosi*fpa
telikiaksia=aksiametaekptosi+aksiafpa

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "*****ΑΠΟΔΕΙΞΗ ΛΙΑΝΙΚΗΣ ΠΩΛΗΣΗΣ*****"
print "*ΟΝΟΜΑΤΕΠΩΝΥΜΟ ΠΕΛΑΤΗ: ",onoma
print "*ΚΩΔΙΚΟΣ ΠΡΟΙΟΝΤΟΣ: ",kodikos
print "*ΠΟΣΟΣΤΟ ΕΚΠΤΩΣΗΣ: ",int(pososto),"%"
print "*ΑΞΙΑ ΠΡΟΙΟΝΤΟΣ: ",posoagoras
print "*ΑΞΙΑ ΕΚΠΤΩΣΗΣ: ",ekptosi
print "*ΦΠΑ 23%:",aksiafpa
print "*ΤΕΛΙΚΗ ΑΞΙΑ:",telikiaksia
print "***********ΤΕΛΟΣ ΕΚΤΥΠΩΣΗΣ***********"

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
