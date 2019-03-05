# -*- coding: utf-8 -*-

sum=0
plithosA=0
for i in range(4):
   a=input('Δώσε κατηγορία εισιτηρίου (0,1):')
# ακολουθει φίλτρο εισαγωγής ΕΓΚΥΡΩΝ ΔΕΔΟΜΕΝΩΝ (0 ή 1 στην περίπτωσή μας)
   while a!=0 and a!=1:
       a=input('Δώσε σωστή κατηγορία εισιτηρίου (0,1):')
   if a==0:
      print 'Α θέση'
      sum=sum+50     
      plithosA=plithosA+1
   else:
      print 'Β θέση'
      sum=sum+20        

print 'Α θέση:',plithosA,' επιβάτες'
print 'Β θέση:',4-plithosA,' επιβάτες'

print 'Συνολικό ποσό επιβατών:',sum
