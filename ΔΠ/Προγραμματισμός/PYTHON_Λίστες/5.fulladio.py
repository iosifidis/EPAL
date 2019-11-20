# -*- coding: utf-8 -*-

# Αρχικοποίηση
import datetime # Εισαγωγή βιβλιοθήκης
now = datetime.datetime.now() # Παίρνω την σημερινή ημερομηνία
ONOMA=[] # Δημιουργία Λίστας
ETOS_GEN=[] # Δημιουργία Λίστας
psifizoun=0 # Μετρητής


# Δημιουργία λίστας
for i in range(3426): # Κάνε 3426 επαναλήψεις
    name=raw_input("Δώσε όνομα:") # Διαβάζει όνομα
    ONOMA.append(name) # Προσθέτει ονόματα στην λίστα
    print ""
    etos=int(input("Δώσε έτος γέννησης:")) # Διαβάζει έτος γέννησης    
    ETOS_GEN.append(etos) # Προσθέτει το έτος γέννησης στην λίστα
    print ""

# Ερώτημα α
PSIFIZOUN_NAMES=[] # Δημιουργώ την λίστα αυτών που ψηφίζουν.

for i in range(3426): # Κάνε 3426 επαναλήψεις
    if now.year-ETOS_GEN[i]>=18: # Συγκρίνω εάν η ηλικία του είναι πάνω από 18
        psifizoun=psifizoun+1 # Πρόσθεσε ένα
        PSIFIZOUN_NAMES.append(ONOMA[i]) # Προσθήκη του ονόματος σε μια νέα λίστα

print "Τα άτομα που ψηφίζουν είναι:",PSIFIZOUN_NAMES # Θεωρητικά μπορεί να μπει μέσα στην επανάλληψη ως ONOMA[i]
print ""
print "Το πλήθος των ατόμων που ψηφίζουν είναι:",psifizoun
print ""

# Ερώτημα β
OGDONTARHDES=[] #  Δημιουργώ λίστα με τα άτομα άνω των 80 ετών
for i in range(3426): # Κάνε 3426 επαναλήψεις
    if now.year-ETOS_GEN[i]>=80: # Εάν έχει ηλικία πάνω από 80
        OGDONTARHDES.append(ONOMA[i]) # Πρόσθεσε το όνομα σε λίστα

print "Τα άτομα άνω των 80 ετών είναι:",OGDONTARHDES # Θεωρητικά μπορεί να μπει στην επανάλληψη και να εμφανίζει όνομα

# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
