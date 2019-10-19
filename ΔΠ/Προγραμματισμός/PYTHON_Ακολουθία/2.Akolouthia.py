# -*- coding: utf-8 -*-

# Σταθερές
pagio=9
lepto=0.003
sms=0.043
fpa=0.23

# Εισαγωγή δεδομένων
kodikos=raw_input("Δώσε κωδικό πελάτη: ")
print ""
omilia=float(input("Δώσε λεπτά ομιλίας πελάτη: "))
print ""
sms_ola=int(input("Δώσε SMS του πελάτη: "))
print ""

# Επεξεργασία
timi=omilia*lepto*fpa+sms_ola*sms*fpa+pagio*fpa

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Ο πελάτης με κωδικό",kodikos,"πρέπει να πληρώσει",round(timi,2),"€"

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
