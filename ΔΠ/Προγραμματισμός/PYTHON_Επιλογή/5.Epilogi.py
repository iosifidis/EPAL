# -*- coding: utf-8 -*-

# Σταθερές
pagio=12
fpa=0.23

# Σταθερές χρεώσεων
# Ομιλία
o200=0.12
o400=0.09
o400k=0.06
#SMS
sms_xr=0.15
#MMS
mms_xr=0.40

# Εισαγωγή δεδομένων
omilia=float(input("Δώσε χρόνο ομιλίας: "))
print ""
sms=int(input("Δώσε αριθμό SMS: "))
print ""
mms=int(input("Δώσε αριθμό mms: "))
print ""

# Επεξεργασία ομιλίας
if omilia<=200:
    pliromi_omilias=omilia*o200
elif omilia<=400:
    pliromi_omilias=omilia*o400
else:
    pliromi_omilias=omilia*o200k

# Επεξεργασία SMS
if sms<=50:
    pliromi_sms=0
else:
    pliromi_sms=sms*sms_xr

#Επεξεργασία MMS
pliromi_mms=mms*mms_xr

# Υπολογισμοί προς εκτύπωση
pliromi=pliromi_omilias+pliromi_sms+pliromi_mms
poso_fpa=pliromi*fpa
teliko=pliromi+poso_fpa+pagio


# Εμφάνιση αποτελεσμάτων
print "Ο πελάτης πρέπει να πλρώσει",teliko,"€"
print ""
print "Στο παραπάνω ποσό αναλογεί ΦΠΑ ",poso_fpa,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
