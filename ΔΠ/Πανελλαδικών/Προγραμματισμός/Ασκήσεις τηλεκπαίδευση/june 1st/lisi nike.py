flag=False
epitagi=500
nike=0
temaxia=0
erotisi="N"

while erotisi=="N":
    timi=float(input("Dose timi proiontos:"))    
    while epitagi-timi>=0:
        proion=raw_input("Dose onoma proiontos:")
        epitagi=epitagi-timi

        temaxia=temaxia+1

        if proion=="Nike":
            nike=nike+1
            if nike==6:
                epitagi=epitagi+20
                flag==True
            elif nike==11:
                epitagi=epitagi+10
                flag==True

        timi=float(input("Dose timi proiontos:"))

    print "To ipoloipo den eparkei gia tin agora."
    print "Diathesimo ipoloipo:",epitagi
    if epitagi>0:
        erotisi=raw_input(" Thelete na sinexisete?N/O")
print "TELOS AGORON!"
print "Agorastikan ",temaxia," temaxia"
print "Ksodeutikan:", 500-epitagi,"Euro"
if flag==True:
    print "epofelithike"
else:
    print "Den epofelithike"
    

