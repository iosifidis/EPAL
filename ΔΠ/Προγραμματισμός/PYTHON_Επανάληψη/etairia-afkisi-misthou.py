# -*- coding: utf-8 -*-

# Άσκηση όπου υπολογίζει την αύξηση μισθού σε μια εταιρία 1200 υπαλλήλων, ανάλογα με τα χρόνια εργασίας

# Αρχικοποίηση
sum=0 # Αθροιστής για αυτούς με πάνω από 6 έτη εργασίας
max=0 # Για να υπολογίσω τον εργαζόμενο με την μεγαλύτερη αύξηση
ekato=0 # Μετρητής για να βρώ ποσοστό εργαζομένων με αύξηση άνω των 100Ε
eksi_eti=0 # Μετρητής για εργαζομένους με εργασία πάνω από 6 έτη

#Έλεγχος-Επεξεργασία-Εισαγωγή δεδομένων
for i in range(1200):
    name=raw_input("Δώσε όνομα εργαζομένου:")
    print ''
    misthos=float(input("Δώσε μισθό:"))
    print ''
    while misthos<0: # Έλεγχος εγκυρότητας
        misthos=float(input("Ο μισθός δεν μπορεί να είναι αρνητικός. Δώσε σωστά το μισθό:"))
        print ''
    eti=int(input("Δώσε έτη εργασίας:"))
    print ''
    while eti<0: # Έλεγχος εγκυρότητας
        eti=int(input("Τα έτη δεν μπορεί να είναι αρνητικός αριθμός. Δώσε σωστά τα έτη:")) 
        print ''
    if eti<=3:
        misthost=misthos+misthos*0.05
    elif eti>=4 and eti<6:
        misthost=misthos+misthos*0.09
    else:
        sum=sum+misthos*0.12 # Αθροίζω την αύξηση των εργαζομένων με πάνω από 6 έτη
        eksi_eti=eksi_eti+1 # Αθροίζω τους εργαζόμενους με υπηρεσία άνω των 6 ετών
        misthost=misthos+misthos*0.12
    if misthost-misthos>100: # Αν η αύξηση είναι άνω των 100Ε
        ekato=ekato+1 # Κράτα τον αριθμό των εργαζομένων
    if misthost-misthos>max: # Αν η διαφορά ξεπερνά το μέγιστο
        max=misthost-misthos # Όρισε νέο μέγιστο
        maxname=name # Αποθήκευσε το όνομα του εργαζομένου
    print "Ο",name,"έχει νέο μισθό",misthost,"Ευρώ"
    print '' 

pososto100=ekato/1200*100

# Εμφάνιση
if eksi_eti!=0:
    print 'Ο μέσος όρος αύξησης των υπαλλήλων άνω των 6 ετών είναι:',sum/eksi_eti,'Ευρώ'
else:
    print "Δεν υπάρχει εργαζόμενος στην εταιρία που εργάζεται πάνω από 6 ετη."

print ''
print "Το ποσοστό των υπαλλήλων με αύξηση πάνω από 100ευρώ είναι",pososto100,"%"

print ''
print 'Ο υπάλληλος με την μεγαλύτερη αύξηση είναι ο',maxname '

# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
