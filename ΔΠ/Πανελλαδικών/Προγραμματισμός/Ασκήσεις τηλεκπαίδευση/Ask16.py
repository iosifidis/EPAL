# -*- coding: cp1253 -*-
'''
Σε ένα ηλεκτρονικό κατάστημα (e-shop) σχολικών ειδών, κάθε φορά που ο πελάτης επιλέγει ένα νέο προϊόν για αγορά, αυτό μαζί με την τιμή του τοποθετούνται στο καλάθι αγορών μαζί με τα ήδη υπάρχοντα που έχει επιλέξει.Αν θέλει να αναιρέσει κάποια αγορά του, απλώς την αφαιρεί από το καλάθι αγορών. 
Να αναπτύξετε πρόγραμμα που διαχειρίζεται το καλάθι αγορών του καταστήματος για ένα πελάτη, ως εξής:
Α. Θα χρησιμοποιεί τις λίστες ON και ΤIΜI για την υλοποίηση του καλαθιού αγορών, όπου στην πρώτη θα τοποθετούνται οι ονομασίες των προϊόντων και στη δεύτερη οι αντίστοιχες τιμές τους.

Β. Θα διαβάζει επαναληπτικά την ενέργεια του πελάτη ελέγχοντας ότι δέχεται μόνο τις επιτρεπόμενες τιμές.
Επιτρεπόμενες τιμές είναι “B” για αγορά νέου προϊόντος, “C” για ακύρωση της τελευταίας αγοράς του και “E” για τερματισμό των αγορών. Αν ο πελάτης αγοράσει ένα νέο προϊόν, τότε:
i.  θα διαβάζει την ονομασία καιτην τιμή του και θα τα εισάγει στο καλάθι αγορών (στις 2 λίστες).
ii. Στη συνέχεια τα προϊόντα θα ταξινομούνται βάση της ονομασίας τους σε αύξουσα ταξινόμηση.

Αν ο πελάτης θέλει να ακυρώσει κάποια αγορά του, τότε: 
i.  θα καλεί συνάρτηση δυαδικής αναζήτησης με την ονομασία του προϊόντος που επιθυμεί να διαγράψει και, αν το προϊόν υπάρχει στο καλάθι αγορών, θα πραγματοποιείται η διαγραφή, 
ii.  διαφορετικά εμφανίζει το μήνυμα «Το προϊόν δεν υπάρχει».

Η διαδικασία επαναλαμβάνεται μέχρι ο πελάτης να επιλέξει τον τερματισμό των αγορών του.

Γ. Αν το καλάθι αγορών είναι άδειο θα εμφανίζει το μήνυμα «Δεν πραγματοποιήθηκαν αγορές», διαφορετικά:
i.  Θα εμφανίζει το όνομα κάθε προϊόντος, το πλήθος των προϊόντων και τη συνολική αξία τους.
ii.  Αν πραγματοποιήθηκαν αναιρέσεις αγορών, θα εμφανίζει πόσες φορές πραγματοποιήθηκε αναίρεση προϊόντος.
iii.  Θα εμφανίζει την ονομασία του προϊόντος με τη μεγαλύτερη τιμή.
'''

def bubble(lista1,lista2):
    n=len(lista1)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if lista1[j]<lista1[j-1]:
                lista1[j],lista1[j-1]=lista1[j-1],lista1[j]
                lista2[j],lista2[j-1]=lista2[j-1],lista2[j]
                
def search(lista,key):
    first=0
    last=len(lista)-1
    position=-1
    while position==-1 and first<=last:
        mid=(first+last)/2
        if key==lista[mid]:
            position=mid
        elif key>lista[mid]:
            first=mid+1
        else:
            last=mid-1
    return position

ON=[]
TIMI=[]
sum=0
plithos=0
choice=raw_input("Parakalo doste tin energeia pou epithimeite:")
while not(choice=="B" or choice=="C" or choice=="E"):
    choice=raw_input("Parakalo doste tin energeia pou epithimeite:")
while choice!="E":
    if choice=="B":
        onoma=raw_input("Dose onomasia proiontos:")
        ON.append(onoma)
        timi=float(input("Dose timi proiontos:"))
        TIMI.append(timi)
        bubble(ON,TIMI)
       
        '''
        Εναλλακτικά μπορείτε να μη γράψετε τη συνάρτηση bubble και να γράψετε απευθείας:
        n=len(ON)
        for i in range(n-1):
            for j in range(n-1,i,-1):
                if ON[j]<ON[j-1]:
                    ON[j],ON[j-1]=ON[j-1],ON[j]
                    TIMI[j],TIMI[j-1]=TIMI[j-1],TIMI[j]
        '''
        
    if choice=="C":
        key=raw_input("Parakalo doste to onoma tou proiontos pou thelete na afairesete:")
        position=search(ON,key)
        if position != -1:
            ON.pop(position)
            TIMI.pop(position)
            plithos=plithos+1
        else:
            print "Το προϊόν δεν υπάρχει"    
    choice=raw_input("Parakalo doste tin energeia pou epithimeite:")
    while not(choice=="B" or choice=="C" or choice=="E"):
        choice=raw_input("Parakalo doste tin energeia pou epithimeite:")
if len(ON)==0:  #if ON==[]:
    print "Den pragmatopoiithikan agores"
else:
    max=TIMI[0]
    for i in range(len(ON)):
        print ON[i]
        sum=sum+TIMI[i]
        if max<TIMI[i]:
            max=TIMI[i]
    print "Agorasthkan ", len(ON)," proionta"
    print "Sinoliki aksia:",sum
    if plithos!=0:
        print "eginan ", plithos," anaireseis"
    print "Akrivotero proion:",max

