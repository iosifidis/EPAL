# -*- coding: cp1253 -*-
'''
��� ��� �������� ��� ���������� ����������� ���������� ��� ������������
�������� ���� ������ �������� ������� ���������. �� ������� ��������� ��
�����:
�. �������� ��� ������� ���� ������ NAME ��� VOTE, �� ����� ����
��������� ��� ��� ������ ��� ����� ��� �����.
�. ����� ��������� � ����� ��������� �� ������� ��� ���������� ����� ���
����������� ���������� ���� �������� ����� ����� (�� �������� ��� ���
�������� ����������� ���������).
�. �������� �� ����� ���� ��������� ��� ������� �� �
������������� ��������� ��������� � ���, ������������ ��������� ������.
'''
def bublesort(ar,ar2):
    n=len(ar)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if ar[j]>ar[j-1]:    
                ar[j],ar[j-1]=ar[j-1],ar[j]
                ar2[j],ar2[j-1]=ar2[j-1],ar2[j]

def search(L,key):
    first=0
    last=len(L)-1
    position=-1 #found=False
    while first<last and position==-1: #found==False
        mid=(first+last)/2
        if L[mid]==key:
            position=mid #found=True
        elif L[mid]<key:
            first=mid+1
        else:
            last=mid-1
    return position #return found

NAME=[]
VOTE=[]
for i in range (30):
    name=raw_input("onoma:")
    vote=int(input("psifos:"))
    NAME.append(name)
    VOTE.append(vote)
bubblesort(VOTE,NAME)
name=raw_input("onoma iposifiou:")
pos=search(NAME,name)
if pos!=-1:
    print "o ypopsifios den iparxei"
elif pos<7:
    print "o ypopsifios ", NAME[pos]," eklegetai"
else:
    "o ypopsifios ", NAME[pos]," den eklegetai"


    
