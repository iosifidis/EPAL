# -*- coding: utf-8 -*-

# Αρχικοποίηση
import random # Εισάγω βιβλιοθηκη
zaries1=[] # Δημιουργώ λίστα για 1ο ζάρι
zaries2=[] # Δημιουργώ λίστα για 2ο ζάρι
diples=0 # Μετρητής
pano10=0 # Μετρητής

# Εισαγωγή δεδομένων
for i in range(500): # Κάνε 500 επαναλήψεις
    zari1=random.randint(1,6) # Διαβάζει τυχαίους αριθμούς από το 1 έως το 6
    zaries1.append(zari1) # Προσθέτει την ζαριά στην λίστα zaries1
    zari2=random.randint(1,6) # Διαβάζει τυχαίους αριθμούς από το 1 έως το 6
    zaries2.append(zari2) # Προσθέτει την ζαριά στην λίστα zaries2

# Ερώτημα α
for i in range(500): # Κάνε 500 επαναλήψεις
    if zaries1[i]==zaries2[i]: # Εάν η η ζαριά στην πρώτη λίστα είναι ίση με την ζαριά της 2ης λίστας
        diples=diples+1 # Πρόσθεσε ένα

print "Οι διπλές που καταγράφηκαν είναι:",diples
print ""

# Ερώτημα β
posostodiples=diples/500.0*100 # Υπολογισμός ποσοστού
print "Το ποσοστό των διπλών ήταν",posostodiples,"%"
print ""

# Ερώτημα γ
for i in range(500): # Κάνε 500 επαναλήψεις
    if zaries1[i]+zaries2[i]>=10: # Εάν το άθροισμα των ζαριών είναι πάνω από 10
        pano10=pano10+1 # Πρόσθεσε ένα

print "Το πλήθος των ζαριών με άθροισμα πάνω από 10 ήταν:",pano10,"φορες"

# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
