# -*- coding: utf-8 -*-



# Εισαγωγή δεδομένων
afm=int(input("Δώσε ΑΦΜ: "))
print ""
eisodima=float(input("Δώσε εισόδημα: "))
print ""

# Επεξεργασία
if afm%10==1 or afm%10==2:
    k="M"
else:
    k="EE"

if k=="EE":
    foros=eisodima*0.3
else:
    if eisodima<=10000:
        foros=0
    elif eisodima<=20000:
        foros=eisodima*0.15
    else:
        foros=eisodima*0.25


# Εμφάνιση αποτελεσμάτων
print "ΦΟΡΟΣ",foros,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
