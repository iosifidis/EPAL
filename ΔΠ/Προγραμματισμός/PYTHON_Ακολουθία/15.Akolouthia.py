# -*- coding: utf-8 -*-

# Η άσκηση έχει κάποιες ασάφειες γενικά!!! Σύμφωνα με την εκφώνηση, αυτά είναι τα ζητούμενα.
# Σταθερές
bus_ticket=170
passenger_ticket=25

# Εισαγωγή δεδομένων
bus=int(input("Εισάγετε τον αριθμό των λεωφορείων: "))
print ""
epivates=int(input("Εισάγετε αριθμό συμμετεχόντων μαζί με οδηγούς: "))
print ""

# Επεξεργασία
cost=bus*bus_ticket+epivates*passenger_ticket

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "Το πληρωτέο ποσό είναι",cost,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
