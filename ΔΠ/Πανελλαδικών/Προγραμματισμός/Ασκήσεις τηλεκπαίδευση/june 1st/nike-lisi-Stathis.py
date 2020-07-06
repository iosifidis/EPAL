# -*- coding: utf-8 -*-

epitagi=500
temaxia=0
nike=0
nike5=False
nike10=False
sinexia = "N"
sum=0


while epitagi!=0 and sinexia=="N":
    timi=float(input("Δώσε τιμή τεμαχίου:"))
    while epitagi-timi<0:
        print "Δεν μπορείς να αγοράσεις αυτό το προιόν γιατί ξεπερνά το υπόλοιπο της επιταγής σου των",epitagi,"€"
        sinexia=raw_input("Θέλετε να συνεχίσετε; N/O")
        if sinexia=="N":
            timi=float(input("Δώσε τιμή τεμαχίου:"))
        else:
            timi=0

    if epitagi-timi==0:
        print "Τέλος αγορών"
        sinexia=="O"

    if sinexia=="N":
        proion=raw_input("Δώσε όνομα προϊόντος:")
        epitagi=epitagi-timi
        sum=sum+timi
        temaxia=temaxia+1
        

        if proion=="Nike":
            nike=nike+1

        if nike>5 and nike5==False:
            epitagi=epitagi+20
            nike5=True
        elif nike-5>10 and nike10==False:
            epitagi=epitagi+30
            nike10=True
     

print "Ξοδεύτηκε",sum,'€, και αγοράστηκαν',temaxia,"προϊόντα"

if nike5==True and nike10==True:
    print 'Επωφελήθηκε από την προσφορά της Nike κατά 50€'
elif nike5==True and nike10==False:
    print "Επωφελήθηκε κατά 20 €"
else:
    print 'Δεν επωφελήθηκε από την προσφορά της Nike'
