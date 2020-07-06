# -*- coding: cp1253 -*-

'''
Να γράψετε μια συνάρτηση σε Python, η οποία θα δέχεται μια λίστα, θα ελέγχει αν τα στοιχεία της είναι σε αύξουσα σειρά και θα επιστρέφει αντίστοιχα Τrue ή False.
'''

def taxin(L):
    correct = True
    i = 0
    N = len(L)-1
    while correct and i<N :
        if L[ i ] > L[ i+1 ] :
          correct = False
        i = i +1
    return correct

M=[2,5,12,18,24,32]
M1=[3,8,14,12,25]
if taxin(M)==True:
    print "η λίστα είναι ταξινομημένη"
else:
   print "η λίστα δεν είναι ταξινομημένη" 
keno=input("πατήστε ένα πλ΄ηκτρο για να συνεχίσετε:")
control=taxin(M1)
if control==True:
    print "η λίστα είναι ταξινομημένη"
else:
   print "η λίστα δεν είναι ταξινομημένη"
