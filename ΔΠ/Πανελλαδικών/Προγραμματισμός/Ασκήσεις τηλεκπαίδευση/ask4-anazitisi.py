# -*- coding: cp1253 -*-
'''
� ��������� �������� ���������� ����� ��������� �� ���������� ����������
�� �����-���� ��� ���������� ������ �� ������� ������� ������� ���������
��� 20%. �� ���������� ��������� �� �����: 
�. ��� ���� ��� ��� �� 28 �����-���� ��� ���������� ������, �������� ��
����� ��� �� ������� ������� ������� ���, �������������� ��� �� �������
����� ������� �������. 
�. ��������� ���������� ��� ��������� ��� ������-����� ��� ����� �� �������
��� ������� ������� ����. 
�. �������� ��� �������� ���� �������-������. 
�. ����� ��������� � ����� ������� �� ������� ������� ������� ��� ���� ��
������������ ������ ����� ��� ������� �� ����������� � ��� ������������
��������� ������. 
'''
def bubblesort(lista,lista2):
    N=len(lista)
    for i in range(N-1):
        for j in range(N-1,i,-1):
            if lista[j]<lista[j-1]:
                lista[j],lista[j-1] = lista[j-1],lista[j]
                lista2[j],lista2[j-1] = lista2[j-1],lista2[j]

def diadiki(lista,key):
    first=0
    last=len(lista)-1
    pos=-1
    while first<=last and pos==-1:
        mid=(first+last)/2
        if lista[mid]==key:
            pos=mid
        elif lista[mid]<key:
            first=mid+1
        else:
            last=mid-1
    return pos

def epidotisi(pososto):
    if pososto<20:
        print "H xora epidoteitai"
    else:
        print "H xora den epidoteitai"
        

XORA=[]
POSOSTO=[]
for i in range(28):
    x=raw_input("Dose xora:")
    XORA.append(x)
    p=float(input("Dose pososto:"))
    while not (p>=0):   #p<0
        p=float(input("Dose pososto:"))
    POSOSTO.append(p)
bubblesort(XORA,POSOSTO)
for i in range(28):
    print XORA[i], POSOSTO[i]
xora=raw_input("Dose onoma xoras:")
pos=diadiki(XORA,xora)
pososto=POSOSTO[pos]
epidotisi(pososto)


    
