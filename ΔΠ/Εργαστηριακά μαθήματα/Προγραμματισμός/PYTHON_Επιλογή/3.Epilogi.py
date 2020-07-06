# -*- coding: utf-8 -*-

# Σταθερές
ekpt100=0.06
ekpt300=0.09
ekpt300k=0.12

# Εισαγωγή δεδομένων
agora=float(input("Δώσε ποσό αγοράς πελάτη σε €: "))
print ""

# Επεξεργασία
if agora<=100:
    ekptosi=agora*ekpt100
    vathmida="6%"
elif agora<=300:
    ekptosi=agora*ekpt300
    vathmida="9%"
else:
    ekptosi=agora*ekpt300k
    vathmida="12%"

# Υπολογισμοί
teliko=agora-ekptosi

# Εμφάνιση αποτελεσμάτων
print "Η αρχική τιμή αγοράς είναι",agora,"€"
print ""
print "Στο ποσό αυτό θα γίνει έκπτωση",vathmida,", δηλαδή",ekptosi,"€"
print ""
print "Το τελικό ποσό πληρωμής στο κατάστημα είναι",teliko,"€"

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
