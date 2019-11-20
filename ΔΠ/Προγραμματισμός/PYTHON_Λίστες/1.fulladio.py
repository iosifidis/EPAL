# -*- coding: utf-8 -*-

# Αρχικοποίηση
thetikoi=0 # Μετρητής
arnitikoi=0 # Μετρητής
arithmoi=[] # Δημιουργία Λίστας

# Εισαγωγή δεδομένων - Έλεγχος δεδομένων
for i in range(80): # Κάνε 80 επαναλήψεις
    arithmos=int(input("Δώσε αριθμό:")) # Διαβάζει αριθμό
    print ""
    arithmoi.append(arithmos) # Προσθέτει τον αριθμό στην λίστα
for arithmos in arithmoi: # Ελέγχει κάθε αριθμό της λίστας (Εναλλακτικά for i in range(80):)
    if arithmos>0: # Εάν ο αριθμός είναι θετικός (Εναλλακτικά if arithmoi[i]>0:)
        thetikoi=thetikoi+1 # Πρόσθεσε ένα
    else: # Αν δεν είναι θετικός (δηλαδή αρνητικός)
        arnitikoi=arnitikoi+1 # Πρόσθεσε ένα στους αρνητικούς
  

# Αποτελέσματα
print "" # Το βάζω για να έχει οπτικά μια σειρά κενό.
print "Το πλήθος των θετικών αριθμών είναι:",thetikoi # Εμφάνιση πλήθους θετικών
print "" # Το βάζω για να έχει οπτικά μια σειρά κενό.
print "Το πλήθος των αρνητικών είναι:",arnitikoi # Εμφάνιση πλήθους αρνητικών
print "" # Το βάζω για να έχει οπτικά μια σειρά κενό.

# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
