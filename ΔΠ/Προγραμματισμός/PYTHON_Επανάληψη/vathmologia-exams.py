# -*- coding: utf-8 -*-

# Άσκηση όπου υπολογίζει την βαθμολογία υποψηφίου στις πανελλαδικές

# Αρχικοποίηση
max=0
diakosia=0.0
mathites=0
perasan=0

# Εισαγωγή δεδομένων
name=raw_input("Δώσε όνομα μαθητή:")
print ''

#Έλεγχος-Επεξεργασία
while name!=" ": 
  mathites=mathites+1 # Μετρητής μαθητών
  math1=float(input("Βαθμολογητής 1: Δώστε βαθμό Μαθηματικών 0-100:"))
  math2=float(input("Βαθμολογητής 2: Δώστε βαθμό Μαθηματικών 0-100:"))
  ne1=float(input("Βαθμολογητής 1: Δώστε βαθμό Νέα Ελληνικά 0-100:"))
  ne2=float(input("Βαθμολογητής 2: Δώστε βαθμό Νέα Ελληνικά 0-100:"))
  eidikotita1=float(input("Βαθμολογητής 1: Δώστε βαθμό στο πρώτο μάθημα ειδικότητας 0-100:"))
  eidikotita2=float(input("Βαθμολογητής 2: Δώστε βαθμό στο πρώτο μάθημα ειδικότητας 0-100:"))
  meidikotita1=float(input("Βαθμολογητής 1: Δώστε βαθμό στο δεύτερο μάθημα ειδικότητας 0-100:"))
  meidikotita2=float(input("Βαθμολογητής 2: Δώστε βαθμό στο δεύτερο μάθημα ειδικότητας 0-100:"))
  math=(math1+math2)*1.5
  ne=(ne1+ne2)*1.5
  eidikotita=(eidikotita1+eidikotita2)*3.5
  meidikotita=(meidikotita1+meidikotita2)*3.5
  total=math+ne+eidikotita+meidikotita # Πρόσθεση όλων των βαθμολογιών
  print "Ο μαθητής",name,"έγραψε",total,"μόρια"
  print ""
  if total>=1675: # Έλεγχος πόσοι πέρασαν τη βάση
    perasan=perasan+1 # Μετρητής μαθητών που πέρασαν τη βάση
  if total>=1875: # Έλεγχος πόσοι είχαν 200 πάνω από την βάση
    diakosia=diakosia+1 # Μετρητής μαθητών που είχαν 200 μόρια πάνω από την βάση
  if total>max: # Έλεγχος μαθητή με τον μεγαλύτερο βαθμό
    maxname=name # Διατήρηση του ονόματος του μαθητή με τον ψηλότερο βαθμό
  name=raw_input("Δώσε όνομα επόμενου μαθητή ή κενό για έξοδο.") # Ερώτημα για να βγω από την επανάληψη

# Εμφάνιση
print ""
if perasan!=0:
    print 'Το πλήθος των μαθητών που πέρασαν ήταν',perasan,'άτομα'
else:
    print "Δεν πέρασε κανείς."
print ""
if mathites!=0:
    pososto200=diakosia/mathites*100
    print 'Το ποσοστό των μαθητών που συγκέντρωσαν έως πάνω από 200 μόρια από την βάση ήταν',pososto200,'%'
else:
    print "Κανείς δεν πέρασε ή δεν εισάγατε βαθμολογία μαθητή."
print ""
if mathites!=0:
    print 'Ο μαθητής με την υψηλότερη βαθμολογία ήταν ο',maxname
else:
    print "Δεν εισάγατε βαθμολογία μαθητή."
print ""


# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
