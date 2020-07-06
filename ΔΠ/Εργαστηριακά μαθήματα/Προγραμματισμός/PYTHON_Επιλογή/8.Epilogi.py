# -*- coding: utf-8 -*-



# Εισαγωγή δεδομένων
print "Όπως κάθε χρόνο, ήρθε η ώρα για πληρωμή των τελών κυκλοφορίας."
print "Παρακαλείστε να εισάγετε τον τύπο του οχήματος και τον κυβισμό όταν σας ζητηθεί:"
print "Για αυτοκίνητα, πληκτρολογήστε το γράμμα Α"
print "Για δίκυκλα, πληκτρολογήστε το γράμμα Δ"
print ""
oxima=raw_input("Δώσε τύπο οχήματος: ")
print ""
kivika=int(input("Δώσε κυβικά: "))
print ""

# Επεξεργασία
if oxima=="Δ" or oxima=="δ" or oxima=="D" or oxima=="d"
	if kivika<=500:
	    pliromi=50
	else:
	    pliromi=100
else:
	if kivika<=1358:
	    pliromi=100
	elif kivika<=1750:
	    pliromi=150
	elif kivika<=2000:
	    pliromi=200
	elif kivika>2000:
	    pliromi=300


# Εμφάνιση αποτελεσμάτων
print "Το ποσό τελών είναι",pliromi,"€"


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
