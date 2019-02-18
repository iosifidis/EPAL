# -*- coding: cp1253 -*-
min=20
max=0
athroisma=0
for i in range(25):
   g=int(input("Δώσε βαθμό στο μάθημα Προγραμματισμός Η/Υ: "))
   athroisma=athroisma+g
   if g>max:
     max=g
   if g<min:
    min=g
mo=athroisma/25.0
print "Ο μέσος όρος είναι: ",mo
print "Ο μικρότερος είναι: ",min
print "Ο μεγαλύτερος είναι: ",max

