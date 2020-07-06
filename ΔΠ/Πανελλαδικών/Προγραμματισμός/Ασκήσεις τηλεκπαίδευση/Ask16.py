# -*- coding: cp1253 -*-
'''
�� ��� ����������� ��������� (e-shop) �������� �����, ���� ���� ��� � ������� �������� ��� ��� ������ ��� �����, ���� ���� �� ��� ���� ��� ������������� ��� ������ ������ ���� �� �� ��� ��������� ��� ���� ��������.�� ����� �� ��������� ������ ����� ���, ����� ��� ������� ��� �� ������ ������. 
�� ���������� ��������� ��� ������������� �� ������ ������ ��� ������������ ��� ��� ������, �� ����:
�. �� ������������ ��� ������ ON ��� �I�I ��� ��� ��������� ��� �������� ������, ���� ���� ����� �� ������������� �� ��������� ��� ��������� ��� ��� ������� �� ����������� ����� ����.

�. �� �������� ������������ ��� �������� ��� ������ ���������� ��� ������� ���� ��� ������������� �����.
������������� ����� ����� �B� ��� ����� ���� ���������, �C� ��� ������� ��� ���������� ������ ��� ��� �E� ��� ���������� ��� ������. �� � ������� �������� ��� ��� ������, ����:
i.  �� �������� ��� �������� ������ ���� ��� ��� �� �� ������� ��� ������ ������ (���� 2 ������).
ii. ��� �������� �� �������� �� ������������� ���� ��� ��������� ���� �� ������� ����������.

�� � ������� ����� �� �������� ������ ����� ���, ����: 
i.  �� ����� ��������� �������� ���������� �� ��� �������� ��� ��������� ��� �������� �� ��������� ���, �� �� ������ ������� ��� ������ ������, �� ���������������� � ��������, 
ii.  ����������� ��������� �� ������ ��� ������ ��� �������.

� ���������� ��������������� ����� � ������� �� �������� ��� ���������� ��� ������ ���.

�. �� �� ������ ������ ����� ����� �� ��������� �� ������ ���� ����������������� ������, �����������:
i.  �� ��������� �� ����� ���� ���������, �� ������ ��� ��������� ��� �� �������� ���� ����.
ii.  �� ����������������� ���������� ������, �� ��������� ����� ����� ���������������� �������� ���������.
iii.  �� ��������� ��� �������� ��� ��������� �� �� ���������� ����.
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
        ����������� �������� �� �� ������� �� ��������� bubble ��� �� ������� ���������:
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
            print "�� ������ ��� �������"    
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

