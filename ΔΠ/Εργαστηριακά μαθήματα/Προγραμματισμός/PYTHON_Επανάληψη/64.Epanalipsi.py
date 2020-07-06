# -*- coding: utf-8 -*-

"""  Στις τελευταίες εξετάσεις Αγγλικών για το First Certificate ένα φροντιστήριο εκπροσωπήθηκε από 220 μαθητές. Να αναπτύξετε πρόγραμμα που θα διαβάζει για καθέναν από τους μαθητές αυτούς τον βαθμό που πήρε στις εξετάσεις και θα εκτυπώνει το ποσοστό επιτυχίας του φροντιστηρίου, καθώς και τον αριθμό των μαθητών που τελικά δεν κατόρθωσαν να αποκτήσουν το First Certificate. Πόσοι εξεταζόμενοι πήραν βαθμό C;
ΣΗΜΕΙΩΣΗ: Να θεωρήσετε ότι όλοι οι βαθμοί που εισάγονται θεωρούνται έγκυροι.
Επιτυχία έχουμε αν ο βαθμός του μαθητή είναι A, B ή C.
"""

# Ερώτημα α
# Αρχικοποίηση
perasan=0.0
perasanC=0.0

# Εισαγωγή δεδομένων
for i in range(220):
	vathmos=raw_input("Δώστε βαθμό μαθητή:")
	if vathmos=="A" or vathmos=="B":
		perasan=perasan+1
	elif vathmos=="C":
		perasanC=perasanC+1

print ""

# Έλεγχος-Επεξεργασία
perasmenoi=(perasan+perasanC)/220*100
apetihan=220-perasan-perasanC

# Εμφάνιση
print "Πέρασαν",perasmenoi,"%"
print ""
print "Απέτυχαν",apetihan,"μαθητές"
print ""
print "Οι μαθητές που πέρασαν με C ήταν",perasanC

# Footer
print ''
print 'Ιάσο κόκλα'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
