# -*- coding: utf-8 -*-
'''
Οι λέξεις που ορίζονται σε ένα λεξικό παρατίθενται αλφαβητικά. Ο ορισμός
κάθε λέξης καταλαμβάνει μία ή και περισσότερες γραμμές.
Να γράψετε αλγόριθμο ο οποίος, για ένα λεξικό 50 χιλιάδων λέξεων:
Δ1. Διαβάζει το πλήθος Χ των γραμμών που χωράει μια σελίδα του λεξικού.
Η τιμή αυτή είναι κοινή για όλες τις σελίδες.
Δ2.Διαβάζει κάθε λέξη και το μήκος του ορισμού της σε γραμμές και
αποθηκεύει τα δεδομένα αυτά στους μονοδιάστατες λίστες LEXI και MIKOS,
αντίστοιχα. Να εξασφαλίσετε με κατάλληλους ελέγχους ότι κανένας ορισμός
δεν εκτείνεται σε περισσότερες από Χ γραμμές. Οι λέξεις δίνονται με τυχαία
σειρά.
Δ3. Ταξινομεί τις λέξεις σε αύξουσα αλφαβητική σειρά.
Δ4. Υπολογίζει και αποθηκεύει σε, παράλληλη με τη LEXI, λίστα ακεραίων PAGE,
τον αριθμό της σελίδας στην οποία βρίσκεται κάθε λέξη. Να ληφθεί υπόψη πως
όταν ο ορισμός μιας λέξης δε χωράει ολόκληρος σε μια σελίδα, τότε οι γραμμές
του ορισμού που περισσεύουν τοποθετούνται στην επόμενη σελίδα. Θεωρούμε ωστόσο
ότι η λέξη βρίσκεται στη σελίδα όπου ξεκινά ο ορισμός της. 

Δ5. Να καλεί τη συνάρτηση CreateLetters() η οποία επιστρέφει μια λίστα με
τα 24 γράμματα του αλφαβήτου και θα χρησιμοποιηθούν παρακάτω. Η συνάρτηση δεν
χρειάζεται να κατασκευαστεί. Θεωρείστε ότι υπάρχει ήδη.

Δ6. Αξιοποιώντας τη λίστα που επιστρέφει το ερώτημα Δ5, να κατασκευάζει κι
εμφανίζει παράλληλη λίστα ακεραίων Ε, η οποία έχει τη μορφή ευρετηρίου.
Συγκεκριμένα, κάθε στοιχείο της λίστας Ε αντιστοιχεί σε ένα γράμμα και η
τιμή του είναι ο αριθμός σελίδας στην οποία βρίσκεται η πρώτη λέξη που ξεκινά
με το γράμμα αυτό. Για παράδειγμα, το γράμμα Ω βρίσκεται στη θέση 23 στη
λίστα των γραμμάτων και αν η πρώτη λέξη που ξεκινά από Ω βρίσκεται στη σελίδα
765, τότε το Ε[23] θα πρέπει να έχει την τιμή 765. Να υποθέσετε ότι για κάθε
γράμμα υπάρχει στο λεξικό τουλάχιστον μια λέξη που να ξεκινά από αυτό.
Υπόδειξη: Το γράμμα από το οποίο ξεκινά μια λέξη μπορεί να βρεθεί
συγκρίνοντας τη λέξη με τα γράμματα του αλφαβήτου που βρίσκονται στον πίνακα
των γραμμάτων. Για παράδειγμα, αν για μια λέξη λ γνωρίζουμε ότι λ ≥ ‘Π’ αλλά
και λ < ‘Ρ’, τότε μπορούμε να συμπεράνουμε ότι η λέξη ξεκινά από
(ή ταυτίζεται με) το γράμμα Π.
'''

X=int(input("Poses grammes exei mia selida?"))

LEXI=[]
MIKOS=[]
for i in range(50000):
    lexi=raw_input("Doste leksi:")
    mikos=int(input("Se poses grammes orizetai auti i leksi?"))
    while mikos>X:
        mikos=int(input("Dosate polles grammes. Parakalo oriste ligoteres"))
    LEXI.append(lexi)
    MIKOS.append(mikos)

bubblesort(LEXI,MIKOS)

PAGE=[]
sum=0
sel=1
i=0
while i<50000:
    if sum+MIKOS[i]<X:
        sum=sum+MIKOS[i]
        PAGE.append(sel)
    else:
        PAGE.append(sel)
        sel=sel+1
        sum=MIKOS[i]-(X-sum)
    i=i+1

L=CreateLetters()
E=[]
j=0
for i in range(50000):
    done=False
    while j<=22 and done==False:
        if LEXI[i]>=L[j] and LEXI[i]<L[j+1]:
            E[j]==PAGE[i]
            done=True
            j=j+1
        else:
            done=False
    if j==23 and done==False:
        if LEXI[i]>=L[j]:
            E[j]==PAGE[i]
            done=True




            
        

