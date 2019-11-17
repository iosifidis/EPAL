# -*- coding: utf-8 -*-

# Να αναπτύξετε πρόγραμμα που θα εμφανίζει όλους τους ακέραιους αριθμούς στο διάστημα τιμών από 100 έως και 600 που να είναι πολλαπλάσια του 3 αλλά όχι του 5. Να εμφανίζεται επίσης και ο μέσος όρος των αριθμών αυτών.

# Αρχικοποίηση
sum=0
plithos=0

# Έλεγχος-Επεξεργασία
for i in range(100,601):
    if i%3==0:
        if i%5==0:
            sum=sum-i
            plithos=plithos+1
        else:
            sum=sum+i
            plithos=plithos+1
            print i,

mo=sum/plithos

# Εμφάνιση
print ""
print 'Ο μέσος όρος είναι',mo



# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
