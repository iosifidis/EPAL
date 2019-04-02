# -*- coding: utf-8 -*-

#Αθροιστές-Μετρητές
se=0 # Μετρητής είσπραξης επιβατικών
epivatika=0 # Μετρητής επιβατικών
sf=0 # Μετρητής είσπραξης φορτηγών 
fortiga=0 # Μετρητής φορτηγών
moto=0 # Μετρητής μοτοσυκλετών
sm=0 # Μετρητής είσπραξης μοτοσυκλετών
meli=0 # Μετρητής μελών
mmeli=0 # Μετρητής μη μελών
plithos=0 # Μετρητής πλήθους οχημάτων
sum=0 # Σύνολο εισπράξεων

#Ερώτηση και υπολογισμοί
print ''
to=raw_input ("F για φορτηγά\nE για επιβατικά\nM για μοτοσυκλέτες\nTELOS για τέλος\nΔώσε Τύπο οχήματος: ")
print ''
while to!="TELOS":
	melos=raw_input ("Μέλος; (Ν/Ο) ")
	if melos == "N" :
		meli=meli+1
		if to == "F" :
			fortiga=fortiga+1
			poso=70
			sf=sf+poso
		elif to == "E" :
			epivatika=epivatika+1
			poso=40
			se=se+poso
		elif to == "M" :
			moto=moto+1
			poso=25
			sm=sm+poso
	else:
		mmeli=mmeli+1
		if to == "F" :
			fortiga=fortiga+1
			poso=80
			sf=sf+poso
		elif to == "E" :
			epivatika=epivatika+1
			poso=50
			se=se+poso
		elif to == "M" :
			moto=moto+1
			poso=30
			sm=sm+poso

	
	print ''
	to=raw_input ("F για φορτηγά\nE για επιβατικά\nM για μοτοσυκλέτες\nTELOS για τέλος\nΔώσε Τύπο οχήματος: ")

# Υπολογισμοί-Αθροίσματα
plithos=fortiga+epivatika+moto
sum=sf+se+sm	

# Εκτυπώσεις
print ''
print "Φορτηγά: ",fortiga," Είσπραξη: ",sf,"Ευρώ"
print ''
print "Επιβατικά: ",epivatika," Είσπραξη: ",se,"Ευρώ"
print ''
print "Μοτοσυκλέτες: ",moto," Είσπραξη: ",sm,"Ευρώ"
print ''
print "Πλήθος οχημάτων: ",plithos # Μπορώ να βάλω fortiga+epivatika+moto
print ''
print "Σύνολο εισπράξεων: ",sum # Μπορώ να βάλω sf+se+sm
print ''
print "Σύνολο μελών: ",meli
print ''
print "Σύνολο μή μελών: ",mmeli # Βρίσκω τα μη μέλη... plithos-meli 

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
