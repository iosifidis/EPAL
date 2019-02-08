# -*- coding: cp1253 -*-
# Επίσκεψη σε μουσείο. Πόσα θα πληρώσουμε;
mathites=int(input('Πόσοι θα επισκεφθούν το μουσείο: '))
sum=0 #μηδενίζω τον αθροιστή
en=0 #μηδενίζω τον αθροιστή
an=0 #μηδενίζω τον αθροιστή
for i in range(0,mathites):
    age=input('Δώσε ηλικία του επισκέπτη :')
    if age>=18:
        sum=sum+20 #αθροιστής
        en=en+1 #αθροιστής
    else:
        sum=sum+15 #αθροιστής
        an=an+1 #αθροιστής
print ''
print 'Οι ενήλικες ειναι ',en,'ενώ οι ανήλικες ειναι ',an
print 'Το τελικό ποσό είναι ',sum,' Euros'
print ''

# Footer
print ''
print 'Μην παραχαράσετε την ιστορία.'
print 'Ευχαριστούμε για την προτίμησή σας.'
print ''
print 'Copyleft 2019, Efstathios Iosifidis'
