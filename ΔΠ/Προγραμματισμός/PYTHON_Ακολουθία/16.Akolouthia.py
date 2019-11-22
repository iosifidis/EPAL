# -*- coding: utf-8 -*-

# Σταθερές

# Εισαγωγή δεδομένων
namea=raw_input("Εισάγετε ονοματεπώνυμο μαθητή: ")
print ""
psifoia=int(input("Εισάγετε ψήφους που έλαβε ο μαθητής: "))
print ""
nameb=raw_input("Εισάγετε ονοματεπώνυμο μαθητή: ")
print ""
psifoib=int(input("Εισάγετε ψήφους που έλαβε ο μαθητής: "))
print ""
namec=raw_input("Εισάγετε ονοματεπώνυμο μαθητή: ")
print ""
psifoic=int(input("Εισάγετε ψήφους που έλαβε ο μαθητής: "))
print ""
named=raw_input("Εισάγετε ονοματεπώνυμο μαθητή: ")
print ""
psifoid=int(input("Εισάγετε ψήφους που έλαβε ο μαθητής: "))
print ""

# Επεξεργασία
psifoi=float(psifoia+psifoib+psifoic+psifoid)
posostoa=(psifoia*100)/psifoi
posostob=(psifoib*100)/psifoi
posostoc=(psifoic*100)/psifoi
posostod=(psifoid*100)/psifoi

# Εμφάνιση αποτελεσμάτων και ερώτημα
print "O",namea,"έλαβε",posostoa,"ποσοστό"
print ""
print "O",nameb,"έλαβε",posostob,"ποσοστό"
print ""
print "O",namec,"έλαβε",posostoc,"ποσοστό"
print ""
print "O",named,"έλαβε",posostod,"ποσοστό"
print ""


# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
