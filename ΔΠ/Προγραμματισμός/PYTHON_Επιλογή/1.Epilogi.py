# -*- coding: utf-8 -*-

# Εισαγωγή δεδομένων
vathmos=float(input("Δώσε βαθμό μαθητή (από 0 έως 20): "))

#Έλεγχος
while vathmos<0 or vathmos>20:
    print ""
    print "Ο βαθμός που δώσατε είναι εκτός ορίων 0 έως 20."
    print ""
    vathmos=float(input("Δώσε βαθμό μαθητή (από 0 έως 20): "))

# Επεξεργασία
if vathmos>=0 and vathmos<=20:
	if vathmos<9.5:
    		print "Απορρίπτεται"
	elif vathmos<=13:
	    print "Σχεδον Καλά"
	elif vathmos<=16:
    	    print "Καλά"
	elif vathmos<=18:
	    print "Πολύ Καλά"
	elif vathmos>18:
	    print "Άριστα"
else:
	print "Ο βαθμός που δώσατε είναι εκτός ορίων 0 έως 20."

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
