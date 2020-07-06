#ΑΣΚΗΣΗ 1
'''def taxin(L):
    correct = True
    i = 0
    N = len(L)-1
    while correct and i<N :
        if (L[ i ] > L[ i+1 ]) :
          correct = False
        i = i +1
    return correct

M=[2,5,12,18,24,32];
M1=[3,8,14,12,25];
if taxin(M)==True:
    print ("η λίστα είναι ταξινομημένη");
else:
   print ("η λίστα δεν είναι ταξινομημένη"); 
keno=input("πατήστε ένα πλ΄ηκτρο για να συνεχίσετε:");
control=taxin(M1);
if control==True:
    print ("η λίστα είναι ταξινομημένη");
else:
   print ("η λίστα δεν είναι ταξινομημένη");
'''

#ΑΣΚΗΣΗ 2
'''
def count_true( List ) :
      true_values = 0
      for i in List :
         if i=='True' :
              true_values = true_values + 1
      return true_values;

L=[];
for i in range(5):
    timi=input("Δώστε True ή False:");
    print(timi);
    L.append(timi);
print (L);
k=count_true(L);
print (k);
for i in range(5):
    if i< k:
        L[i]=True
    else:   
        L[i]=False;
print (L);        
'''   
#ΑΣΚΗΣΗ 3
'''
def insSort(L) :
           number = int(input("Δώστε αριθμό: "));
           while (number !=0) :   
                L.append(number);
                value = L[ len(L) - 1 ]
                j = len(L) - 1
                while j > 0 and L[ j-1 ] < value :
                     L[ j ] = L[ j-1 ];
                     j = j-1;
                     L[ j ] = value;
                number = int(input("Δώστε αριθμό: "));
           return L;

L = [ ]
insSort(L);
print (L);
'''
#ΑΣΚΗΣΗ 4
'''
def bubbleSort( A ):
      N = len( A )
      for i in range( N ):
            for j in range(N-1, i, -1):
                  if A[ j ] < A[ j-1 ] :
                        A[ j ], A[ j-1 ] = A[ j-1 ], A[ j ]


def binarySearch( A, key ):
      last = len( A ) - 1
      first = 0
      found = False
      while first <= last and not found:
            mid = (last + first) // 2
            if A[ mid ] == key :
                  found = True
            elif A[ mid ] < key :
                  first = mid + 1
            else:
                  last = mid - 1
      return found


A=[];
B=[];
for i in range(10):
      ar=int(input("Δώστε αριθμό για την πρώτη λίστα: "));
      A.append(ar);
      
for i in range(5):
      ar=int(input("Δώστε αριθμό για την δεύτερη λίστα: "));
      B.append(ar);      

bubbleSort( A );
count = 0
for item in B :
      if binarySearch( A, item )==True :
            count = count + 1;


print ("Πλήθος κοινών στοιχείων = ", count);
'''
#ΑΣΚΗΣΗ 5
'''
def bubbleSort( A ):
      N = len( A )
      for i in range( N ):
            for j in range(N-1, i, -1):
                  if A[ j ] < A[ j-1 ] :
                        A[ j ], A[ j-1 ] = A[ j-1 ], A[ j ];

def binarySearch( A, key ):
      last = len( A ) - 1;
      first = 0;
      found = False;
      while first <= last and not found:
            mid = (last + first) // 2;
            if A[ mid ] == key :
                  found = True;
            elif A[ mid ] < key :
                  first = mid + 1;
            else:
                  last = mid - 1;
      return found;

nameList = [ ]
name = input("Δώστε όνομα: ")
while name != ' ' :
      nameList.append( name )
      name = input("Δώστε όνομα: ");
bubbleSort( nameList);
onoma = input("Δώστε όνομα:που ψάχνετε στη λίστα: ")
found = binarySearch( nameList, onoma);
if found == True:
          print ("Το όνομα υπάρχει στη λίστα");
else :
         print ("Το όνομα δεν υπάρχει στη λίστα");
'''
#ΑΣΚΗΣΗ 6
'''def bubbleSort( A ,B):
      N = len( A )
      for i in range( N ):
            for j in range(N-1, i, -1):
                  if A[ j ] > A[ j-1 ] :
                        A[ j ], A[ j-1 ] = A[ j-1 ], A[ j ];
                        B[ j ], B[ j-1 ] = B[ j-1 ], B[ j ];
                  elif A[ j ] == A[ j-1 ] :
                       if B[ j ] < B[ j-1 ] :
                             B[ j ], B[ j-1 ] = B[ j-1 ], B[ j ]; 

nameList = [ ]
vathList=[];
vath = int(input("Δώστε βαθμό: "));        
while vath>0:
      name = input("Δώστε όνομα: ");
      vathList.append(vath);
      nameList.append(name);
      vath = int(input("Δώστε βαθμό: ")); 
bubbleSort(vathList,nameList);
for i in range (len(nameList)):
      print(nameList[i],vathList[i]);
'''      






















           
