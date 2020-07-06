# -*- coding: utf-8 -*-
import datetime
now = datetime.datetime.now()
AR=[]
POSO=[]
sum=0
for i in range(2):
	arithmosk=raw_input("Δώσε αριθμό κυκλοφορίας:")
	AR.append(arithmosk)
	xronos=int(input("Δώσε χρόνο κυκλοφορίας:"))
	kivika=int(input("Δώσε κυβικά:"))
	if (now.year-xronos)>10:	
		if kivika<1000:
			poso=120
		elif kivika>=1000 and kivika<=1999:
			poso=240
		else:
			poso=300
	else:
		if kivika<1000:
			poso=90
		elif kivika>=1000 and kivika<=1999:
			poso=130
		else:
			poso=190

	sum=sum+poso
	POSO.append(poso)

print "Το συνολικό ποσό που πρέπει να πληρώσει η εταιρία είναι",sum
min=POSO[0]
for i in range(2):
	if POSO[i]<min:
		min=POSO[i]
print "Το μικρότερο ποσό που πρέπει να πληρώσει η εταιρία είναι",min

for i in range(2):
	if POSO[i]==min:
		print "Ο αριθμός",AR[i],"χρειάζεται να πληρώσει το ποσό",min

for i in range(2):
	if "ΚΝΖ" in AR[i]:
		print "O",AR[i],"πρέπει να πληρώσει:",POSO[i]

