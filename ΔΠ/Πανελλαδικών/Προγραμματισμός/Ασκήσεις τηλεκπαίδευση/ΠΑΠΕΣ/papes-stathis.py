def bubblesort(lista,lista2):
    n=len(lista)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if lista[j]>lista[j-1]:
                lista[j],lista[j-1]=lista[j-1],lista[j]
                lista2[j],lista2[j-1]=lista2[j-1],lista2[j]

def diadiki_me_thesi(lista,key):
    first=0
    last=len(lista)-1
    position=-1
    while first<=last and position==-1:
        mid=(first+last)/2
        if lista[mid]==key:
            position=mid
        elif lista[mid]<key:
            first=mid+1
        else:
            last=mid-1
    return position

PAPES=[]
VOTES=[]
PROTOS=[]
for i in range(18):
    pope=raw_input("Dose ipopsifiotita:")
    PAPES.append(pope)
papas=False
while papas==False:
    for i in range(18):
        VOTES[i]=0

    for i in range(115):
        vote=raw_input("Poion psifizeis:")
        thesi=diadiki_me_thesi(PAPES,vote)
        if thesi != -1:
            VOTES[thesi]=VOTES[thesi]+1

    bubblesort(VOTES,PAPES)

    PROTOS.append(PAPES[0])

    if VOTES[0]>2.0/3*115:
        print "Leukos Kapnos"
        papas=True
    else:
        print "Mauros kapnos"
        papas=False
        
print PAPES[0]

for i in range(len(PROTOS)):
    if PROTOS[i]==PROTOS[0]:
        favori=True
    else:
        favori=False
if PROTOS[0]==PAPES[0] and favori==True:
    print 'FAVORI'
else:
    print 'AOUTSIDER'

