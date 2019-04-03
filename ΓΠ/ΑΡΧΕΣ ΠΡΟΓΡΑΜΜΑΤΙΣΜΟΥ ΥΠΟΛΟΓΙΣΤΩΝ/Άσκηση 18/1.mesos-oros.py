# -*- coding: utf-8 -*-

print '''Να γραφεί πρόγραμμα το οποίο θα διαβάζει 10 ακεραίους από το πληκτρολόγιο και θα υπολογίζει και θα εκτυπώνει το μέσο όρο των αρτίων αριθμών (μόνο) που διαβάστηκαν.
'''
print ''

# Αθροιστές-Μετρητές 
sum=0 #Αθροιστής
artios=0 #Μετρητής

# Διαβάζει τιμές
for i in range(10):
    number=input('Δώσε μια τιμή:')
    if number%2==0:
        sum=sum+number
        artios=artios+1
    else:
        continue

# Υπολογισμοί
mo=sum/artios

# Εμφανιση αποτελεσματων
print 'Ο μέσος όρος του αθροίσματος των άρτιων αριθμών είναι:',round(mo,2)

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
