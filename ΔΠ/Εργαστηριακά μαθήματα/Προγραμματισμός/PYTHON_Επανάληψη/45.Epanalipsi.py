# -*- coding: utf-8 -*-

# Να αναπτύξετε πρόγραμμα που θα διαβάζει κάποιο πλήθος θετικών ακεραίων και θα τερματίζει όταν εισαχθεί αρνητικός αριθμός ή το 0. Για τους αριθμούς που διαβάστηκαν θα εκτυπώνει: 
# α. το πλήθος,
# β. το μέσο όρο,
# γ. το πλήθος των άρτιων,
# δ. το μέσο όρο των άρτιων.

# Αρχικοποίηση
sum=0.0 # Αθροιστής
sum_artioi=0.0 # Αθροιστής
artioi=0 # Μετρητής
plithos=0 # Μετρητής

# Εισαγωγή δεδομένων
arithmos=int(input("Δώστε θετικό ακέραιο αριθμό ή αρνητικό για τερματισμό:"))

# Έλεγχος-Επεξεργασία
while arithmos>0:
    plithos=plithos+1
    sum=sum+arithmos
    if arithmos%2==0:
        artioi=artioi+1
        sum_artioi=sum_artioi+arithmos
    print ''
    arithmos=int(input("Δώστε θετικό ακέραιο αριθμό ή αρνητικό για τερματισμό:"))
    print ''

# Εμφάνιση
if plithos!=0:
    mo=sum/plithos
    print 'Ο μέσος όρος είναι',mo
else:
    print "Δεν υπάρχει μέσος όρος."

if artioi!=0:
    mo_artioi=sum_artioi/artioi
    print 'Ο μέσος όρος των άρτιων είναι',mo_artioi
else:
    print "Δεν υπάρχει μέσος όρος."

print "Το πλήθος των αριθμών είναι",plithos,". Από αυτούς άρτιοι είναι",artioi

# Footer
print ''
print 'Πω πω μια στροφάρα!!! Έλα γιώργη...'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
