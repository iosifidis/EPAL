# -*- coding: utf-8 -*-

# Σταθερές
epivarinsi=0.04
amavres=0.05
color=0.11

# Εισαγωγή δεδομένων
posesamavres=int(input("Δώσε αριθμό ασπρόμαυρων φωτωτυπιών: "))
print ""
posescolor=int(input("Δώσε αριθμό έχγρωμων φωτοτυπιών: "))
print ""


# Επεξεργασία
tempkostos=posesamavres*amavres+posescolor*color
kostos=tempkostos+tempkostos*epivarinsi

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Ποσό καταβολής",kostos,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
