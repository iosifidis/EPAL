# -*- coding: utf-8 -*-

# Σταθερές
pagio=12
kostosmb=0.65

# Εισαγωγή δεδομένων
data=float(input("Δώσε MB συνδρομητή: "))
print ""

# Επεξεργασία
if data<=120:
    pliromi=pagio
elif data>120:
    pliromi=pagio+(data-120)*kostosmb

# Εμφάνιση αποτελεσμάτων
print "Ο πελάτης κατέβασε δεδομένα ",data,"MB. Επομένως θα πληρώσει στην εταιρία",pliromi,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
