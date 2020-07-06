# -*- coding: utf-8 -*-

# Αρχικοποίηση
import random # Εισαγωγή βιβλιοθήκης
olokliri=[] # Δημιουργία λίστας
thetikoi=[] # Δημιουργία λίστας

# Εισαγωγή δεδομένων
for i in range(1000): # Κάνε 1000 επαναλήψεις
    arithmos=random.randint(-100,100) # Διαβάζει τυχαίους αριθμούς από το -100 έως το 100
    olokliri.append(arithmos) # Προσθέτει τον αριθμό στην λίστα

# Υπολογισμοί
for arithmos in olokliri: # Για κάθε αριθμός από την λίστα olokliri
    if arithmos>0:
        thetikoi.append(arithmos)
print "Η λίστα με τους θετικούς αριθμούς είναι:",thetikoi

# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
