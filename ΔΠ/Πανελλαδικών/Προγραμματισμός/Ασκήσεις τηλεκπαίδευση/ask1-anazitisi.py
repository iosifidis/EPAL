# -*- coding: cp1253 -*-
'''
Να αναπτύξετε πρόγραμμα το οποίο: 
α. Διαβάζει 20 ονόματα και τα εισάγει στη λίστα L1. 
β. Διαβάζει 30 ονόματα και τα εισάγει στη λίστα L2. 
γ. Ταξινομεί κατά φθίνουσα σειρά τα ονόματα της λίστας L2. 
δ. Εμφανίζει πόσα από τα ονόματα της λίστας L1 εμφανίζονται στη λίστα L2.
(Θα αξιοποιήσετε το γεγονός ότι τα ονόματα είναι σε αλφαβητική σειρά)
'''

def bubblesort(lista):
    N=len(lista)
    for i in range(N-1):
        for j in range(N-1,i,-1):
            if lista[j]<lista[j-1]:
                lista[j],lista[j-1] = lista[j-1],lista[j]


def diadiki(lista,key):
    first=0
    last=len(lista)-1
    found=False
    while first<=last and not found:
        mid=(first+last)/2
        if lista[mid]==key:
            found=True
        elif lista[mid]<key:
            first=mid+1
        else:
            last=mid-1
    return found

L1=[]
L2=[]
for i in range(20):
    name=raw_input("Dose onoma:")
    L1.append(name)
    
for i in range(30):
    name=raw_input("Dose onoma:")
    L2.append(name)

bubblesort(L2)

for i in range(20):
    onoma=L1[i]
        if diadiki(L2,onoma):
            count=count+1
print count

