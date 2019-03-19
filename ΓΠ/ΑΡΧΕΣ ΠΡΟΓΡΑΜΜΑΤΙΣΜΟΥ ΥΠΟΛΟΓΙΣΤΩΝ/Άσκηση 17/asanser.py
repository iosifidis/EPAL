# -*- coding: utf-8 -*-

print '''Ένα ασανσέρ έχει μέγιστο όριο ασφάλειας τα 500 κιλά. Να γράψετε
πρόγραμμα σε Python που θα διαβάζει το βάρος και τη σειρά με την οποία
κάθε άτομο εισέρχεται στο ασανσέρ (π.χ. 45.1, 89.2). Το πρόγραμμα θα
τερματίζει όταν το ασανσέρ γεμίσει (σε σχέση με το μέγιστο επιτρεπτό όριο
ασφαλείας). Στη συνέχεια θα εμφανίζει τη σειρά του τελευταίου ατόμου,
που κατάφερε να μπει στο ασανσέρ.
'''
print ''

# Αθροιστές-Μετρητές
atoma=0 
sum=0
print ''

# Διαβάζει τιμές
while sum<500: 
  varos=float(input('Δώσε βάρος ατόμου που θα εισέλθει στον ανελκηστήρα:'))
  atoma=atoma+1
  sum=sum+varos

# 'Ελεγχος εάν έχει ξεπεράσει τα 500 κιλά, να δηλώσει ως άτομο που μπήκε, το τελευταιο.
if sum==500: 
   atoma=atoma
else:
   print 'Έχετε ξεπεράσει το όριο. Ο τελευταίος να βγει από το ασανσέρ!!!'
   atoma=atoma-1

# Εμφανιση αποτελεσματων ποσού πληρωμής
print ''
print 'Ο τελευταίος που τα κατάφερε να μπει είναι ο:',atoma

# Footer
print ''
print 'Εν κουλί αυτό;'
print 'Ευχαριστούμε για την προτίμησή σας.'
print 'E-mail: iefstathios@gmail.com'
print 'Copyleft 2019, Efstathios Iosifidis'
