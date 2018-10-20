#!/usr/bin/python
# -*- coding: utf-8 -*-

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
			poso=20
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

print "Φορτηγά: ",fortiga," Είσπραξη: ",sf,"Ευρώ"
print "Επιβατικά: ",epivatika," Είσπραξη: ",se,"Ευρώ"
print "Μοτοσυκλέτες: ",moto," Είσπραξη: ",sm,"Ευρώ"
print "Πλήθος οχημάτων: ",plithos #Γ3
print "Σύνολο εισπράξεων: ",sum #Γ3
print "Σύνολο μελών: ",meli #Γ4
print "Σύνολο μή μελών: ",mmeli #Γ4
