# -*- coding: cp1253 -*-
'''
Να γράψετε μια συνάρτηση σε Python η οποία θα δέχεται μια λίστα με λογικές τιμές True/False και θα διαχωρίζει τις τιμές αυτές, τοποθετώντας τα True πριν από τα False.
'''

def sortTrue(L):
    for i in range(len(L)):
        if L[i]==True:
            L.insert(0,L.pop(i))
    return L

L=[]
for i in range(5):
    timi=input("Δώστε True ή False:");
    print timi
    L.append(timi)
print L
k=count_true(L)
print k
