# -*- coding: utf-8 -*-
'''
∆ίνεται το παρακάτω τμήμα προγράμματος Python:
for i  in range (0, 100, 5) 
   print i 
 Το τμήμα αυτό του προγράμματος εμφανίζει διαδοχικά τους 
αριθμούς 0, 5, 10, … , 95. Να τροποποιήσετε τον παραπάνω
κώδικα έτσι ώστε αυτοί να εμφανίζονται σε αντίστροφη σειρά.
'''
for i  in range (0, 100, 5): 
    print i 

print "Λύση"
for i in range(95,-1,-5):
    print i
