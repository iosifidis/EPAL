#ASKHSH1

'''
pl=0
athr=0
while athr <=500:
       size=int(input("Δώσε μέγεθος αρχείου"));
       athr=athr+size;
       pl=pl+1;
print ("Συνολικό πλήθος αρχείων:",pl,athr);
'''
#ASKHSH2
'''
seira=0;
athr=0
baros=int(input("Δώσε βάρος 1ου ατόμου:"));
while athr+baros <=500:
        athr=athr+baros;        
        seira=seira+1;
        baros=int(input("Δώσε βάρος 1ου ατόμου:"));
print (seira,athr);
'''

#ASKHSH3
'''
plithos_a_thesis=0;
syn_poso=0;
for i in range(6):
    kat=int(input("Δώσε κατηγορία 0 ή 1:  "));
    if kat==0:
       plithos_a_thesis=plithos_a_thesis+1;
       syn_poso=syn_poso+50;         
    else:
       syn_poso=syn_poso+20;
print ("Πλήθος επιβατών Α' θέσης:",plithos_a_thesis);      
print ("Συνολικό ποσό που εισπράχθηκε:",syn_poso,"Ευρώ");
'''
              
 #ASKHSH4
'''
pl=0;
meg=0;
arith=int(input("Δώσε αριθμό κυκλοφορίας:"));
meg_arith=0
syn_poso=0;
while arith!=99:
       poso=int(input("Δώσε ποσό κλήσης:"));
       syn_poso=syn_poso+poso;
       pl=pl+1;
       if poso >=meg:  
              meg=poso;
              meg_arith=arith;
       arith=int(input("Δώσε αριθμό κυκλοφορίας:"));
print ("Συνολικό πλήθος οχημάτων:",pl);
print ("Συνολικό ποσό που εισπράχθηκε:",syn_poso,"Ευρώ");
print("Αριθμός κυκλοφορίας με μεγαλύτερο ποσό:",meg_arith,"με ποσό:",meg,"Ευρώ");
'''
#ASKHSH5
'''
seira=0;
athr=0
kod=int(input("Δώσε κωδικό: "));
while kod!=0:
        name=input ("Δώσε ονοματεπώνυμο: ")
        timi=int(input("Δώσε τιμή: "));
        tropos=int(input("Δώσε τρόπο πληρωμής 1,2 ή 3: "));
        if tropos==1:
               poso=timi-timi*3/100.0;
               message="Απολύτως μετρητοίς";
        elif tropos==2:
               poso=timi;
               message="Εξόφληση σε 15 ήμέρες";
        else:
               poso=timi+timi*12/100.0;
               message="Εξόφληση εντός 6 μηνών";
        print (kod,name," ",poso," Ευρώ"," ",message);
        kod=int(input("Δώσε κωδικό: "));
 '''       
#ASKHSH6
'''def meg(x,y):
       if x>y:
              return x;
       else:
              return y;

elax=300;
onoma=input("Δώσε Όνομα υποψηφίου: ");
elax_name=" ";
while onoma!="TELOS":
        vath1=int(input ("Δώσε βαθμό1: "))
        vath2=int(input ("Δώσε βαθμό2: "));
        vath3=int(input ("Δώσε βαθμό3: "));
        print (" Ο μεγαλύτερος βαθμός είναι:  ",meg(meg(vath1,vath2),vath3));
        athr=vath1+vath2+vath3;
        if (athr/3.0 >=55)and (vath1>=50) and (vath2>=50) and (vath3>=50):
               print("O",onoma,"  έχει συνολική βαθμολογία  ", athr);
               if athr<elax:
                      elax=athr;
                      elax_name=onoma;
        onoma=input("Δώσε Όνομα υποψηφίου: ");               
print("Ο επιτυχών με τη μικρότερη συνολική βαθμολογία είναι ο:  ",elax_name);
'''    

                      

