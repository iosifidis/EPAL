# -*- coding: utf-8 -*-

#Αθροιστές-Μετρητές
se=0
epivatika=0
sf=0
fortiga=0
moto=0
sm=0
meli=0
mmeli=0
plithos=0
sum=0

#Ερώτηση και υπολογισμοί
to=raw_input ("Τύπος οχήματος: (Fortiga/Epivatika/Moto/TELOS) ")
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

	plithos=fortiga+epivatika+moto
	sum=sf+se+sm
	to=raw_input ("Τύπος οχήματος: (Fortiga/Epivatika/Moto/TELOS) ")

# Εκτυπώσεις
print "Φορτηγά: ",fortiga," Είσπραξη: ",sf,"Ευρώ"
print "Επιβατικά: ",epivatika," Είσπραξη: ",se,"Ευρώ"
print "Μοτοσυκλέτες: ",moto," Είσπραξη: ",sm,"Ευρώ"
print "Πλήθος οχημάτων: ",plithos
print "Σύνολο εισπράξεων: ",sum
print "Σύνολο μελών: ",meli
print "Σύνολο μή μελών: ",mmeli

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'