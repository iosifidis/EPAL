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
            if ar[j]<ar[j-1]:    
                ar[j],ar[j-1]=ar[j-1],ar[j]
                ar2[j],ar2[j-1]=ar2[j-1],ar2[j]
    
NAME=[]
VOTE=[]
for i in range(30):
    onoma=raw_input("Dose onoma:")
    arithmos=int(input("Dose arithmo psifon:"))
    NAME.append(onoma)
    VOTE.append(arithmos)

bublesort(VOTE,NAME)
for i in range(7):
    print NAME[i]

onoma=raw_input("Dose onoma ipopsifiou:")
for i in range(7):
    if onoma==NAME[i]:
        print "Eklegetai"
    else:
        print "Den eklegetai"
    




